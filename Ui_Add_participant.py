# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Add_participant.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_participant(object):
    def setupUi(self, Add_participant):
        Add_participant.setObjectName("Add_participant")
        Add_participant.resize(608, 376)
        self.gridLayout = QtWidgets.QGridLayout(Add_participant)
        self.gridLayout.setObjectName("gridLayout")
        self.label_username_login_role = QtWidgets.QLabel(Add_participant)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 3, 1, 2)
        self.lineEdit_find_by_second_name = QtWidgets.QLineEdit(Add_participant)
        self.lineEdit_find_by_second_name.setObjectName("lineEdit_find_by_second_name")
        self.gridLayout.addWidget(self.lineEdit_find_by_second_name, 2, 1, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(Add_participant)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 5, 3, 1, 1)
        self.pushButton_ok = QtWidgets.QPushButton(Add_participant)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout.addWidget(self.pushButton_ok, 5, 4, 1, 1)
        self.tree_add_participant_to_event = QtWidgets.QTreeWidget(Add_participant)
        self.tree_add_participant_to_event.setObjectName("tree_add_participant_to_event")
        self.tree_add_participant_to_event.header().setDefaultSectionSize(57)
        self.tree_add_participant_to_event.header().setMinimumSectionSize(20)
        self.tree_add_participant_to_event.header().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tree_add_participant_to_event, 4, 0, 1, 5)
        self.lineEdit_find_by_phone = QtWidgets.QLineEdit(Add_participant)
        self.lineEdit_find_by_phone.setObjectName("lineEdit_find_by_phone")
        self.gridLayout.addWidget(self.lineEdit_find_by_phone, 2, 0, 1, 1)
        self.label_add_participant_event = QtWidgets.QLabel(Add_participant)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_add_participant_event.setFont(font)
        self.label_add_participant_event.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_participant_event.setObjectName("label_add_participant_event")
        self.gridLayout.addWidget(self.label_add_participant_event, 1, 0, 1, 5)
        self.pushButton_add_selected_participant = QtWidgets.QPushButton(Add_participant)
        self.pushButton_add_selected_participant.setObjectName("pushButton_add_selected_participant")
        self.gridLayout.addWidget(self.pushButton_add_selected_participant, 5, 0, 1, 1)
        self.lineEdit_find_by_email = QtWidgets.QLineEdit(Add_participant)
        self.lineEdit_find_by_email.setObjectName("lineEdit_find_by_email")
        self.gridLayout.addWidget(self.lineEdit_find_by_email, 2, 2, 1, 1)
        self.pushButton_find = QtWidgets.QPushButton(Add_participant)
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout.addWidget(self.pushButton_find, 2, 3, 1, 1)
        self.label_participant_exist = QtWidgets.QLabel(Add_participant)
        self.label_participant_exist.setText("")
        self.label_participant_exist.setObjectName("label_participant_exist")
        self.gridLayout.addWidget(self.label_participant_exist, 5, 1, 1, 2)

        self.retranslateUi(Add_participant)
        self.pushButton_cancel.clicked.connect(Add_participant.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Add_participant)
        Add_participant.setTabOrder(self.lineEdit_find_by_phone, self.lineEdit_find_by_second_name)
        Add_participant.setTabOrder(self.lineEdit_find_by_second_name, self.pushButton_find)
        Add_participant.setTabOrder(self.pushButton_find, self.tree_add_participant_to_event)
        Add_participant.setTabOrder(self.tree_add_participant_to_event, self.pushButton_add_selected_participant)
        Add_participant.setTabOrder(self.pushButton_add_selected_participant, self.pushButton_ok)
        Add_participant.setTabOrder(self.pushButton_ok, self.pushButton_cancel)

    def retranslateUi(self, Add_participant):
        _translate = QtCore.QCoreApplication.translate
        Add_participant.setWindowTitle(_translate("Add_participant", "Event"))
        self.label_username_login_role.setText(_translate("Add_participant", "username_login_role"))
        self.lineEdit_find_by_second_name.setPlaceholderText(_translate("Add_participant", "Фамилия..."))
        self.pushButton_cancel.setText(_translate("Add_participant", "Отмена"))
        self.pushButton_ok.setText(_translate("Add_participant", "ОК"))
        self.tree_add_participant_to_event.headerItem().setText(0, _translate("Add_participant", "№"))
        self.tree_add_participant_to_event.headerItem().setText(1, _translate("Add_participant", "Телефон"))
        self.tree_add_participant_to_event.headerItem().setText(2, _translate("Add_participant", "Фамилия"))
        self.tree_add_participant_to_event.headerItem().setText(3, _translate("Add_participant", "Имя"))
        self.tree_add_participant_to_event.headerItem().setText(4, _translate("Add_participant", "Отчество"))
        self.tree_add_participant_to_event.headerItem().setText(5, _translate("Add_participant", "e-mail"))
        self.lineEdit_find_by_phone.setPlaceholderText(_translate("Add_participant", "Номер телефона..."))
        self.label_add_participant_event.setText(_translate("Add_participant", "Добавить участника в мероприятие"))
        self.pushButton_add_selected_participant.setText(_translate("Add_participant", "Добавить выбранного"))
        self.lineEdit_find_by_email.setPlaceholderText(_translate("Add_participant", "e-mail..."))
        self.pushButton_find.setText(_translate("Add_participant", "Найти"))
