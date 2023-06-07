
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_List_participants(object):
    def setupUi(self, List_participants):
        List_participants.setObjectName("List_participants")
        List_participants.resize(1150, 600)
        self.gridLayout_3 = QtWidgets.QGridLayout(List_participants)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tree_participants_list = QtWidgets.QTreeWidget(List_participants)
        self.tree_participants_list.setObjectName("tree_participants_list")
        self.tree_participants_list.headerItem().setText(0, "1")
        self.tree_participants_list.header().setDefaultSectionSize(130)
        self.tree_participants_list.header().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tree_participants_list, 6, 0, 1, 7)
        self.pushButton_delete_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_delete_participant.setObjectName("pushButton_delete_participant")
        self.gridLayout_3.addWidget(self.pushButton_delete_participant, 3, 2, 1, 1)
        self.pushButton_create_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_create_participant.setObjectName("pushButton_create_participant")
        self.gridLayout_3.addWidget(self.pushButton_create_participant, 3, 0, 1, 1)
        self.pushButton_export_xls = QtWidgets.QPushButton(List_participants)
        self.pushButton_export_xls.setObjectName("pushButton_export_xls")
        self.gridLayout_3.addWidget(self.pushButton_export_xls, 7, 3, 1, 1)
        self.pushButton_edit_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_edit_participant.setObjectName("pushButton_edit_participant")
        self.gridLayout_3.addWidget(self.pushButton_edit_participant, 3, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(List_participants)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_3.addWidget(self.pushButton_close, 8, 6, 1, 1)
        self.label_username_login_role = QtWidgets.QLabel(List_participants)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username_login_role.setFont(font)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout_3.addWidget(self.label_username_login_role, 0, 5, 1, 2)
        self.label_participants_list = QtWidgets.QLabel(List_participants)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_participants_list.setFont(font)
        self.label_participants_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_participants_list.setObjectName("label_participants_list")
        self.gridLayout_3.addWidget(self.label_participants_list, 0, 2, 1, 3)
        self.label_attention = QtWidgets.QLabel(List_participants)
        self.label_attention.setObjectName("label_attention")
        self.gridLayout_3.addWidget(self.label_attention, 3, 3, 1, 4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_find_by_phone = QtWidgets.QLineEdit(List_participants)
        self.lineEdit_find_by_phone.setObjectName("lineEdit_find_by_phone")
        self.gridLayout_2.addWidget(self.lineEdit_find_by_phone, 0, 0, 1, 1)
        self.lineEdit_find_by_second_name = QtWidgets.QLineEdit(List_participants)
        self.lineEdit_find_by_second_name.setObjectName("lineEdit_find_by_second_name")
        self.gridLayout_2.addWidget(self.lineEdit_find_by_second_name, 0, 2, 1, 1)
        self.lineEdit_find_by_email = QtWidgets.QLineEdit(List_participants)
        self.lineEdit_find_by_email.setObjectName("lineEdit_find_by_email")
        self.gridLayout_2.addWidget(self.lineEdit_find_by_email, 0, 4, 1, 1)
        self.label_or1 = QtWidgets.QLabel(List_participants)
        self.label_or1.setObjectName("label_or1")
        self.gridLayout_2.addWidget(self.label_or1, 0, 1, 1, 1)
        self.pushButton_find = QtWidgets.QPushButton(List_participants)
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout_2.addWidget(self.pushButton_find, 0, 5, 1, 1)
        self.label_or2 = QtWidgets.QLabel(List_participants)
        self.label_or2.setObjectName("label_or2")
        self.gridLayout_2.addWidget(self.label_or2, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 8, 0, 1, 3)
        self.pushButton_reset_search = QtWidgets.QPushButton(List_participants)
        self.pushButton_reset_search.setObjectName("pushButton_reset_search")
        self.gridLayout_3.addWidget(self.pushButton_reset_search, 7, 2, 1, 1)
        self.label_find_event = QtWidgets.QLabel(List_participants)
        self.label_find_event.setObjectName("label_find_event")
        self.gridLayout_3.addWidget(self.label_find_event, 7, 0, 1, 2)

        self.retranslateUi(List_participants)
        self.pushButton_create_participant.clicked.connect(List_participants.show) # type: ignore
        self.pushButton_delete_participant.clicked.connect(List_participants.show) # type: ignore
        self.pushButton_export_xls.clicked.connect(List_participants.showMaximized) # type: ignore
        self.pushButton_find.clicked.connect(self.tree_participants_list.expandAll) # type: ignore
        self.pushButton_edit_participant.clicked.connect(List_participants.show) # type: ignore
        self.pushButton_close.clicked.connect(List_participants.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(List_participants)
        List_participants.setTabOrder(self.pushButton_find, self.pushButton_create_participant)
        List_participants.setTabOrder(self.pushButton_create_participant, self.pushButton_edit_participant)
        List_participants.setTabOrder(self.pushButton_edit_participant, self.lineEdit_find_by_phone)
        List_participants.setTabOrder(self.lineEdit_find_by_phone, self.tree_participants_list)
        List_participants.setTabOrder(self.tree_participants_list, self.pushButton_export_xls)
        List_participants.setTabOrder(self.pushButton_export_xls, self.pushButton_close)
        List_participants.setTabOrder(self.pushButton_close, self.pushButton_delete_participant)

    def retranslateUi(self, List_participants):
        _translate = QtCore.QCoreApplication.translate
        List_participants.setWindowTitle(_translate("List_participants", "Fast Community"))
        self.pushButton_delete_participant.setText(_translate("List_participants", "Удалить участника"))
        self.pushButton_create_participant.setText(_translate("List_participants", "Создать участника"))
        self.pushButton_export_xls.setText(_translate("List_participants", "Export xls"))
        self.pushButton_edit_participant.setText(_translate("List_participants", "Редактировать участника"))
        self.pushButton_close.setText(_translate("List_participants", "Закрыть"))
        self.label_username_login_role.setText(_translate("List_participants", "username_login_role"))
        self.label_participants_list.setText(_translate("List_participants", "Общий список всех участников"))
        self.label_attention.setText(_translate("List_participants", "Внимание! Удаление участника повлечет удаление всех его документов из БД."))
        self.lineEdit_find_by_phone.setPlaceholderText(_translate("List_participants", "Номер телефона"))
        self.lineEdit_find_by_second_name.setPlaceholderText(_translate("List_participants", "Фамилия..."))
        self.lineEdit_find_by_email.setPlaceholderText(_translate("List_participants", "e-mail..."))
        self.label_or1.setText(_translate("List_participants", "или"))
        self.pushButton_find.setText(_translate("List_participants", "Найти"))
        self.label_or2.setText(_translate("List_participants", "или"))
        self.pushButton_reset_search.setText(_translate("List_participants", "Сброс фильтров поиска"))
        self.label_find_event.setText(_translate("List_participants", "Фильтры поиска участника:"))
