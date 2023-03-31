import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem, QHeaderView, QFileDialog, QMessageBox
import time
import datetime
import pymysql
import paramiko
import ssh_config
import generate_password
from db_config import *
from Class_Mysql import *
from Class_User import *
from Class_Processing import *
from Ui_Login import *
from Ui_Event_shedule import *
from Ui_Event import *
from Ui_Add_participant import *
from Ui_Analisis_list import *
from Ui_Accept_docs import *
from Ui_Create_event import *
from Ui_Create_participant import *
from Ui_Create_organization import *
from Ui_Create_inspector import *
from Ui_Create_user import *
from Ui_List_organization import *
from Ui_List_participants import *
from Ui_Choose_organization import *
from Ui_Upload_docs import *


class Login(Ui_Login):
    """Класс работы с окном Вход в программу"""
    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_bad_password.setText('')
        self.label_user_not_found.setText('')

        # disabled after debug
        self.lineEdit_login.setText(login_name)
        self.lineEdit_password.setText(login_password)

        self.clicked_connect()
        dialog.show()
        app.exit(app.exec())

    def clicked_connect(self):
        """Обработка нажатий кнопки Логин в окне 'Вход в программу'"""
        self.pushButton_login.clicked.connect(self.check_access)

    def check_access(self):
        """Обработка входящих логина и пароля"""
        global user_login
        login = {}
        table_name = 'users'
        self.label_bad_password.setText('')
        self.label_user_not_found.setText('')
        login['phone_number'] = self.lineEdit_login.text().strip()
        login['password'] = self.lineEdit_password.text().strip()
        journal.log(f'Попытка входа с учетными данными: {login}')
        user_login = Mysql().select_one(login, table_name)
        journal.log(f"Пользователь: {user_login['second_name']} {user_login['first_name']} вошел в систему")


class Event_shedule(Ui_Event_shedule):
    """Класс работы с окном Расписание Мероприятий"""
    def __init__(self):
        window = QMainWindow()
        super().setupUi(window)
        self.username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{self.username_login_role}')
        # Установка ResizeToContents для tree_event
        self.tree_event_shedule.header().setStretchLastSection(False)
        self.tree_event_shedule.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Установка наименований столбцов и центрирование открываемого окна
        self.adjust_tree(self.tree_event_shedule)
        self.move_to_centre(window)
        # Чтение мероприятий из базы данных
        self.db = Mysql()
        self.table_name = 'events'
        self.all_events = self.db.select_all(self.table_name)
        # Формирование расписания мероприятий
        self.events_list()
        self.clicked_connect(window)
        window.showMaximized()
        window.show()
        sys.exit(app.exec())

    def move_to_centre(self, window):
        """Выравниваем окно по центру экрана"""
        desktop = QApplication.desktop()
        desktop.screenGeometry()
        x = (desktop.width() - window.width()) // 2
        y = (desktop.height() - window.height()) // 2
        window.move(x, y)

    def adjust_tree(self, tree):
        """Установка наименований для колонок Tree"""
        columns_names = ['id', '№_', 'Мероприятие', 'Дата и время', 'Страна', 'Город', 'Участников', 'Организация', 'Статус']
        for i in columns_names:
            tree.headerItem().setText(columns_names.index(i), i)
        self.tree_event_shedule.setColumnHidden(0, True)

    def clicked_connect(self, window):
        """Обращения к классам окон по клику мыши"""
        self.tree_event_shedule.itemDoubleClicked.connect(self.open_event)
        self.tree_event_shedule.itemDoubleClicked.connect(self.update_events_shedule)
        self.pushButton_exit.clicked.connect(self.close_shedule)
        self.pushButton_exit.clicked.connect(window.close)
        self.pushButton_create_event.clicked.connect(Create_Event)
        self.pushButton_create_event.clicked.connect(self.update_events_shedule)
        self.pushButton_create_participant.clicked.connect(Create_participant)
        self.pushButton_create_organization.clicked.connect(Create_organization)
        self.pushButton_create_inspector.clicked.connect(Create_inspector)
        self.pushButton_list_organization.clicked.connect(List_organization)
        self.pushButton_list_of_all_participants.clicked.connect(List_participants)
        # self.pushButton_open_event.clicked.connect(Event)
        self.pushButton_export_xls.clicked.connect(window.showMaximized)
        self.pushButton_print.clicked.connect(Create_user)
        # self.pushButton_find_event.clicked.connect(self.tree_event_shedule.clear)

    def open_event(self):
        """Открытие Мероприятия из списка в Event_shedule"""
        try:
            dct = {}
            item = self.tree_event_shedule.currentItem()
            print(f'Выбрана строка для открытия {item}')
            dct['id'] = item.text(0)
            dct_event = self.db.select_one(dct, self.table_name)
            Event(dct_event)
        except Exception as ex:\
            print("Не выделен ни один объект в дереве")

    def events_list(self):
        """Вывод списка Мероприятий в Event Shedule"""
        event_string = []
        number = 1
        for dct in self.all_events:
            event_string.append(str(dct['id']))
            event_string.append(str(number))
            event_string.append(dct['event_name'])
            event_string.append(dct['date_time'].strftime('%d-%m-%Y %H:%M'))
            event_string.append(dct['country'])
            event_string.append(dct['city'])
            event_string.append(str(dct['count']))
            organization = self.set_organization(dct)
            event_string.append(organization['organization_name'])
            event_string.append(str(dct['status']))
            item = QTreeWidgetItem(event_string)
            self.tree_event_shedule.addTopLevelItem(item)
            event_string.clear()
            number += 1
        self.label_total_completed_events.setText(f"Всего в списке {len(self.all_events)} мероприятий")

    def set_organization(self, dct_event):
        """Извлечение {} организации из таблицы соответствия organizations_events"""
        # Получаем соответствие id События = id Организация
        event_id = {}
        event_id['event_id'] = dct_event['id']
        dct = self.db.select_one(event_id, 'organizations_events')
        # Извлекаем организацию по полученному соответсвию
        organization_id = {}
        organization_id['id'] = dct['organization_id']
        organization = self.db.select_one(organization_id, 'organizations')
        return organization

    def update_events_shedule(self):
        """Функция обновления списка Расписание Мероприятий"""
        self.tree_event_shedule.clear()
        db = Mysql()
        update_events = db.select_all(self.table_name)
        self.all_events = update_events
        self.events_list()

    def close_shedule(self):
        """Запись лога выхода, по нажатию на кнопку Выход"""
        journal.finish_log(f'{self.username_login_role}')


