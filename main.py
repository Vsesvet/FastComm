from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem, QHeaderView
import time
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
        user_login = Mysql().find_selected(login, table_name)
        journal.log(f"Пользователь: {user_login['second_name']} {user_login['first_name']} вошел в систему")


        # if user_login = None
        # Вход, если логин и пароль верные
        # if flag_access == 0:
        #     app.exit()
        #     return user_login
        # # Номер телефона не найден в БД.
        # elif flag_access == 1:
        #     self.label_user_not_found.setText("не найден")
        # # Не верный пароль
        # elif flag_access == 2:
        #     self.label_bad_password.setText("не верный")
        #     print(user_login['second_name'], user_login['first_name'], flag_access)


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
        self.adjust_tree(self.tree_event_shedule)
        self.move_to_centre(window)
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

    def close_app(self):
        """Выход из программы по Закрытию окна"""
        # разобраться, пока не работает
        journal.close_login()
        sys.exit(4)

    def adjust_tree(self, tree):
        """Установка наименований для колонок Tree"""
        columns_names = ['Мероприятие', 'Дата', 'Страна', 'Город', 'Участников', 'Организация', 'Статус']
        # tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        for i in columns_names:
            tree.headerItem().setText(columns_names.index(i), i)

    def clicked_connect(self, window):
        """Обращения к классам окон по клику мыши"""
        self.pushButton_exit.clicked.connect(self.close_shedule)
        self.pushButton_exit.clicked.connect(window.close)
        self.pushButton_create_event.clicked.connect(Create_Event)
        self.pushButton_create_participant.clicked.connect(Create_participant)
        self.pushButton_create_organization.clicked.connect(Create_organization)
        self.pushButton_create_inspector.clicked.connect(Create_inspector)
        self.pushButton_list_organization.clicked.connect(List_organization)
        self.pushButton_list_of_all_participants.clicked.connect(List_participants)
        self.pushButton_open_event.clicked.connect(Event)
        self.pushButton_export_xls.clicked.connect(window.showMaximized)
        self.pushButton_print.clicked.connect(Create_user)
        # self.pushButton_find_event.clicked.connect(self.tree_event_shedule.clear)
        # self.comboBox_event_status.currentIndexChanged['QString'].connect(self.tree_event_shedule.expandAll)

    def close_shedule(self):
        """Запись лога выхода, по нажатию на кнопку Выход"""
        journal.finish_log(f'{self.username_login_role}')


class Event(Ui_Event):
    """Работа с окном Мероприятие"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        # Установка ResizeToContents для treeWidget_list_participance
        self.tree_event_list_participants.header().setStretchLastSection(False)
        self.tree_event_list_participants.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.clicked_connect()
        dialog.exec()

    def clicked_connect(self):
        """Обработка нажатий кнопок"""
        self.pushButton_add_event_participance.clicked.connect(Add_participant)
        self.pushButton_analisis_doc.clicked.connect(Analisis_list)


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
        # tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
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
        # self.clicked_connect()
        dialog.exec()


class Add_participant(Ui_Add_participant):
    """Окно добавления участника в Мероприятие"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)

        self.label_username_login_role.setText(f'{username_login_role}')
        # self.clicked_connect()
        dialog.exec()


