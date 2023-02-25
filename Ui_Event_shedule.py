# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Event_shedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Event_shedule(object):
    def setupUi(self, Event_shedule):
        Event_shedule.setObjectName("Event_shedule")
        Event_shedule.resize(1080, 620)
        self.centralwidget = QtWidgets.QWidget(Event_shedule)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_find_event = QtWidgets.QLabel(self.centralwidget)
        self.label_find_event.setObjectName("label_find_event")
        self.gridLayout_2.addWidget(self.label_find_event, 6, 0, 1, 2)
        self.tree_event_shedule = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_event_shedule.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_event_shedule.setObjectName("tree_event_shedule")
        self.tree_event_shedule.header().setDefaultSectionSize(130)
        self.tree_event_shedule.header().setHighlightSections(True)
        self.tree_event_shedule.header().setMinimumSectionSize(50)
        self.tree_event_shedule.header().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.tree_event_shedule, 4, 0, 1, 6)
        self.pushButton_create_participant = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_participant.setObjectName("pushButton_create_participant")
        self.gridLayout_2.addWidget(self.pushButton_create_participant, 3, 0, 1, 1)
        self.label_total_completed_events = QtWidgets.QLabel(self.centralwidget)
        self.label_total_completed_events.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_total_completed_events.setObjectName("label_total_completed_events")
        self.gridLayout_2.addWidget(self.label_total_completed_events, 5, 3, 1, 3)
        self.pushButton_open_event = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_event.setObjectName("pushButton_open_event")
        self.gridLayout_2.addWidget(self.pushButton_open_event, 3, 3, 1, 1)
        self.pushButton_create_inspector = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_inspector.setObjectName("pushButton_create_inspector")
        self.gridLayout_2.addWidget(self.pushButton_create_inspector, 3, 1, 1, 1)
        self.label_username_login_role = QtWidgets.QLabel(self.centralwidget)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout_2.addWidget(self.label_username_login_role, 0, 3, 1, 3)
        self.label_event_shedule = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_event_shedule.setFont(font)
        self.label_event_shedule.setAlignment(QtCore.Qt.AlignCenter)
        self.label_event_shedule.setObjectName("label_event_shedule")
        self.gridLayout_2.addWidget(self.label_event_shedule, 1, 0, 1, 6)
        self.pushButton_create_organization = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_organization.setObjectName("pushButton_create_organization")
        self.gridLayout_2.addWidget(self.pushButton_create_organization, 2, 1, 1, 1)
        self.pushButton_export_xls = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_xls.setObjectName("pushButton_export_xls")
        self.gridLayout_2.addWidget(self.pushButton_export_xls, 2, 3, 1, 1)
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setObjectName("pushButton_print")
        self.gridLayout_2.addWidget(self.pushButton_print, 2, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_status_event = QtWidgets.QLabel(self.centralwidget)
        self.label_status_event.setObjectName("label_status_event")
        self.gridLayout.addWidget(self.label_status_event, 0, 4, 1, 1)
        self.dateEdit_finish_event = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_finish_event.setDate(QtCore.QDate(2023, 12, 31))
        self.dateEdit_finish_event.setObjectName("dateEdit_finish_event")
        self.gridLayout.addWidget(self.dateEdit_finish_event, 1, 1, 1, 1)
        self.pushButton_select_organization = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select_organization.setObjectName("pushButton_select_organization")
        self.gridLayout.addWidget(self.pushButton_select_organization, 1, 3, 1, 1)
        self.comboBox_event_status = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_event_status.setObjectName("comboBox_event_status")
        self.comboBox_event_status.addItem("")
        self.comboBox_event_status.addItem("")
        self.comboBox_event_status.addItem("")
        self.comboBox_event_status.addItem("")
        self.gridLayout.addWidget(self.comboBox_event_status, 0, 5, 1, 1)
        self.lineEdit_organization = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_organization.setObjectName("lineEdit_organization")
        self.gridLayout.addWidget(self.lineEdit_organization, 0, 3, 1, 1)
        self.lineEdit_find_event = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_find_event.setObjectName("lineEdit_find_event")
        self.gridLayout.addWidget(self.lineEdit_find_event, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.dateEdit_begin_event = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_begin_event.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_begin_event.setObjectName("dateEdit_begin_event")
        self.gridLayout.addWidget(self.dateEdit_begin_event, 1, 0, 1, 1)
        self.pushButton_find_event = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find_event.setObjectName("pushButton_find_event")
        self.gridLayout.addWidget(self.pushButton_find_event, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 7, 0, 1, 6)
        self.pushButton_list_organization = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_list_organization.setObjectName("pushButton_list_organization")
        self.gridLayout_2.addWidget(self.pushButton_list_organization, 3, 4, 1, 1)
        self.pushButton_list_of_all_participants = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_list_of_all_participants.setObjectName("pushButton_list_of_all_participants")
        self.gridLayout_2.addWidget(self.pushButton_list_of_all_participants, 3, 5, 1, 1)
        self.pushButton_create_event = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_event.setObjectName("pushButton_create_event")
        self.gridLayout_2.addWidget(self.pushButton_create_event, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout_2.addWidget(self.pushButton_exit, 2, 5, 1, 1)
        Event_shedule.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Event_shedule)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menubar.setObjectName("menubar")
        Event_shedule.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Event_shedule)
        self.statusbar.setObjectName("statusbar")
        Event_shedule.setStatusBar(self.statusbar)

        self.retranslateUi(Event_shedule)
        self.pushButton_create_event.clicked.connect(Event_shedule.show) # type: ignore
        self.pushButton_create_participant.clicked.connect(Event_shedule.show) # type: ignore
        self.pushButton_create_organization.clicked.connect(Event_shedule.show) # type: ignore
        self.pushButton_create_inspector.clicked.connect(Event_shedule.show) # type: ignore
        self.pushButton_export_xls.clicked.connect(Event_shedule.showFullScreen) # type: ignore
        self.pushButton_print.clicked.connect(Event_shedule.show) # type: ignore
        self.pushButton_find_event.clicked.connect(self.tree_event_shedule.clear) # type: ignore
        self.comboBox_event_status.currentIndexChanged['QString'].connect(self.tree_event_shedule.expandAll) # type: ignore
        self.pushButton_open_event.clicked.connect(Event_shedule.show)
        self.pushButton_select_organization.clicked.connect(Event_shedule.show) # type: ignore
        self.pushButton_exit.clicked.connect(Event_shedule.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Event_shedule)
        Event_shedule.setTabOrder(self.pushButton_create_event, self.pushButton_create_participant)
        Event_shedule.setTabOrder(self.pushButton_create_participant, self.pushButton_create_organization)
        Event_shedule.setTabOrder(self.pushButton_create_organization, self.pushButton_create_inspector)
        Event_shedule.setTabOrder(self.pushButton_create_inspector, self.tree_event_shedule)
        Event_shedule.setTabOrder(self.tree_event_shedule, self.pushButton_export_xls)
        Event_shedule.setTabOrder(self.pushButton_export_xls, self.pushButton_print)
        Event_shedule.setTabOrder(self.pushButton_print, self.pushButton_exit)
        Event_shedule.setTabOrder(self.pushButton_exit, self.lineEdit_find_event)
        Event_shedule.setTabOrder(self.lineEdit_find_event, self.dateEdit_begin_event)
        Event_shedule.setTabOrder(self.dateEdit_begin_event, self.dateEdit_finish_event)
        Event_shedule.setTabOrder(self.dateEdit_finish_event, self.comboBox_event_status)

    def retranslateUi(self, Event_shedule):
        _translate = QtCore.QCoreApplication.translate
        Event_shedule.setWindowTitle(_translate("Event_shedule", "Логистик  (update 23.02)"))
        self.label_find_event.setText(_translate("Event_shedule", "Фильтры поиска мероприятия:"))
        self.tree_event_shedule.headerItem().setText(0, _translate("Event_shedule", "1"))
        self.tree_event_shedule.headerItem().setText(1, _translate("Event_shedule", "2"))
        self.tree_event_shedule.headerItem().setText(2, _translate("Event_shedule", "3"))
        self.tree_event_shedule.headerItem().setText(3, _translate("Event_shedule", "4"))
        self.tree_event_shedule.headerItem().setText(4, _translate("Event_shedule", "5"))
        self.tree_event_shedule.headerItem().setText(5, _translate("Event_shedule", "6"))
        self.tree_event_shedule.headerItem().setText(6, _translate("Event_shedule", "7"))
        self.tree_event_shedule.headerItem().setText(7, _translate("Event_shedule", "8"))
        self.pushButton_create_participant.setText(_translate("Event_shedule", "Создать участника"))
        self.label_total_completed_events.setText(_translate("Event_shedule", "Всего проведено ___ мероприятия"))
        self.pushButton_open_event.setText(_translate("Event_shedule", "Мероприятие"))
        self.pushButton_create_inspector.setText(_translate("Event_shedule", "Создать инспектора"))
        self.label_username_login_role.setText(_translate("Event_shedule", "username_login_role"))
        self.label_event_shedule.setText(_translate("Event_shedule", "Расписание мероприятий"))
        self.pushButton_create_organization.setText(_translate("Event_shedule", "Создать организацию"))
        self.pushButton_export_xls.setText(_translate("Event_shedule", "Export xls"))
        self.pushButton_print.setText(_translate("Event_shedule", "Печать"))
        self.label_status_event.setText(_translate("Event_shedule", "  Статус мероприятия"))
        self.pushButton_select_organization.setText(_translate("Event_shedule", "Выбрать"))
        self.comboBox_event_status.setItemText(0, _translate("Event_shedule", "Все"))
        self.comboBox_event_status.setItemText(1, _translate("Event_shedule", "Запланировано"))
        self.comboBox_event_status.setItemText(2, _translate("Event_shedule", "Проведено"))
        self.comboBox_event_status.setItemText(3, _translate("Event_shedule", "Отменено"))
        self.lineEdit_organization.setPlaceholderText(_translate("Event_shedule", "Организация..."))
        self.lineEdit_find_event.setPlaceholderText(_translate("Event_shedule", "Наименование мероприятия..."))
        self.pushButton_find_event.setText(_translate("Event_shedule", "Найти"))
        self.pushButton_list_organization.setText(_translate("Event_shedule", "Список организаций"))
        self.pushButton_list_of_all_participants.setText(_translate("Event_shedule", "Список всех участников"))
        self.pushButton_create_event.setText(_translate("Event_shedule", "Создать мероприятие"))
        self.pushButton_exit.setText(_translate("Event_shedule", "Выход"))