class Event(Ui_Event):
    """Работа с окном Мероприятие"""
    def __init__(self, dct_event):
        self.dct_event = dct_event
        self.table_name = 'events'
        self.db = Mysql()

        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.adjust_tree()
        self.output_form()
        self.participants_event_list = self.get_participants()
        print(self.participants_event_list)
        self.set_list_participants_events()
        self.clicked_connect(dialog)
        dialog.exec()

    def get_participants(self):
        """Получение списка участников Мероприятия по id"""
        try:
            dct = {}
            dct['event_id'] = self.dct_event['id']
            relation = self.db.select_every(dct, 'events_participants')
            # Если записей соответствия в таблице нет, то выходим из функции, отображая пустой список
            if relation == ():
                return None
            # Получаем relation = списку словарей соответствия event_id = participant_id
            # Удаляем из списка словарей ключи event_id
            # Забираем всех participants по их id в список словарей
            participants = []
            for slovar in relation:
                slovar['id'] = slovar['participant_id']
                del slovar['event_id']
                del slovar['participant_id']
                dct = self.db.select_one(slovar, 'participants')
                participants.append(dct)
            # print(participants)
            return participants
        except Exeption as ex:
            print(f"Ошибка!")

    def adjust_tree(self):
        """Установка наименований для колонок списка"""
        # Установка ResizeToContents для treeWidget_list_participance
        self.tree_event_participants_list.header().setStretchLastSection(False)
        self.tree_event_participants_list.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        columns_names = ['id', '№_', 'Фамилия', 'Имя', 'Отчество', 'Город', 'Телефон', 'e-mail', 'Пароль']
        for i in columns_names:
            self.tree_event_participants_list.headerItem().setText(columns_names.index(i), i)
        self.tree_event_participants_list.setColumnHidden(0, True)

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок"""
        self.pushButton_ok.clicked.connect(self.update_event)
        self.pushButton_ok.clicked.connect(dialog.close)
        self.pushButton_del_event_participant.clicked.connect(self.delete_participant_from_event)
        self.pushButton_add_event_participant.clicked.connect(lambda: Add_participant(self.dct_event))
        self.pushButton_add_event_participant.clicked.connect(self.update_list_participants_events)
        self.pushButton_analisis_doc.clicked.connect(Analisis_list)
        self.pushButton_open_access.clicked.connect(self.open_access)
        self.pushButton_close_access.clicked.connect(self.close_access)
        self.pushButton_select_organization.clicked.connect(Choose_organization)
        self.pushButton_select_organization.clicked.connect(self.set_choose_organization)

    def output_form(self):
        """Заполняем поля данных Мероприятия из полученного словаря dct_event"""
        # self.label_Event.setText(f"Мероприятие  № {self.dct_event['id']}")
        self.lineEdit_event_name.setText(self.dct_event['event_name'])
        self.lineEdit_event_theme.setText(self.dct_event['event_theme'])
        self.organization = self.set_organization()
        self.lineEdit_selected_organization.setText(self.organization['organization_name'])
        self.event_dateTime.setDateTime(self.dct_event['date_time'])
        self.lineEdit_event_country.setText(self.dct_event['country'])
        self.lineEdit_event_city.setText(self.dct_event['city'])
        self.lineEdit_type_event.setText(self.dct_event['type'])
        self.lineEdit_event_comment.setText(self.dct_event['comment'])
        status = self.comboBox_event_status.findText(self.dct_event['status'])
        self.comboBox_event_status.setCurrentIndex(status)
        access = self.dct_event['access']
        if access == 1:
            self.pushButton_open_access.setText("Открыт")
        else:
            self.pushButton_close_access.setText('Закрыт')

    def set_list_participants_events(self):
        """Участники Мероприятия"""
        if self.participants_event_list == None:
            self.dct_event['count'] = 0
            return
        participants = self.participants_event_list
        self.tree_event_participants_list.clear()
        participant_string = []
        number = 1
        for dct in participants:
            participant_string.append(str(dct['id']))
            participant_string.append(str(number))
            participant_string.append(dct['second_name'])
            participant_string.append(dct['first_name'])
            participant_string.append(dct['last_name'])
            participant_string.append(dct['city'])
            participant_string.append(dct['phone_number'])
            participant_string.append(dct['email'])
            participant_string.append(dct['password'])
            item = QTreeWidgetItem(participant_string)
            self.tree_event_participants_list.addTopLevelItem(item)
            participant_string.clear()
            number += 1

        self.label_total_participants.setText(f"Всего в списке {len(participants)} участников")
        self.dct_event['count'] = len(participants)

    def delete_participant_from_event(self):
        """Удаление участника из списка Мероприятия"""
        # Считываем выделенную строку, получаем из нее participant_id
        # По event_id и participant_id удаляем строку в таблице events_participants
        # Обновляем список
        self.participant = {}
        item = self.tree_event_participants_list.currentItem()
        if item == None:
            self.show_message_not_select()
            return
        self.participant['id'] = item.text(0)
        full_relation = self.processing_relation()
        self.db.delete_row(full_relation, 'events_participants')
        self.update_list_participants_events()

    def show_message_not_select(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Внимание")
        msg_box.setText('Не выделен ни один участник')
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def processing_relation(self):
        """Получение id строки, по event_id и participant_id из таблицы events_participants"""
        relation = {}
        relation['event_id'] = self.dct_event['id']
        relation['participant_id'] = self.participant['id']
        full_relation = self.db.select_one(relation, 'events_participants')
        return full_relation

    def update_list_participants_events(self):
        """Обновление списка участников Мероприятия"""
        self.participants_event_list = self.get_participants()
        self.set_list_participants_events()

    def set_organization(self):
        """Извлечение {} организации из таблицы соответствия organizations_events"""
        # Получаем соответствие id События = id Организация
        event_id = {}
        event_id['event_id'] = self.dct_event['id']
        dct = self.db.select_one(event_id, 'organizations_events')
        # Извлекаем организацию по полученному соответсвию
        organization_id = {}
        organization_id['id'] = dct['organization_id']
        organization = self.db.select_one(organization_id, 'organizations')
        return organization

    def set_choose_organization(self):
        """Установка выбранной организации в текстовое поле через глобальную переменную organization_dct"""
        global organization_dct
        self.organization = organization_dct
        self.lineEdit_selected_organization.setText(organization_dct['organization_name'])
        # organization_dct = self.organization

    def update_event(self):
        """Обновление текстовых полей"""
        self.dct_event['event_name'] = self.lineEdit_event_name.text()
        self.dct_event['event_theme'] = self.lineEdit_event_theme.text()
        self.dct_event['date_time'] = self.event_dateTime.dateTime().toString("yyyy-MM-dd hh:mm")
        self.dct_event['country'] = self.lineEdit_event_country.text()
        self.dct_event['city'] = self.lineEdit_event_city.text()
        self.dct_event['type'] = self.lineEdit_type_event.text()
        self.dct_event['comment'] = self.lineEdit_event_comment.text()
        self.dct_event['status'] = self.comboBox_event_status.currentText()
        # self.dct_event['count'] = 0
        self.update_in_db()

    def update_in_db(self):
        """Запись изменений текстовых полей в базу данных"""
        db = Mysql()
        db.update_row(self.dct_event, self.table_name)

        relation = {}
        relation["event_id"] = self.dct_event['id']
        relation = db.select_one(relation, 'organizations_events')
        relation["organization_id"] = self.organization['id']
        db.update_row(relation, 'organizations_events')

    def open_access(self):
        self.dct_event['access'] = 1
        self.pushButton_open_access.setText("Открыт")
        self.pushButton_close_access.setText('Закрыть доступ для организации')
        print(f"Доступ для организации {self.dct_event['access']}")

    def close_access(self):
        self.dct_event['access'] = 0
        self.pushButton_close_access.setText('Закрыт')
        self.pushButton_open_access.setText("Открыть доступ для организации")
        print(f"Доступ для организации {self.dct_event['access']}")

    def comboBox(self):
        pass
        # combo_box.findText(текст) - поиск элемента по тексту в выпадающем списке. Возвращает int
        # ui.comboBox.currentText() - получение значения из QComboBox. Возвращает строку
        # combo_box.currentIndex() - возвращает целое число, т.е. Индекс выбранного элемента
        # combo_box.setCurrentIndex(индекс) - он установит элемент с заданным индексом


class Add_participant(Ui_Add_participant):
    """Окно добавления участника в Мероприятие"""
    def __init__(self, dct_event):
        self.dct_event = dct_event
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.db = Mysql()
        participants = self.db.select_all('participants')
        self.label_username_login_role.setText(f'{username_login_role}')
        self.adjust_tree()
        self.set_list_view(participants)
        self.clicked_connect(dialog)
        dialog.exec()

    def adjust_tree(self):
        """Установка наименований для колонок списка"""
        self.tree_add_participant_to_event.header().setStretchLastSection(False)
        self.tree_add_participant_to_event.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        columns_names = ['id', '№', 'Телефон', 'Фамилия', 'Имя', 'Отчество', 'e-mail']
        for i in columns_names:
            self.tree_add_participant_to_event.headerItem().setText(columns_names.index(i), i)
        self.tree_add_participant_to_event.setColumnHidden(0, True)

    def clicked_connect(self, dialog):
        """Назначения действий на нажатия кнопок"""
        self.tree_add_participant_to_event.itemDoubleClicked.connect(self.add_selected)
        self.pushButton_find.clicked.connect(self.find_participant)

    def add_selected(self):
        """Добавление выбранного участника в мероприятие"""
        # insert to events_participants
        # добавить участника в list
        try:
            dct = {}
            item = self.tree_add_participant_to_event.currentItem()
            dct['participant_id'] = item.text(0)
            dct['event_id'] = self.dct_event['id']
            print(f'Составлен словарь {dct}')
            # Проверяем нет ли такого участника в этом Мероприятии. Если нет, то добавляем.
            check = self.db.select_one(dct, 'events_participants')
            if check == None:
                self.db.insert_row(dct, 'events_participants')
                dct = self.add_entry_participants_event_data(dct)

                self.db.insert_row(dct, 'participants_event_data')
                self.show_message_add_participant()
                journal.log(f"В Мероприятие {self.dct_event['event_name']} добавлен участник {check['second_name']} {check['first_name']}")
            else:
                self.show_message_participant_exist()


        except Exception as ex:\
            print("Не выделен ни один объект в дереве")

    def select_path_participants_event_data(self, dct):
        """Забираем profile_path из таблицы participants_data"""
        del dct['event_id']
        dct_participants_data = self.db.select_one(dct, 'participants_data')
        return dct_participants_data['profile_path']


    def add_entry_participants_event_data(self, dct):
        """Заполняем словарь dct для вставки row в таблицу participants_event_data"""
        dct['path'] = self.select_path_participants_event_data(dct)
        dct['event_id'] = self.dct_event['id']
        id = self.dct_event['id']
        dct['act'] = f'{id}_act'
        dct['agreement'] = f'{id}_agreement'
        dct['contract'] = f'{id}_contract'
        dct['survey'] = f'{id}_survey'
        dct['act_exist'] = False
        dct['act_accept'] = False
        dct['agreement_exist'] = False
        dct['agreement_accept'] = False
        dct['contract_exist'] = False
        dct['contract_accept'] = False
        dct['survey_exist'] = False
        dct['survey_accept'] = False
        return dct

    def show_message_participant_exist(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Внимание")
        msg_box.setText('Участник уже присутствует в списке мероприятия.')
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def show_message_add_participant(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Оповещение")
        msg_box.setText("Участник добавлен(а).")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def set_list_view(self, participants):
        """Список участников для добавления в Мероприятие"""
        self.tree_add_participant_to_event.clear()
        participant_string = []
        number = 1
        # ( id, №__, phone_number, second_name, first_name, last_name, email)
        for dct in participants:
            participant_string.append(str(dct['id']))
            participant_string.append(str(number))
            participant_string.append(dct['phone_number'])
            participant_string.append(dct['second_name'])
            participant_string.append(dct['first_name'])
            participant_string.append(dct['last_name'])
            participant_string.append(dct['email'])
            item = QTreeWidgetItem(participant_string)
            self.tree_add_participant_to_event.addTopLevelItem(item)
            participant_string.clear()
            number += 1
        # self.label_total_participants.setText(f"Всего в списке {len(participant_string)} участников")

    def find_participant(self):
        """Поиск участника по телефону или фамилии или email"""
        table_name = 'participants'
        phone = self.lineEdit_find_by_phone.text()
        second_name = self.lineEdit_find_by_second_name.text()
        email = self.lineEdit_find_by_email.text()
        dct = self.check_find_request(phone, second_name, email)
        if dct == {}:
            find_result = self.db.select_all(table_name)
        else:
            find_result = self.db.select_every(dct, table_name)
        self.set_list_view(find_result)

    def check_find_request(self, phone, second_name, email):
        """Проверка введенных пользователем данных для поиска"""
        dct = {}
        if len(phone) == 0:
            pass
        elif phone.isdigit():
            dct.setdefault('phone_number', phone)
        else:
            self.lineEdit_find_by_phone.setText('Не корректно')

        if len(second_name) == 0:
            pass
        elif second_name.isalpha():
            dct.setdefault('second_name', second_name)
        else:
            self.lineEdit_find_by_second_name.setText('Не корректно')

        if len(email) == 0:
            pass
        elif "@" in email:
            dct.setdefault('email', email)
        else:
            self.lineEdit_find_by_email.setText('Не корректно')
        return dct


class Choose_organization(Ui_Choose_organization):
    def __init__(self, event_id):
        self.event_id = event_id
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')

        self.table_name = 'organizations'
        self.db = Mysql()

        self.adjust_tree()
        self.output_form_of_all_organizations()
        self.clicked_connect()
        self.dialog.exec()

    def clicked_connect(self):
        self.tree_organizations_list.itemDoubleClicked.connect(self.select_organization)
        self.tree_organizations_list.itemDoubleClicked.connect(self.dialog.close)
        self.pushButton_add.clicked.connect(self.select_organization)
        self.pushButton_add.clicked.connect(self.dialog.close)

    def adjust_tree(self):
        """Настройка отображения списка Организаций"""
        self.tree_organizations_list.header().setStretchLastSection(False)
        self.tree_organizations_list.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        columns_names = ['id', 'Наименование Организации', 'ИНН', 'КПП', 'Номер телефона']
        for column in columns_names:
            self.tree_organizations_list.headerItem().setText(columns_names.index(column), column)
        # self.tree_organizations_list.setColumnHidden(0, True)

    def output_form_of_all_organizations(self):
        """Отображение данных по Организациям"""
        # ['id', 'organization_name', 'organization_inn', 'organization_kpp', 'phone_number']
        all_organizations = self.db.select_all(self.table_name)
        self.tree_organizations_list.clear()
        organization_string = []
        number = 1
        for dct in all_organizations:
            organization_string.append(str(dct['id']))
            # organization_string.append(str(number))
            organization_string.append(dct['organization_name'])
            organization_string.append(dct['organization_inn'])
            organization_string.append(dct['organization_kpp'])
            organization_string.append(dct['phone_number'])
            item = QTreeWidgetItem(organization_string)
            self.tree_organizations_list.addTopLevelItem(item)
            organization_string.clear()
            number += 1

    def select_organization(self):
        try:
            self.organization = {}
            item = self.tree_organizations_list.currentItem()
            self.organization['id'] = item.text(0)
            self.organization = self.db.select_one(self.organization, 'organizations')
            global organization_dct
            organization_dct = self.organization

        except Exception as ex:\
            print("Не выделен ни один объект в дереве")


class Analisis_list(Ui_Analisis_docs):
    """Класс работы с окном Анализ загруженных документов"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def adjust_tree(self, tree):
        """Установка наименований для колонок Tree"""
        columns_names = ['Телефон', 'Фамилия', 'Имя', 'Отчество', 'Паспорт', 'Прописка', 'ИНН', 'СНИЛС', 'Диплом', 'Сертификат', 'Согласие', 'Анкета', 'Договор', 'Акт', 'Отчет']
        for name in columns_names:
            tree.headerItem().setText(columns_names.index(name), name)

    def clicked_connect(self):
        """Обработка нажатий кнопок"""
        pass
        # self.pushButton_add_participance.clicked.connect(List_participants)
        self.pushButton_open_analisis_doc.clicked.connect(Accept_docs)


