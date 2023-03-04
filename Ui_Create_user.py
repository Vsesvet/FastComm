# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Create_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create_user(object):
    def setupUi(self, Create_user):
        Create_user.setObjectName("Create_user")
        Create_user.setWindowModality(QtCore.Qt.NonModal)
        Create_user.resize(500, 327)
        Create_user.setMinimumSize(QtCore.QSize(500, 300))
        Create_user.setMaximumSize(QtCore.QSize(1000, 500))
        self.gridLayout = QtWidgets.QGridLayout(Create_user)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_disabled_user = QtWidgets.QCheckBox(Create_user)
        self.checkBox_disabled_user.setChecked(True)
        self.checkBox_disabled_user.setObjectName("checkBox_disabled_user")
        self.gridLayout.addWidget(self.checkBox_disabled_user, 11, 0, 1, 2)
        self.lineEdit_phone_number = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.gridLayout.addWidget(self.lineEdit_phone_number, 4, 0, 1, 1)
        self.comboBox_select_role = QtWidgets.QComboBox(Create_user)
        self.comboBox_select_role.setObjectName("comboBox_select_role")
        self.comboBox_select_role.addItem("")
        self.comboBox_select_role.addItem("")
        self.comboBox_select_role.addItem("")
        self.comboBox_select_role.addItem("")
        self.gridLayout.addWidget(self.comboBox_select_role, 4, 1, 1, 2)
        self.lineEdit_second_name = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_second_name.setObjectName("lineEdit_second_name")
        self.gridLayout.addWidget(self.lineEdit_second_name, 5, 0, 1, 1)
        self.lineEdit_comment = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.gridLayout.addWidget(self.lineEdit_comment, 10, 0, 1, 5)
        self.pushButton_cancel = QtWidgets.QPushButton(Create_user)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 12, 3, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 8, 0, 1, 1)
        self.lineEdit_city = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 7, 1, 1, 2)
        self.lineEdit_full_name = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.gridLayout.addWidget(self.lineEdit_full_name, 6, 0, 1, 5)
        self.lineEdit_first_name = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.gridLayout.addWidget(self.lineEdit_first_name, 5, 1, 1, 2)
        self.label_username_login_role = QtWidgets.QLabel(Create_user)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 1, 1, 4)
        self.pushButton_generate = QtWidgets.QPushButton(Create_user)
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.gridLayout.addWidget(self.pushButton_generate, 8, 1, 1, 2)
        self.pushButton_ok = QtWidgets.QPushButton(Create_user)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout.addWidget(self.pushButton_ok, 12, 4, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 7, 0, 1, 1)
        self.label_create_new_user = QtWidgets.QLabel(Create_user)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_new_user.setFont(font)
        self.label_create_new_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_create_new_user.setObjectName("label_create_new_user")
        self.gridLayout.addWidget(self.label_create_new_user, 1, 0, 1, 5)
        self.lineEdit_last_name = QtWidgets.QLineEdit(Create_user)
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.gridLayout.addWidget(self.lineEdit_last_name, 5, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)

        self.retranslateUi(Create_user)
        self.pushButton_generate.clicked.connect(self.lineEdit_password.selectAll) # type: ignore
        self.pushButton_ok.clicked.connect(Create_user.show) # type: ignore
        self.pushButton_cancel.clicked.connect(Create_user.close) # type: ignore
        self.checkBox_disabled_user.stateChanged['int'].connect(Create_user.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Create_user)
        Create_user.setTabOrder(self.lineEdit_phone_number, self.comboBox_select_role)
        Create_user.setTabOrder(self.comboBox_select_role, self.lineEdit_second_name)
        Create_user.setTabOrder(self.lineEdit_second_name, self.lineEdit_first_name)
        Create_user.setTabOrder(self.lineEdit_first_name, self.lineEdit_last_name)
        Create_user.setTabOrder(self.lineEdit_last_name, self.lineEdit_full_name)
        Create_user.setTabOrder(self.lineEdit_full_name, self.lineEdit_email)
        Create_user.setTabOrder(self.lineEdit_email, self.lineEdit_city)
        Create_user.setTabOrder(self.lineEdit_city, self.lineEdit_password)
        Create_user.setTabOrder(self.lineEdit_password, self.pushButton_generate)
        Create_user.setTabOrder(self.pushButton_generate, self.lineEdit_comment)
        Create_user.setTabOrder(self.lineEdit_comment, self.checkBox_disabled_user)
        Create_user.setTabOrder(self.checkBox_disabled_user, self.pushButton_cancel)
        Create_user.setTabOrder(self.pushButton_cancel, self.pushButton_ok)

    def retranslateUi(self, Create_user):
        _translate = QtCore.QCoreApplication.translate
        Create_user.setWindowTitle(_translate("Create_user", "Event"))
        self.checkBox_disabled_user.setText(_translate("Create_user", "Отключить учетную запись"))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Create_user", "79265001020"))
        self.comboBox_select_role.setItemText(0, _translate("Create_user", "1_sysadmin"))
        self.comboBox_select_role.setItemText(1, _translate("Create_user", "2_admin"))
        self.comboBox_select_role.setItemText(2, _translate("Create_user", "3_inspector"))
        self.comboBox_select_role.setItemText(3, _translate("Create_user", "4_participant"))
        self.lineEdit_second_name.setPlaceholderText(_translate("Create_user", "Фамилия..."))
        self.lineEdit_comment.setPlaceholderText(_translate("Create_user", "Комментарий..."))
        self.pushButton_cancel.setText(_translate("Create_user", "Отмена"))
        self.lineEdit_password.setPlaceholderText(_translate("Create_user", "Пароль..."))
        self.lineEdit_city.setPlaceholderText(_translate("Create_user", "Город..."))
        self.lineEdit_full_name.setPlaceholderText(_translate("Create_user", "Полное имя..."))
        self.lineEdit_first_name.setPlaceholderText(_translate("Create_user", "Имя..."))
        self.label_username_login_role.setText(_translate("Create_user", "username_login_role"))
        self.pushButton_generate.setText(_translate("Create_user", "Сгенерировать"))
        self.pushButton_ok.setText(_translate("Create_user", "OK"))
        self.lineEdit_email.setPlaceholderText(_translate("Create_user", "e-mail..."))
        self.label_create_new_user.setText(_translate("Create_user", "Создание пользователя"))
        self.lineEdit_last_name.setPlaceholderText(_translate("Create_user", "Отчество..."))
