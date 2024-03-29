# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Create_inspector.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create_inspector(object):
    def setupUi(self, Create_inspector):
        Create_inspector.setObjectName("Create_inspector")
        Create_inspector.setWindowModality(QtCore.Qt.NonModal)
        Create_inspector.resize(500, 300)
        Create_inspector.setMinimumSize(QtCore.QSize(500, 300))
        Create_inspector.setMaximumSize(QtCore.QSize(500, 300))
        Create_inspector.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Create_inspector)
        self.gridLayout.setObjectName("gridLayout")
        self.label_create_inspector = QtWidgets.QLabel(Create_inspector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_inspector.setFont(font)
        self.label_create_inspector.setAlignment(QtCore.Qt.AlignCenter)
        self.label_create_inspector.setObjectName("label_create_inspector")
        self.gridLayout.addWidget(self.label_create_inspector, 1, 0, 1, 5)
        self.lineEdit_second_name = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_second_name.setObjectName("lineEdit_second_name")
        self.gridLayout.addWidget(self.lineEdit_second_name, 6, 0, 1, 1)
        self.lineEdit_organization_name = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_organization_name.setObjectName("lineEdit_organization_name")
        self.gridLayout.addWidget(self.lineEdit_organization_name, 4, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.pushButton_generate = QtWidgets.QPushButton(Create_inspector)
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.gridLayout.addWidget(self.pushButton_generate, 9, 1, 1, 2)
        self.lineEdit_email = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 8, 0, 1, 1)
        self.lineEdit_comment = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.gridLayout.addWidget(self.lineEdit_comment, 11, 0, 1, 5)
        self.checkBox_disabled_inspector = QtWidgets.QCheckBox(Create_inspector)
        self.checkBox_disabled_inspector.setObjectName("checkBox_disabled_inspector")
        self.gridLayout.addWidget(self.checkBox_disabled_inspector, 12, 0, 1, 2)
        self.pushButton_cancel = QtWidgets.QPushButton(Create_inspector)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 13, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.lineEdit_first_name = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.gridLayout.addWidget(self.lineEdit_first_name, 6, 1, 1, 2)
        self.pushButton_ok = QtWidgets.QPushButton(Create_inspector)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout.addWidget(self.pushButton_ok, 13, 4, 1, 1)
        self.lineEdit_city = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 8, 1, 1, 2)
        self.pushButton_select_organization = QtWidgets.QPushButton(Create_inspector)
        self.pushButton_select_organization.setObjectName("pushButton_select_organization")
        self.gridLayout.addWidget(self.pushButton_select_organization, 4, 1, 1, 2)
        self.lineEdit_last_name = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.gridLayout.addWidget(self.lineEdit_last_name, 6, 3, 1, 2)
        self.label_username_login_role = QtWidgets.QLabel(Create_inspector)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 0, 1, 5)
        self.lineEdit_phone_number = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.gridLayout.addWidget(self.lineEdit_phone_number, 4, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 9, 0, 1, 1)
        self.lineEdit_full_name = QtWidgets.QLineEdit(Create_inspector)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.gridLayout.addWidget(self.lineEdit_full_name, 7, 0, 1, 5)

        self.retranslateUi(Create_inspector)
        self.pushButton_generate.clicked.connect(Create_inspector.update) # type: ignore
        self.pushButton_select_organization.clicked.connect(Create_inspector.open) # type: ignore
        self.checkBox_disabled_inspector.stateChanged['int'].connect(Create_inspector.show) # type: ignore
        self.pushButton_cancel.clicked.connect(Create_inspector.close) # type: ignore
        self.pushButton_ok.clicked.connect(Create_inspector.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Create_inspector)
        Create_inspector.setTabOrder(self.lineEdit_phone_number, self.pushButton_select_organization)
        Create_inspector.setTabOrder(self.pushButton_select_organization, self.lineEdit_organization_name)
        Create_inspector.setTabOrder(self.lineEdit_organization_name, self.lineEdit_second_name)
        Create_inspector.setTabOrder(self.lineEdit_second_name, self.lineEdit_first_name)
        Create_inspector.setTabOrder(self.lineEdit_first_name, self.lineEdit_last_name)
        Create_inspector.setTabOrder(self.lineEdit_last_name, self.lineEdit_email)
        Create_inspector.setTabOrder(self.lineEdit_email, self.lineEdit_city)
        Create_inspector.setTabOrder(self.lineEdit_city, self.lineEdit_password)
        Create_inspector.setTabOrder(self.lineEdit_password, self.pushButton_generate)
        Create_inspector.setTabOrder(self.pushButton_generate, self.lineEdit_comment)
        Create_inspector.setTabOrder(self.lineEdit_comment, self.checkBox_disabled_inspector)

    def retranslateUi(self, Create_inspector):
        _translate = QtCore.QCoreApplication.translate
        Create_inspector.setWindowTitle(_translate("Create_inspector", "Fast Community"))
        self.label_create_inspector.setText(_translate("Create_inspector", "Создание нового инспектора"))
        self.lineEdit_second_name.setPlaceholderText(_translate("Create_inspector", "Фамилия..."))
        self.lineEdit_organization_name.setPlaceholderText(_translate("Create_inspector", "Организация..."))
        self.pushButton_generate.setText(_translate("Create_inspector", "Сгенерировать"))
        self.lineEdit_email.setPlaceholderText(_translate("Create_inspector", "e-mail..."))
        self.lineEdit_comment.setPlaceholderText(_translate("Create_inspector", "Комментарий..."))
        self.checkBox_disabled_inspector.setText(_translate("Create_inspector", "Отключить учетную запись"))
        self.pushButton_cancel.setText(_translate("Create_inspector", "Отмена"))
        self.lineEdit_first_name.setPlaceholderText(_translate("Create_inspector", "Имя..."))
        self.pushButton_ok.setText(_translate("Create_inspector", "OK"))
        self.lineEdit_city.setPlaceholderText(_translate("Create_inspector", "Город..."))
        self.pushButton_select_organization.setText(_translate("Create_inspector", "Выбор организации"))
        self.lineEdit_last_name.setPlaceholderText(_translate("Create_inspector", "Отчество..."))
        self.label_username_login_role.setText(_translate("Create_inspector", "username_login_role"))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Create_inspector", "89265001020"))
        self.lineEdit_password.setPlaceholderText(_translate("Create_inspector", "Пароль..."))
        self.lineEdit_full_name.setPlaceholderText(_translate("Create_inspector", "Полное ФИО ..."))