class Accept_docs(Ui_Accept_docs):
    """Окно Принятия или отклонения документов"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def view_document(self):
        import webbrowser
        webbrowser.open("/home/vsesvet/Изображения/2_passport.jpg")
        #  для Windows os.startfile(r'/home/event/participants_data/2_Волкова_Ольга_Викторовна/2_passport.png')
        # os.startfile(r'D:\picture.jpg')

    def clicked_connect(self):
        """Обработка нажатий на кнопки в окне Принятия или отклонения документов"""
        # Кнопки основных действий
        self.pushButton_upload_docs.clicked.connect(Upload_docs)
        self.pushButton_open_passport.clicked.connect(self.view_document)
        # self.pushButton_Ok.clicked.connect(Accept_docs.close)
        # self.pushButton_Cancel.clicked.connect(Accept_docs.close)

        # # Кнопки открытия документов для просмотра
        # self.pushButton_open_agree.clicked.connect(Accept_docs.close)
        # self.pushButton_open_act.clicked.connect(Accept_docs.close)
        # self.pushButton_open_contract.clicked.connect(Accept_docs.close)
        # self.pushButton_open_diploma.clicked.connect(Accept_docs.close)
        # self.pushButton_open_inn.clicked.connect(Accept_docs.close)
        # self.pushButton_open_registration.clicked.connect(Accept_docs.close)
        # self.pushButton_open_report.clicked.connect(Accept_docs.close)
        # self.pushButton_open_sertificate.clicked.connect(Accept_docs.close)
        # self.pushButton_open_snils.clicked.connect(Accept_docs.close)
        # self.pushButton_open_survey.clicked.connect(Accept_docs.close)
        # Кнопки Принятия / Отклонения
        self.checkBox_reject_passport.clicked['bool'].connect(self.checkBox_accept_passport.setDisabled)
        self.checkBox_accept_passport.clicked['bool'].connect(self.checkBox_reject_passport.setDisabled)
        self.checkBox_accept_registration.clicked['bool'].connect(self.checkBox_reject_registration.setDisabled)
        self.checkBox_reject_registration.clicked['bool'].connect(self.checkBox_accept_registration.setDisabled)
        self.checkBox_accept_act.clicked['bool'].connect(self.checkBox_reject_act.setDisabled)
        self.checkBox_accept_sertificate.clicked['bool'].connect(self.checkBox_reject_sertificate.setDisabled)
        self.checkBox_accept_report.clicked['bool'].connect(self.checkBox_reject_report.setDisabled)
        self.checkBox_accept_inn.clicked['bool'].connect(self.checkBox_reject_inn.setDisabled)
        self.checkBox_accept_diploma.clicked['bool'].connect(self.checkBox_reject_diploma.setDisabled)
        self.checkBox_accept_contract.clicked['bool'].connect(self.checkBox_reject_contract.setDisabled)
        self.checkBox_accept_agree.clicked['bool'].connect(self.checkBox_reject_agree.setDisabled)
        self.checkBox_accept_survey.clicked['bool'].connect(self.checkBox_reject_survey.setDisabled)
        self.checkBox_accept_snils.clicked['bool'].connect(self.checkBox_reject_snils.setDisabled)
        self.checkBox_reject_act.clicked['bool'].connect(self.checkBox_accept_act.setDisabled)
        self.checkBox_reject_agree.clicked['bool'].connect(self.checkBox_accept_agree.setDisabled)
        self.checkBox_reject_contract.clicked['bool'].connect(self.checkBox_accept_contract.setDisabled)
        self.checkBox_reject_diploma.clicked['bool'].connect(self.checkBox_accept_diploma.setDisabled)
        self.checkBox_reject_inn.clicked['bool'].connect(self.checkBox_accept_inn.setDisabled)
        self.checkBox_reject_report.clicked['bool'].connect(self.checkBox_accept_report.setDisabled)
        self.checkBox_reject_sertificate.clicked['bool'].connect(self.checkBox_accept_sertificate.setDisabled)
        self.checkBox_reject_snils.clicked['bool'].connect(self.checkBox_accept_snils.setDisabled)
        self.checkBox_reject_survey.clicked['bool'].connect(self.checkBox_accept_survey.setDisabled)


class Create_Event(Ui_Create_event):
    """Работа с окном Создание Мероприятия"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.db = Mysql()
        self.label_username_login_role.setText(f'{username_login_role}')
        # self.table_name = 'events'
        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий на кнопки в окне Создание Мероприятия"""
        self.pushButton_select_organization.clicked.connect(Choose_organization)
        self.pushButton_select_organization.clicked.connect(self.set_organization)
        self.pushButton_ok.clicked.connect(self.get_event_data)
        self.pushButton_ok.clicked.connect(self.write_event_to_db)
        self.pushButton_ok.clicked.connect(self.relation_to_db)
        self.pushButton_ok.clicked.connect(self.event_templates_to_db)
        self.pushButton_ok.clicked.connect(dialog.close)

    def set_organization(self):
        """Установка организации в поле отображения Мероприятия"""
        global organization_dct
        self.lineEdit_selected_organization.setText(organization_dct['organization_name'])

    def get_event_data(self):
        """Считывание данных из полей Мероприятия, введенных пользователем"""
        self.dct_event = {}
        self.dct_event['event_name'] = self.lineEdit_event_name.text()
        self.dct_event['event_theme'] = self.lineEdit_event_theme.text()
        self.dct_event['date_time'] = self.event_dateTime.dateTime().toString("yyyy-MM-dd hh:mm")
        self.dct_event['country'] = self.lineEdit_event_country.text()
        self.dct_event['city'] = self.lineEdit_event_city.text()
        self.dct_event['type'] = self.lineEdit_type_event.text()
        self.dct_event['comment'] = self.lineEdit_event_comment.text()
        self.dct_event['status'] = 'Запланировано'
        self.dct_event['access'] = False
        self.dct_event['count'] = 0
        # print(f"Вывод данных введенной организации: {self.dct_event}")

    def write_event_to_db(self):
        print(self.dct_event)
        self.db.insert_row(self.dct_event, 'events')

    def relation_to_db(self):
        """Запись в таблицу organizations_events связки Мероприятие-Организация"""
        global organization_dct
        self.dct_event = self.db.select_one(self.dct_event, 'events')
        relation = {}
        relation['organization_id'] = organization_dct['id']
        relation['event_id'] = self.dct_event['id']
        print(f'Запись в таблицу organizations_events: {relation}')
        self.db.insert_row(relation, 'organizations_events')

    def event_templates_to_db(self):
        """Запись в event_templates именования шаблонов документов"""
        dct = {}
        dct['event_id'] = self.dct_event['id']
        id = self.dct_event['id']
        dct['path_template'] = f'/home/event/event_templates/{id}'
        dct['act_template'] = 'act_template'
        dct['agreement_template'] = 'agreement_template'
        dct['contract_template'] = 'contract_template'
        dct['survey_template'] = 'survey_template'
        self.db.insert_row(dct, 'event_templates')
        self.create_templates_directory(dct['path_template'])

    def create_templates_directory(self, path):
        """Создание директории для хранения шаблонов документов Мероприятия"""
        host, login, secret = ssh_config.host, ssh_config.login, ssh_config.secret
        templates_path = path
        event = paramiko.client.SSHClient()
        event.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        event.connect(host, username=login, password=secret)
        stdin, stdout, stderr = event.exec_command(f"mkdir -p {templates_path}")
        journal.log(f"Создана директория для хранения шаблонов документов Мероприятия {templates_path}")
        print(stdout.read().decode())
        stdin.close()
        event.close()


class Create_user(Ui_Create_user):
    """Окно создания Пользователя"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.table_name = 'users'
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий на кнопки в окне Создание Пользователя"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_ok.clicked.connect(self.read_field)
        self.pushButton_ok.clicked.connect(dialog.close)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def generate_password(self):
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')

    def read_field(self):
        new_user = {}
        new_user['phone_number'] = self.lineEdit_phone_number.text()
        new_user['second_name'] = self.lineEdit_second_name.text()
        new_user['first_name'] = self.lineEdit_first_name.text()
        new_user['last_name'] = self.lineEdit_last_name.text()
        new_user['full_name'] = f"{self.lineEdit_second_name.text()} {self.lineEdit_first_name.text()} {self.lineEdit_last_name.text()}"
        new_user['id'] = 2 # admin
        new_user['email'] = self.lineEdit_email.text()
        new_user['city'] = self.lineEdit_city.text()
        new_user['password'] = self.lineEdit_password.text()
        new_user['comment'] = self.lineEdit_comment.text()
        new_user['disabled'] = False
        self.write_user_to_db(new_user)

    def write_user_to_db(self, new_user):
        sql = Mysql()
        sql.create_user(new_user)