class Create_Event(Ui_Create_event):
    """Работа с окном Создание Мероприятия"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def clicked_connect(self):
        self.pushButton_select_organization.clicked.connect(List_organization)


class Create_user(Ui_Create_user):
    """Окно создания Пользователя"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
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
        new_user['role_id'] = 2 # admin
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
        self.lineEdit_full_name.setText(' Ефремов Максим Георгиевич ')
        self.lineEdit_phone_number.setText('89859925870')

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
        # # Форматирование номера телефона
        # phone_number = self.formating_phone(phone_number)
        # print(phone_number)
        # if len(phone_number) == 11:
        #     try:
        #         self.db.create_participant(phone_number, second_name, first_name, last_name, role, full_name, email, city,
        #                                 password, comment, disabled)
        #         self.dialog.close()
        #
        #     except Exception as ex:
        #         print("Error add new participant")
        # else:
        #     self.lineEdit_phone_number.setPlaceholderText("ВВЕДИТЕ НОМЕР ТЕЛЕФОНА")

        """Считывание данных из Ui в {}"""
        dct = {}
        dct['phone_number'] = self.lineEdit_phone_number.text().strip().replace(' ', '')
        dct['second_name'] = self.lineEdit_second_name.text().strip()
        dct['first_name'] = self.lineEdit_first_name.text().strip()
        dct['last_name'] = self.lineEdit_last_name.text().strip()
        dct['full_name'] = self.lineEdit_full_name.text().strip()
        dct['role_id'] = '4'
        dct['email'] = self.lineEdit_email.text().strip()
        dct['city'] = self.lineEdit_city.text().strip()
        dct['password'] = self.lineEdit_password.text().strip()
        dct['comment'] = self.lineEdit_comment.text().strip()
        dct['disabled'] = self.checkBox_disabled_participant.isChecked()
        self.split_full_name(dct, dct['full_name'])
        self.create_profile(dct)

        # Запись в БД
        try:
            self.db.insert_row_to_table(dct, self.table_name)
            self.dialog.close()
        except Exception as ex:
            print('Ошибка создания Участника')
            journal.log(f"Ошибка создания Участника: {dct['second_name']}")

        # Функция создания профиля участника
        self.create_profile(dct)

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
        if len(full_name) > 12:
            split = full_name.split()
            dct['second_name'] = split[0]
            dct['first_name'] = split[1]
            dct['last_name'] = split[2]

        # self.lineEdit_second_name.setText(split_full[0])
        # self.lineEdit_first_name.setText(split_full[1])
        # self.lineEdit_last_name.setText()

    def create_profile(self, dct):
        """Создание профиля - директории для хранения файлов личных документов участника"""
        host, login, secret = ssh_config.host, ssh_config.login, ssh_config.secret
        profile_name = f"{dct['second_name']}_{dct['first_name']}_{dct['last_name']}_{dct['phone_number']}"
        directory_path = f"/home/event/participants_data/{profile_name}"

        event = paramiko.client.SSHClient()
        event.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        event.connect(host, username=login, password=secret)
        stdin, stdout, stderr = event.exec_command(f"mkdir -p {directory_path}")
        print(stdout.read().decode())
        stdin.close()
        event.close()


class Edit_participant(Ui_Create_participant):
    """Окно редактирования Участника"""

    def __init__(self, participant_id):
        self.db = Mysql()
        self.table_name = 'participants'
        dct = {}
        dct['participant_id'] = participant_id
        self.participant = self.db.find_selected(dct, self.table_name)
        print(dct)
        username_login_role = access.get_username_and_role(user_login)
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        self.label_create_participant.setText("Редактирование участника")
        self.label_username_login_role.setText(f'{username_login_role}')

        self.set_view()

        self.clicked_connect(self.dialog)
        self.dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна Редактирование участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.update_participant)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def update_participant(self):
        """Считывает данные с полей и обновляет данные пользователя в базе данных"""
        dct = {}
        dct['phone_number'] = self.lineEdit_phone_number.text().strip().replace(' ', '')
        dct['second_name'] = self.lineEdit_second_name.text().strip()
        dct['first_name'] = self.lineEdit_first_name.text().strip()
        dct['last_name'] = self.lineEdit_last_name.text().strip()
        dct['full_name'] = self.lineEdit_full_name.text().strip()
        dct['email'] = self.lineEdit_email.text().strip()
        dct['city'] = self.lineEdit_city.text().strip()
        dct['password'] = self.lineEdit_password.text().strip()
        dct['comment'] = self.lineEdit_comment.text().strip()
        # dct['disabled'] = self.checkBox_disabled_participant.isChecked()

        # Update-запись в БД.
        self.db.update_row_by_id(self.participant['participant_id'], dct, self.table_name)
        self.dialog.close()
        journal.log(f"Обновлены данные участника: {dct['second_name']} {dct['first_name']}")

    def set_view(self):
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


