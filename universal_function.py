# Универсальные функции main.py

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Ui_Create_participant import *

class Create_participant(Ui_Create_participant):
    """Собираем в словарь данные ввода"""
    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        self.checkBox_disabled_participant.setText("")

        # self.pushButton_save.clicked.connect(self.get_dict)
        # self.get_dict()
        self.view_participant()
        dialog.exec()

    def get_dict(self):
        """Считывание данных из Ui в {}"""
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
        dct['disabled'] = self.checkBox_disabled_participant.text().strip()
        dct['full_name'] = self.lineEdit_full_name.text().strip()
        self.lineEdit_second_name.setText(full_name[0])
        self.lineEdit_first_name.setText(full_name[1])
        self.lineEdit_last_name.setText(full_name[2])
        dct['second_name'] = full_name[0]
        dct['first_name'] = full_name[1]
        dct['last_name'] = full_name[2]
        print(dct)

    def view_participant(self):
        # Вывод данных словаря в Ui
        dct = {'phone_number': '89777194310', 'second_name': 'Ефремов', 'first_name': 'Максим',
               'last_name': 'Георгиевич', 'full_name': 'Ефремов Максим Георгиевич', 'email': 'efremov@mgido.com',
               'city': 'Москва', 'password': 'gnt6al47', 'comment': 'No comment', 'disabled': 'False'}
        self.lineEdit_phone_number.setText(dct['phone_number'])
        self.lineEdit_second_name.setText(dct['second_name'])
        self.lineEdit_first_name.setText(dct['first_name'])
        self.lineEdit_last_name.setText(dct['last_name'])
        self.lineEdit_full_name.setText(dct['full_name'])
        self.lineEdit_email.setText(dct['email'])
        self.lineEdit_city.setText(dct['city'])
        self.lineEdit_password.setText(dct['password'])
        self.lineEdit_comment.setText(dct['comment'])
        # self.checkBox_disabled_participant.stateChanged(False)
        # self.checkBox_disabled_participant.setInt(dct['disabled'])


app = QApplication(sys.argv)
create_participant = Create_participant()
sys.exit(app.exec())