class Create_participant(Ui_Create_participant):
    """Класс создания нового участника"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.table_name = 'participants'

        # disabled after debug
        self.lineEdit_second_name.setText('Ефремов')
        self.lineEdit_first_name.setText('Максим')
        self.lineEdit_last_name.setText('Георгиевич')
        self.lineEdit_phone_number.setText('89889925875')

        self.checkBox_disabled_participant.setText("")
        self.clicked_connect(self.dialog)
        self.db = Mysql()
        self.dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна создание Участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.add_new_participant)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def add_new_participant(self):
        """Добавляет нового пользователя в базу данных"""
        """Считывание данных из Ui в {}"""
        dct = {}
        dct['phone_number'] = self.lineEdit_phone_number.text().strip()
        dct['phone_number'] = self.formating_phone(dct['phone_number'])
        dct['second_name'] = self.lineEdit_second_name.text().strip()
        dct['first_name'] = self.lineEdit_first_name.text().strip()
        dct['last_name'] = self.lineEdit_last_name.text().strip()
        dct['full_name'] = f"{dct['second_name']} {dct['first_name']} {dct['last_name']}"
        dct['role_id'] = '4'
        dct['email'] = self.lineEdit_email.text().strip()
        dct['city'] = self.lineEdit_city.text().strip()
        dct['password'] = self.lineEdit_password.text().strip()
        dct['comment'] = self.lineEdit_comment.text().strip()
        dct['disabled'] = self.checkBox_disabled_participant.isChecked()


        # Запись в БД
        try:
            self.db.insert_row(dct, self.table_name)
            self.dialog.close()
        except Exception as ex:
            print('Ошибка создания Участника')
            journal.log(f"Ошибка создания Участника: {dct['second_name']}")

        # Создание профиля участника
        dct = self.db.select_one(dct, self.table_name)
        self.create_profile(dct)
        self.create_profile_to_db(dct)
        journal.log(f"Создан участник {dct['id']}_{dct['second_name']} {dct['first_name']} {dct['last_name']}")

    def generate_password(self):
        """Генерация пароля по нажатию на кнопку"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')

    def formating_phone(self, phone_number):
        """Форматирование строки телефона"""
        phone_number = phone_number.replace('+7', '8').strip()
        if phone_number.isdigit():
            return phone_number
        else:
            symbols = ["-", "(", ")", " "]
            for symbol in symbols:
                if symbol in phone_number:
                    phone_number = phone_number.replace(symbol, '')
            if phone_number.isdigit():
                return phone_number
            else:
                return f'Не верный формат'

    def split_full_name(self, dct, full_name):
        """Разделение full_name и запись ФИО в second, first, last name"""
        if len(full_name) > 10:
            split = full_name.split()
            dct['second_name'] = split[0]
            dct['first_name'] = split[1]
            dct['last_name'] = split[2]
        return dct

    def create_profile(self, dct):
        """Создание профиля - директории для хранения файлов личных документов участника"""
        host, login, secret = ssh_config.host, ssh_config.login, ssh_config.secret
        profile_name = f"{dct['id']}_{dct['second_name']}_{dct['first_name']}_{dct['last_name']}"
        self.directory_path = f"/home/event/participants_data/{profile_name}"
        event = paramiko.client.SSHClient()
        event.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        event.connect(host, username=login, password=secret)
        stdin, stdout, stderr = event.exec_command(f"mkdir -p {self.directory_path}")
        journal.log(f"Создан профиль нового участника {self.directory_path}{profile_name}")
        print(stdout.read().decode())
        stdin.close()
        event.close()

    def create_profile_to_db(self, dct):
        """Создание записи в таблице: 'participants_data' о новом профиле"""
        table_name = "participants_data"
        dct1 = {}
        dct1['participant_id'] = dct['id']
        dct1['full_name'] = dct["full_name"]
        dct1['profile_path'] = self.directory_path
        dct1['passport'] = f"{dct['id']}_passport"
        dct1['registration'] = f"{dct['id']}_registration"
        dct1['inn'] = f"{dct['id']}_inn"
        dct1['snils'] = f"{dct['id']}_snils"
        dct1['diploma'] = f"{dct['id']}_diploma"
        dct1['sertificate'] = f"{dct['id']}_sertificate"
        dct1['passport_exist'] = False
        # dct1['passport_accept'] = NULL
        dct1['registration_exist'] = False
        # dct1['registration_accept'] = NULL
        dct1['inn_exist'] = False
        # dct1['inn_accept'] = NULL
        dct1['snils_exist'] = False
        # dct1['snils_accept'] = NULL
        dct1['diploma_exist'] = False
        # dct1['diploma_accept'] = NULL
        dct1['sertificate_exist'] = False
        # dct1['sertificate_accept'] = NULL

        self.db.insert_row(dct1, table_name)


