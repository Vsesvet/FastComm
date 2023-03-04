from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
import pymysql
# import generate_password
from Class_User import *
from Class_Processing import *
from Ui_List_participants import *
from main import Create_participant


class List_participants(Ui_List_participants):
    """Список всех участников вне зависимости от мероприятий"""
    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        username_login_role = f"Тестовый пользователь (admin)"
        self.label_username_login_role.setText(f'{username_login_role}')

        # # Установка соеденения с БД
        # Убрать постоянную передачу данных host, port, user, password, db_name
        self.db = Mysql()

        # Установка заголовков для колонок  treeWidget
        headers_names = ['Телефон', 'Фамилия', 'Имя', 'Отчетство', 'Город', 'e-mail', 'Пароль', 'Комментарий']
        self.set_headers(headers_names, self.tree_participants_list)

        # Инициализация функции отображения всех участников
        # self.set_view_of_all_participants()

        self.connect()
        dialog.exec()

    def connect(self):
        self.pushButton_create_participant.clicked.connect(Create_participant)

    def set_headers(self, headers_names, tree):
        # tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)

    def set_view_of_all_participants(self):
        """Отображение данных по всем участникам"""
        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']
        table_name = "participants"
        all_participants = self.db.select_all(table_name)

        value = []

        for id in range(0, len(all_participants)):
            for key in keys:
                value.append(all_participants[id][key])
            item = QTreeWidgetItem(value)
            self.tree_participants_list.addTopLevelItem(item)
            value.clear()
    def delete_participant(self):
        """Удаление участника из списка"""
        try:
            phone_number = self.tree_participants_list.currentItem().text(0)
            print(phone_number)
            id = (self.db.get_participant_id(phone_number))[0]["participant_id"]
            self.db.delete_participant(id)
            self.tree_participants_list.clear()
            self.set_view_of_all_participants()
        except Exception as ex:
            print("cant do")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_login = {}
    journal = Journal()
    processing = Processing()
    access = Access()
    user = User()

    List_participants()
    sys.exit(app.exec())