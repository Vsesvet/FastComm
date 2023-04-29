# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Create_participant.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create_participant(object):
    def setupUi(self, Create_participant):
        Create_participant.setObjectName("Create_participant")
        Create_participant.setWindowModality(QtCore.Qt.NonModal)
        Create_participant.resize(500, 325)
        Create_participant.setMinimumSize(QtCore.QSize(500, 325))
        Create_participant.setMaximumSize(QtCore.QSize(500, 325))
        self.gridLayout = QtWidgets.QGridLayout(Create_participant)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_last_name = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.gridLayout.addWidget(self.lineEdit_last_name, 6, 3, 1, 2)
        self.lineEdit_city = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 9, 1, 1, 2)
        self.checkBox_disabled_participant = QtWidgets.QCheckBox(Create_participant)
        self.checkBox_disabled_participant.setEnabled(True)
        self.checkBox_disabled_participant.setChecked(False)
        self.checkBox_disabled_participant.setObjectName("checkBox_disabled_participant")
        self.gridLayout.addWidget(self.checkBox_disabled_participant, 13, 0, 1, 2)
        self.lineEdit_first_name = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.gridLayout.addWidget(self.lineEdit_first_name, 6, 1, 1, 2)
        self.pushButton_generate = QtWidgets.QPushButton(Create_participant)
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.gridLayout.addWidget(self.pushButton_generate, 10, 1, 1, 2)
        self.lineEdit_email = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 9, 0, 1, 1)
        self.label_username_login_role = QtWidgets.QLabel(Create_participant)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 1, 1, 4)
        self.lineEdit_comment = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.gridLayout.addWidget(self.lineEdit_comment, 12, 0, 1, 5)
        self.lineEdit_second_name = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_second_name.setObjectName("lineEdit_second_name")
        self.gridLayout.addWidget(self.lineEdit_second_name, 6, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(Create_participant)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 14, 4, 1, 1)
        self.lineEdit_full_name = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_full_name.setReadOnly(True)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.gridLayout.addWidget(self.lineEdit_full_name, 8, 0, 1, 5)
        self.label_create_participant = QtWidgets.QLabel(Create_participant)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_participant.setFont(font)
        self.label_create_participant.setAlignment(QtCore.Qt.AlignCenter)
        self.label_create_participant.setObjectName("label_create_participant")
        self.gridLayout.addWidget(self.label_create_participant, 1, 0, 1, 5)
        self.lineEdit_phone_number = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.gridLayout.addWidget(self.lineEdit_phone_number, 4, 1, 1, 2)
        self.pushButton_cancel = QtWidgets.QPushButton(Create_participant)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 14, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 11, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(Create_participant)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 10, 0, 1, 1)
        self.pushButton_send_one_email = QtWidgets.QPushButton(Create_participant)
        self.pushButton_send_one_email.setObjectName("pushButton_send_one_email")
        self.gridLayout.addWidget(self.pushButton_send_one_email, 10, 3, 1, 2)

        self.retranslateUi(Create_participant)
        # self.pushButton_generate.clicked.connect(self.lineEdit_password.selectAll) # type: ignore
        # self.pushButton_save.clicked.connect(Create_participant.show) # type: ignore
        self.pushButton_cancel.clicked.connect(Create_participant.close) # type: ignore
        # self.checkBox_disabled_participant.stateChanged['int'].connect(Create_participant.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Create_participant)
        Create_participant.setTabOrder(self.lineEdit_second_name, self.lineEdit_first_name)
        Create_participant.setTabOrder(self.lineEdit_first_name, self.lineEdit_last_name)
        Create_participant.setTabOrder(self.lineEdit_last_name, self.lineEdit_email)
        Create_participant.setTabOrder(self.lineEdit_email, self.lineEdit_city)
        Create_participant.setTabOrder(self.lineEdit_city, self.lineEdit_password)
        Create_participant.setTabOrder(self.lineEdit_password, self.pushButton_generate)
        Create_participant.setTabOrder(self.pushButton_generate, self.lineEdit_comment)
        Create_participant.setTabOrder(self.lineEdit_comment, self.checkBox_disabled_participant)
        Create_participant.setTabOrder(self.checkBox_disabled_participant, self.pushButton_cancel)
        Create_participant.setTabOrder(self.pushButton_cancel, self.pushButton_save)
        Create_participant.setTabOrder(self.pushButton_save, self.lineEdit_phone_number)

    def retranslateUi(self, Create_participant):
        _translate = QtCore.QCoreApplication.translate
        Create_participant.setWindowTitle(_translate("Create_participant", "Event"))
        self.lineEdit_last_name.setPlaceholderText(_translate("Create_participant", "Отчество..."))
        self.lineEdit_city.setPlaceholderText(_translate("Create_participant", "Город..."))
        self.checkBox_disabled_participant.setText(_translate("Create_participant", "Отключить учетную запись"))
        self.lineEdit_first_name.setPlaceholderText(_translate("Create_participant", "Имя..."))
        self.pushButton_generate.setText(_translate("Create_participant", "Сгенерировать"))
        self.lineEdit_email.setPlaceholderText(_translate("Create_participant", "e-mail..."))
        self.label_username_login_role.setText(_translate("Create_participant", "username_login_role"))
        self.lineEdit_comment.setPlaceholderText(_translate("Create_participant", "Комментарий..."))
        self.lineEdit_second_name.setPlaceholderText(_translate("Create_participant", "Фамилия..."))
        self.pushButton_save.setText(_translate("Create_participant", "OK"))
        self.lineEdit_full_name.setPlaceholderText(_translate("Create_participant", "Полное ФИО..."))
        self.label_create_participant.setText(_translate("Create_participant", "Создание нового участника"))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Create_participant", "89265001020"))
        self.pushButton_cancel.setText(_translate("Create_participant", "Отмена"))
        self.lineEdit_password.setPlaceholderText(_translate("Create_participant", "Пароль..."))
        self.pushButton_send_one_email.setText(_translate("Create_participant", "Отправить  email"))