class Edit_participant(Ui_Create_participant):
    """Окно редактирования Участника"""
    def __init__(self, participant):
        self.participant = participant
        self.table_name = 'participants'
        self.db = Mysql()
        username_login_role = access.get_username_and_role(user_login)
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        self.label_create_participant.setText("Редактирование участника")
        self.label_username_login_role.setText(f'{username_login_role}')
        self.output_form()
        self.clicked_connect(self.dialog)
        self.dialog.exec()

    def output_form(self):
        """Устанавливает в поля для ввода данные выбранного пользователя"""
        self.lineEdit_phone_number.setText(self.participant['phone_number'])
        self.lineEdit_second_name.setText(self.participant['second_name'])
        self.lineEdit_first_name.setText(self.participant['first_name'])
        self.lineEdit_last_name.setText(self.participant['last_name'])
        self.lineEdit_full_name.setText(self.participant['full_name'])
        self.lineEdit_email.setText(self.participant['email'])
        self.lineEdit_city.setText(self.participant['city'])
        self.lineEdit_password.setText(self.participant['password'])
        self.lineEdit_comment.setText(self.participant['comment'])

    def generate_password(self):
        """Генерация пароля в окне Редактирования Участника"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна Редактирование участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.update_participant)
        self.pushButton_cancel.clicked.connect(dialog.close)

    def formating_phone(self, phone_number):
        """Форматирование строки телефона"""
        phone_number = phone_number.replace('+7', '8').strip()
        if phone_number.isdigit():
            return phone_number
        else:
            symbols = ["-", "(", ")", " "]
            for symbol in symbols:
                if symbol in phone_number:
                    phone_number = phone_number.replace(symbol, '')
            if phone_number.isdigit():
                return phone_number
            else:
                return f'Не верный формат'

    def update_participant(self):
        """Считывает данные с полей и обновляет данные пользователя в базе данных"""
        # print(f"Данные участника до обновления: {self.participant}")
        dct = {}
        dct['id'] = self.participant['id']
        dct['phone_number'] = self.lineEdit_phone_number.text().strip()
        dct['phone_number'] = self.formating_phone(dct['phone_number'])
        dct['second_name'] = self.lineEdit_second_name.text().strip()
        dct['first_name'] = self.lineEdit_first_name.text().strip()
        dct['last_name'] = self.lineEdit_last_name.text().strip()
        dct['full_name'] = f"{dct['second_name']} {dct['first_name']} {dct['last_name']}"
        dct['email'] = self.lineEdit_email.text().strip()
        dct['city'] = self.lineEdit_city.text().strip()
        dct['password'] = self.lineEdit_password.text().strip()
        dct['comment'] = self.lineEdit_comment.text().strip()
        # dct['disabled'] = self.checkBox_disabled_participant.isChecked()

        # Update профильной папки
        self.update_profile(dct)
        # Update в таблице participants_data
        self.update_db_participants_data(dct)
        # Update участника в таблице participant
        self.update_db_participant(dct)

        self.dialog.close()
        journal.log(f"Обновлены данные участника в таблице 'participants': {dct['second_name']} {dct['first_name']}")

    def update_profile(self, dct):
        """Изменение профиля участника - директории для хранения файлов личных документов участника"""
        host, login, secret = ssh_config.host, ssh_config.login, ssh_config.secret
        old_profile_name = f"{self.participant['id']}_{self.participant['second_name']}_{self.participant['first_name']}_{self.participant['last_name']}"
        actual_profile_name = f"{dct['id']}_{dct['second_name']}_{dct['first_name']}_{dct['last_name']}"
        self.directory_path = f"/home/event/participants_data/"
        event = paramiko.client.SSHClient()
        event.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        event.connect(host, username=login, password=secret)
        print(f"mv {self.directory_path}{old_profile_name} {self.directory_path}{actual_profile_name}")
        stdin, stdout, stderr = event.exec_command(f"mv {self.directory_path}{old_profile_name} {self.directory_path}{actual_profile_name}")
        journal.log(f"Переименован профиль участника {self.directory_path}{actual_profile_name}")

        self.new_profile_path = f"{self.directory_path}{actual_profile_name}"

        print(stdout.read().decode())
        stdin.close()
        event.close()

    def update_db_participants_data(self, dct):
        """Обновление записи в таблице: 'participants_data' при изменении профиля"""
        table_name = "participants_data"
        dct_new = {}
        dct_new['participant_id'] = self.participant['id']
        # Забираем row по participant_id из таблицы participants_data
        dct_new = self.db.select_one(dct_new, table_name)
        # Обновляем данные в таблице participants_data
        dct_new['full_name'] = dct["full_name"]
        dct_new['profile_path'] = self.new_profile_path
        self.db.update_row(dct_new, table_name)
        journal.log(f"Данные в таблице {table_name} обновлены для '{dct_new['participant_id']} {dct_new['full_name']}'")

    def update_db_participant(self, dct):
        self.db.update_row(dct, 'participants')


class Create_organization(Ui_Create_organization):
    """Окно создания новой организации"""
    def __init__(self):
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.table_name = 'organizations'
        self.db = Mysql()
        self.clicked_connect()
        self.dialog.exec()


    def clicked_connect(self):
        """Обработка нажатий кнопок окна создание Участника"""
        self.pushButton_OK.clicked.connect(self.create_organization)
        self.pushButton_Cancel.clicked.connect(self.dialog.close)

    def create_organization(self):
        """Обработка нажатия кнопки создание новой организации"""
        self.new_org = {}
        self.new_org['organization_name'] = self.lineEdit_organization_name.text()
        self.new_org['organization_INN'] = self.lineEdit_organization_inn.text()
        self.new_org['organization_KPP'] = self.lineEdit_organization_kpp.text()
        self.new_org['phone_number'] = self.lineEdit_phone_number.text()

        self.insert_to_db()

    def insert_to_db(self):
        self.db.insert_row(self.new_org, self.table_name)
        self.dialog.close()


class Edit_organization(Ui_Create_organization):
    def __init__(self, organization):
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.table_name = 'organizations'
        self.organization = organization
        self.db = Mysql()
        self.output_form()
        self.clicked_connect()
        self.dialog.exec()


    def clicked_connect(self):
        """Обработка нажатий кнопок окна создание организации"""
        self.pushButton_OK.clicked.connect(self.edit_organization)
        self.pushButton_Cancel.clicked.connect(self.dialog.close)

    def edit_organization(self):
        """Обработка нажатия кнопки ОК = Принятие изменений"""
        new_org_data = {}
        new_org_data['id'] = self.organization['id']
        new_org_data['organization_name'] = self.lineEdit_organization_name.text()
        new_org_data['organization_INN'] = self.lineEdit_organization_inn.text()
        new_org_data['organization_KPP'] = self.lineEdit_organization_kpp.text()
        new_org_data['phone_number'] = self.lineEdit_phone_number.text()
        self.write_to_db(new_org_data)

    def write_to_db(self, new_org_data):
        self.db.update_row(new_org_data, self.table_name)
        self.dialog.close()

    def output_form(self):
        """Устанавливает в поля ввода данные выбранной Организации"""
        self.label_create_organization.setText('Редактирование организации')
        self.lineEdit_organization_name.setText(self.organization['organization_name'])
        self.lineEdit_organization_inn.setText(self.organization['organization_inn'])
        self.lineEdit_organization_kpp.setText(self.organization['organization_kpp'])
        self.lineEdit_phone_number.setText(self.organization['phone_number'])


class Create_inspector(Ui_Create_inspector):
    """Окно создания инспектора"""
    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def clicked_connect(self):
        """Обработка нажатий кнопок в окне Создание Инспектора"""
        self.pushButton_select_organization.clicked.connect(List_organization)
        self.pushButton_generate.clicked.connect(self.generate_password)

    def generate_password(self):
        """Обработка нажатий кнопок в окне Создание Инспектора"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')