class Create_organization(Ui_Create_organization):
    """Окно создания новой организации"""
    def __init__(self):
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.db = Mysql()
        self.clicked_connect(self.dialog)
        self.dialog.exec()


    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна создание Участника"""
        self.pushButton_OK.clicked.connect(self.create_organization)
        self.pushButton_Cancel.clicked.connect(dialog.close)

    def create_organization(self):
        """Обработка нажатия кнопки создание новой организации"""

        new_org = {}

        new_org['organization_name'] = self.lineEdit_organization_name.text()
        new_org['organization_INN'] = self.lineEdit_organization_inn.text()
        new_org['organization_KPP'] = self.lineEdit_organization_kpp.text()
        new_org['phone_number'] = self.lineEdit_phone_number.text()

        self.write_organization_to_db(new_org)

    def write_organization_to_db(self, new_org):
        self.db.create_organization(new_org)
        self.dialog.close()


class Edit_organization(Ui_Create_organization):
    def __init__(self, id_from_db, current_values):
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.id_from_db = id_from_db
        self.current_values = current_values
        self.db = Mysql()
        self.set_view()
        self.clicked_connect(self.dialog)
        self.dialog.exec()



    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна создание организации"""
        self.pushButton_OK.clicked.connect(self.create_organization)
        self.pushButton_Cancel.clicked.connect(self.dialog.close)

    def create_organization(self):
        """Обработка нажатия кнопки ОК (Подтверждение обновлений)"""
        new_org_data = {}
        new_org_data['organization_name'] = self.lineEdit_organization_name.text()
        new_org_data['organization_INN'] = self.lineEdit_organization_inn.text()
        new_org_data['organization_KPP'] = self.lineEdit_organization_kpp.text()
        new_org_data['phone_number'] = self.lineEdit_phone_number.text()

        self.update_organization(new_org_data)

    def update_organization(self, new_org_data):
        table_name = "organizations"
        self.db.update_row_by_id(self.id_from_db, new_org_data, table_name)

        self.dialog.close()

        # keys = list(new_org_data.keys())
        # values = list(new_org_data.values())
        # check = {f"organization_id": self.id_from_db}
        # table_name = "organizations"
        #
        # for i in range(0, len(keys)):
        #     try:
        #         value = {f"{keys[i]}": values[i]}
        #         print(value, check)
        #         self.db.update_row_by_arg(value, check, table_name)
        #     except Exception as ex:
        #         "Error"
        #self.dialog.close()



    def set_view(self):
        """Устанавливает в поля для ввода данные выбранной организации"""
        self.lineEdit_organization_name.setText(self.current_values[0])
        self.lineEdit_organization_inn.setText(self.current_values[1])
        self.lineEdit_organization_kpp.setText(self.current_values[2])
        self.lineEdit_phone_number.setText(self.current_values[3])

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
        self.tree_organizations_list.header().setStretchLastSection(False)
        self.tree_organizations_list.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.db = Mysql()
        headers_names = ['Наименование Организации', 'ИНН', 'КПП', 'Номер телефона']
        self.set_headers(headers_names, self.tree_organizations_list)
        self.set_view_of_all_organizations()
        self.clicked_connect(self.dialog)
        self.dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок в окне List_organization"""
        self.pushButton_add_organization.clicked.connect(Create_organization)
        self.pushButton_add_organization.clicked.connect(self.update_tree)
        self.pushButton_edit_organization.clicked.connect(self.update_organization)
        self.pushButton_edit_organization.clicked.connect(self.update_tree)
        self.tree_organizations_list.itemDoubleClicked.connect(self.update_organization)
        self.tree_organizations_list.itemDoubleClicked.connect(self.update_tree)
        self.pushButton_delete_organization.clicked.connect(self.delete_organization)
        self.pushButton_OK.clicked.connect(self.dialog.close)
        self.pushButton_Cancel.clicked.connect(self.dialog.close)

    def update_organization(self):
        """Открытие окна редактирования организации + получение данных по выбранной в QTreeWidget организации в виде списка"""
        try:
            item = self.tree_organizations_list.currentItem()
            result_data = []
            for i in range(0, 4):
                item_string = item.text(i)
                print(item_string)
                result_data.append(item_string)

            value_request = "organization_id"
            arg = {'phone_number': result_data[3]}
            table_name = "organizations"
            id_from_db = self.db.get_value_by_arg(value_request, arg, table_name)
            #id_from_db = self.db.get_participant_id(result_data[0])

            Edit_organization(id_from_db, result_data)

        except Exception as ex:
            print("Error")

    def delete_organization(self):
        """Удаление выделенной организации"""
        try:
            item = self.tree_organizations_list.currentItem()
            phone_number = item.text(3)

            value_request = "organization_id"
            arg = {'phone_number': phone_number}
            table_name = "organizations"

            id = self.db.get_value_by_arg(value_request, arg, table_name)

            # arg = {'organization_id': id}

            # self.db.delete_row_by_arg(arg, table_name)
            self.db.delete_row_by_arg(id, table_name)
            self.update_tree()
        except Exception as ex:
            "Error"

    def set_headers(self, headers_names, tree):
        """Установка заголовков таблицы Списка Организаций"""
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)

    def update_tree(self):
        """Обновление общего списка участников (Аналогично функции set_view_of_all_participants, но с небольшими отличиями)"""
        self.tree_organizations_list.clear()
        try:
            db = Mysql()
        except Exception as ex:
            print("Error update list participants")

        keys = ['organization_name', 'organization_INN', 'organization_KPP', 'phone_number']
        table_name = "organizations"
        all_organizations = db.select_all_data(table_name)

        value = []
        for id in range(0, len(all_organizations)):
            for key in keys:
                value.append(all_organizations[id][key])
            item = QTreeWidgetItem(value)
            self.tree_organizations_list.addTopLevelItem(item)
            value.clear()

    def set_view_of_all_organizations(self):
        keys = ['organization_name', 'organization_INN', 'organization_KPP', 'phone_number']
        table_name = "organizations"
        print(table_name)
        all_organizations = self.db.select_all_data(table_name)
        print(all_organizations)
        value = []
        for id in range(0, len(all_organizations)):
            for key in keys:
                value.append(all_organizations[id][key])
            item = QTreeWidgetItem(value)
            self.tree_organizations_list.addTopLevelItem(item)
            value.clear()
    def set_headers(self, headers_names, tree):
        """Устанавливает заголовки колонок для Списка всех организаций"""
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
           tree.headerItem().setText(headers_names.index(header), header)


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
        headers_names = ['Телефон', 'Фамилия', 'Имя', 'Отчество', 'e-mail', 'Город', 'Пароль', 'Комментарий']
        self.set_headers(headers_names, self.tree_participants_list)
        # Инициализация функции вывода списка всех участников
        table_name = 'participants'
        all_participants = self.db.select_all_data(table_name)
        self.set_view_of_all_participants(all_participants)
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
        self.tree_participants_list.itemDoubleClicked.connect(self.edit_participant)
        self.tree_participants_list.itemDoubleClicked.connect(self.update_tree)
        self.pushButton_edit_participant.clicked.connect(self.update_tree)
        self.pushButton_delete_participant.clicked.connect(self.delete_participant)
        self.pushButton_find.clicked.connect(self.find_participant)
        self.pushButton_reset_search.clicked.connect(self.reset_search)


    def edit_participant(self):
        """Открытие окна редактирования пользователя + получение данных по выбранному в QTreeWidget пользователю в виде списка"""
        try:
            dct = {}
            table_name = 'participants'
            item = self.tree_participants_list.currentItem()
            dct['phone_number'] = item.text(0)
            participant = self.db.find_selected(dct, table_name)
            Edit_participant(participant['participant_id'])
        except Exception as ex:\
            print("Не выделен ни один объект в дереве")

    def delete_participant(self):
        """Удаление выделенного участника"""
        item = self.tree_participants_list.currentItem()
        phone_number = item.text(0)

        value_request = "participant_id"
        arg = {'phone_number': phone_number}
        table_name = "participants"
        id = self.db.get_value_by_arg(value_request, arg, table_name)
        arg = {'participant_id': id}
        self.db.delete_row_by_arg(arg, table_name)
        self.update_tree()
        self.delete_profile_participants(phone_number)

    def update_tree(self):
        """Обновление общего списка участников (Аналогично функции set_view_of_all_participants, но с небольшими отличиями)"""
        self.tree_participants_list.clear()
        try:
            db = Mysql()
        except Exception as ex:
            print("Error update list participants")

        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']
        table_name = "participants"
        all_participants = db.select_all_data(table_name)

        value = []
        for id in range(0, len(all_participants)):
            for key in keys:
                value.append(all_participants[id][key])
            item = QTreeWidgetItem(value)
            self.tree_participants_list.addTopLevelItem(item)
            value.clear()

    def set_headers(self, headers_names, tree):
        """Устанавливает заголовки колонок для Списка всех участников"""
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)

    def set_view_of_all_participants(self, all_participants):
        """Отображение данных по всем участникам"""
        print("set_view отработала")
        self.tree_participants_list.clear()
        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']

        value = []
        for id in range(0, len(all_participants)):
            for key in keys:
                value.append(all_participants[id][key])
            item = QTreeWidgetItem(value)
            self.tree_participants_list.addTopLevelItem(item)
            value.clear()

    def find_participant(self):
        """Поиск участника по телефону или фамилии или email"""
        table_name = 'participants'
        phone = self.lineEdit_find_by_phone.text()
        second_name = self.lineEdit_find_by_second_name.text()
        email = self.lineEdit_find_by_email.text()
        dct = self.check_find_request(phone, second_name, email)
        print(dct)
        if dct == {}:
            return
        find_result = self.db.find_several(dct, table_name)
        self.set_view_of_all_participants(find_result)
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

    def delete_profile_participant(self, phone_number):
        """Полное Удаление профиля участника вместе с документами"""
        
        pass

class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.make_pair(self.x,self.y)
    def make_pair(self, x, y):
        return lambda n: x if n == 0 else y

    def first(self, p):
        return p(0)

    def second(self,p):
        return p(1)

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
    Event_shedule()
    sys.exit(app.exec())