class List_organization(Ui_List_organization):
    """Окно выводит список всех Организаций"""
    def __init__(self):
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.table_name = "organizations"
        self.db = Mysql()
        self.adjust_tree()
        all_organizations = self.get_from_db()
        self.output_form_of_all_organizations(all_organizations)
        self.clicked_connect(self.dialog)
        self.dialog.exec()

    def adjust_tree(self):
        """Установка наименований для колонок списка Организаций"""
        self.tree_organizations_list.header().setStretchLastSection(False)
        self.tree_organizations_list.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        columns_names = ['id', '№', 'Наименование Организации', 'ИНН', 'КПП', 'Номер телефона']
        for i in columns_names:
            self.tree_organizations_list.headerItem().setText(columns_names.index(i), i)
        self.tree_organizations_list.setColumnHidden(0, True)

    def get_from_db(self):
        all_organizations = self.db.select_all(self.table_name)
        return all_organizations

    def output_form_of_all_organizations(self, all_organizations):
        """Отображение данных по Организациям"""
        # ['id', '№', 'organization_name', 'organization_inn', 'organization_kpp', 'phone_number']
        self.tree_organizations_list.clear()
        organization_string = []
        number = 1
        for dct in all_organizations:
            organization_string.append(str(dct['id']))
            organization_string.append(str(number))
            organization_string.append(dct['organization_name'])
            organization_string.append(dct['organization_inn'])
            organization_string.append(dct['organization_kpp'])
            organization_string.append(dct['phone_number'])
            item = QTreeWidgetItem(organization_string)
            self.tree_organizations_list.addTopLevelItem(item)
            organization_string.clear()
            number += 1

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок в окне List_organization"""
        self.pushButton_add_organization.clicked.connect(Create_organization)
        self.pushButton_add_organization.clicked.connect(self.update_tree_organizations)
        self.pushButton_edit_organization.clicked.connect(self.edit_organization)
        self.pushButton_edit_organization.clicked.connect(self.update_tree_organizations)
        self.tree_organizations_list.itemDoubleClicked.connect(self.edit_organization)
        self.tree_organizations_list.itemDoubleClicked.connect(self.update_tree_organizations)
        self.pushButton_delete_organization.clicked.connect(self.delete_organization)
        self.pushButton_delete_organization.clicked.connect(self.update_tree_organizations)
        self.pushButton_OK.clicked.connect(self.dialog.close)
        self.pushButton_Cancel.clicked.connect(self.dialog.close)

    def edit_organization(self):
        """Получение id выбранной Организации. Открытие окна Редактирования организации"""
        try:
            item = self.tree_organizations_list.currentItem()
            organization_id = {}
            organization_id['id'] = item.text(0)
            organization = self.db.select_one(organization_id, 'organizations')
            Edit_organization(organization)
        except Exception as ex:
            print("Error")

    def delete_organization(self):
        """Удаление выделенной организации"""
        try:
            organization_id = {}
            item = self.tree_organizations_list.currentItem()
            organization_id['id'] = int(item.text(0))
            organization = self.db.select_one(organization_id, 'organizations')
            self.db.delete_row(organization_id, 'organizations')
            print(f"Удалена организация {organization}")
            journal.log(f"Удалена организация {organization}")
        except Exception as ex:
            "Error Delete organization"

    def update_tree_organizations(self):
        """Обновление общего списка Организаций"""
        db = Mysql()
        all_organizations = db.select_all(self.table_name)
        self.output_form_of_all_organizations(all_organizations)


class List_participants(Ui_List_participants):
    """Окно выводит список всех участников в БД, вне зависимости от мероприятий"""
    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        self.set_username_login_role()
        # Установка соеденения с БД
        self.db = Mysql()
        # Установка размеров под текст.
        self.tree_participants_list.header().setStretchLastSection(False)
        self.tree_participants_list.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Установка заголовков для колонок  treeWidget
        headers_names = ['id', '№', 'Телефон', 'Фамилия', 'Имя', 'Отчество', 'e-mail', 'Город', 'Пароль', 'Комментарий']

        self.set_headers(headers_names, self.tree_participants_list)
        # Инициализация функции вывода списка всех участников
        table_name = 'participants'
        participants = self.db.select_all(table_name)
        print(participants)
        self.output_form(participants)
        self.clicked_connect()
        dialog.exec()

    def set_username_login_role(self):
        """Показывает Имя и Роль пользователя запустившего программу"""
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')

    def clicked_connect(self):
        """Обработка нажатий кнопок в окне Список всех участников"""
        self.pushButton_create_participant.clicked.connect(Create_participant)
        self.pushButton_create_participant.clicked.connect(self.update_tree)
        self.pushButton_edit_participant.clicked.connect(self.edit_participant)
        self.pushButton_edit_participant.clicked.connect(self.update_tree)
        self.tree_participants_list.itemDoubleClicked.connect(self.edit_participant)
        self.tree_participants_list.itemDoubleClicked.connect(self.update_tree)
        self.pushButton_delete_participant.clicked.connect(self.delete_participant)
        self.pushButton_find.clicked.connect(self.find_participant)
        self.pushButton_reset_search.clicked.connect(self.reset_search)

    def edit_participant(self):
        """Открытие окна редактирования пользователя + получение данных по выбранному в QTreeWidget пользователю в виде списка"""
        try:
            dct = {}
            table_name = 'participants'
            item = self.tree_participants_list.currentItem()
            dct['id'] = item.text(0)
            participant = self.db.select_one(dct, table_name)
            Edit_participant(participant)
        except Exception as ex:\
            print("Не выделен ни один объект в дереве")

    def update_tree(self):
        """Обновление общего списка участников (Аналогично функции output_form, но с небольшими отличиями)"""
        self.tree_participants_list.clear()
        try:
            db = Mysql()
        except Exception as ex:
            print("Error update list participants")

        table_name = "participants"
        participants = db.select_all(table_name)
        self. output_form(participants)

    def set_headers(self, headers_names, tree):
        """Устанавливает заголовки колонок для Списка всех участников"""
        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)
        tree.setColumnHidden(0, True)

    def output_form(self, participants):
        """Отображение данных по всем участникам"""
        self.tree_participants_list.clear()
        participant_string = []
        number = 1
        # ( id, №__, phone_number, second_name, first_name, last_name, email, city, password, comment)
        for dct in participants:
            participant_string.append(str(dct['id']))
            participant_string.append(str(number))
            participant_string.append(dct['phone_number'])
            participant_string.append(dct['second_name'])
            participant_string.append(dct['first_name'])
            participant_string.append(dct['last_name'])
            participant_string.append(dct['email'])
            participant_string.append(dct['city'])
            participant_string.append(dct['password'])
            participant_string.append(dct['comment'])
            item = QTreeWidgetItem(participant_string)
            self.tree_participants_list.addTopLevelItem(item)
            participant_string.clear()
            number += 1
        # self.label_total_participants.setText(f"Всего в списке {len(participant_string)} участников")

    def find_participant(self):
        """Поиск участника по телефону или фамилии или email"""
        table_name = 'participants'
        phone = self.lineEdit_find_by_phone.text()
        second_name = self.lineEdit_find_by_second_name.text()
        email = self.lineEdit_find_by_email.text()
        dct = self.check_find_request(phone, second_name, email)
        if dct == {}:
            find_result = self.db.select_all(table_name)
        else:
            find_result = self.db.select_every(dct, table_name)
        self.output_form(find_result)
        print(find_result)

    def check_find_request(self, phone, second_name, email):
        """Проверка введенных пользователем данных для поиска"""
        dct = {}
        if len(phone) == 0:
            pass
        elif phone.isdigit():
            dct.setdefault('phone_number', phone)
        else:
            self.lineEdit_find_by_phone.setText('Не корректно')

        if len(second_name) == 0:
            pass
        elif second_name.isalpha():
            dct.setdefault('second_name', second_name)
        else:
            self.lineEdit_find_by_second_name.setText('Не корректно')

        if len(email) == 0:
            pass
        elif "@" in email:
            dct.setdefault('email', email)
        else:
            self.lineEdit_find_by_email.setText('Не корректно')
        return dct

    def reset_search(self):
        """Сброс полей поиска по участнику в общем списке участников и обновление списка"""
        self.lineEdit_find_by_phone.setText('')
        self.lineEdit_find_by_second_name.setText('')
        self.lineEdit_find_by_email.setText('')
        self.update_tree()

    def delete_participant(self):
        """Полное Удаление выделенного участника вместе с профильной папкой"""
        item = self.tree_participants_list.currentItem()
        dct_id = {} # id для таблицы participants
        dct_id['id'] = int(item.text(0))
        part_id = {} # id для таблицы participants_data
        part_id['participant_id'] = int(item.text(0))
        # Удаление профиля участника
        self.delete_profile_participant(part_id)
        # Удаление участника из таблицы participants
        self.db.delete_row(dct_id, 'participants')
        self.update_tree()

    def delete_profile_participant(self, part_id):
        """Удаление профиля участника с документами"""
        # Забираем данные о профильной папке из БД
        profile = self.db.select_one(part_id, "participants_data")
        directory_path = profile['profile_path']
        host, login, secret = ssh_config.host, ssh_config.login, ssh_config.secret
        event = paramiko.client.SSHClient()
        event.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        event.connect(host, username=login, password=secret)
        stdin, stdout, stderr = event.exec_command(f"rm -rf {directory_path}")
        journal.log(f"Удален профиль участника {part_id['participant_id']} {profile['full_name']}")
        print(stdout.read().decode())
        stdin.close()
        event.close()


class Upload_docs(Ui_Upload_docs):
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        docs = ['passport', 'registration', 'inn', 'snils', 'diploma', 'sertificate']
        self.dict_all_docs = dict.fromkeys(docs)
        self.path_file_passport = ''
        self.path_file_registration = ''
        self.path_file_inn = ''
        self.path_file_snils = ''
        self.path_file_diploma = ''
        self.path_file_sertificate = ''
        self.fname = None
        

        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок"""
        self.pushButton_upload_passport.clicked.connect(
            lambda: self.open_file(self.label_passport_upload, 'passport'))
        self.pushButton_upload_registration.clicked.connect(
            lambda: self.open_file( self.label_registration_upload, 'registration'))
        self.pushButton_upload_inn.clicked.connect(
            lambda: self.open_file(self.label_inn_upload, 'inn'))
        self.pushButton_upload_snils.clicked.connect(
            lambda: self.open_file( self.label_snils_upload, 'snils'))
        self.pushButton_upload_diploma.clicked.connect(
            lambda: self.open_file( self.label_diploma_upload, 'diploma'))
        self.pushButton_upload_sertificate.clicked.connect(
            lambda: self.open_file(self.label_sertificate_upload, 'sertificate'))

        self.pushButton_ok.clicked.connect(lambda: self.press_ok(dialog))

        # self.pushButton_upload_survey.clicked.connect(Upload_docs.show)
        # self.pushButton_upload_agree.clicked.connect(Upload_docs.show)
        # self.pushButton_upload_contract.clicked.connect(Upload_docs.show)
        # self.pushButton_upload_act.clicked.connect(Upload_docs.show)
        # self.pushButton_upload_report.clicked.connect(Upload_docs.show)


    def open_file(self, label, docs_name):
        """Функция выбора файла из окна проводника и присвоение словарю путей откуда будут копироваться файлы"""
        self.fname = QFileDialog.getOpenFileName(None, 'Выберите файл', '/home', "Files (*.pdf, *.jpg *.jpeg, *.png)")
        print(self.fname)
        if self.fname == ('', ''):
            label.setText('Не выбран файл')
        else:
            label.setText('Файл выбран')
        path_file_document = self.fname[0]
        print(f"Выбран путь к файлу {docs_name}: {path_file_document}")
        self.dict_all_docs[docs_name] = path_file_document

    def press_ok(self, dialog):
        """Копирование выбранных документов в профиль участника на сервере"""
        if self.fname == None:
            print('Не выбрано ни одного документа')
        else:
            print(f"Выбраные для загузки следующие документы: {self.dict_all_docs}")
            # вызов ssh.client и копирование файлов из self.path_file_documents в participants_data path/documents
            # Установка флага: Exist для переданного документа в True
            dialog.close()
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    journal = Journal()
    journal.start_log()
    user_login = {}
    Login()
    if user_login == None:
        sys.exit(f'Неверный логин или пароль')
    elif user_login == {}:
        journal.close_login()
        sys.exit(f'Окно Логин закрыто пользователем')
    journal.log(f"Пользователь {user_login['second_name']} {user_login['first_name']}, вошел в систему")
    processing = Processing()
    access = Access()
    user = User()
    organization_dct = {}
    organization_dct['organization_name'] = None
    Event_shedule()
    sys.exit(app.exec())
