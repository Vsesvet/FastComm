# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Choose_organization.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Choose_organization(object):
    def setupUi(self, Choose_organization):
        Choose_organization.setObjectName("Choose_organization")
        Choose_organization.setEnabled(True)
        Choose_organization.resize(618, 447)
        self.gridLayout = QtWidgets.QGridLayout(Choose_organization)
        self.gridLayout.setObjectName("gridLayout")
        self.label_username_login_role = QtWidgets.QLabel(Choose_organization)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 1, 1, 1)
        self.tree_organizations_list = QtWidgets.QTreeWidget(Choose_organization)
        self.tree_organizations_list.setObjectName("tree_organizations_list")
        self.tree_organizations_list.headerItem().setText(0, "1")
        self.tree_organizations_list.header().setDefaultSectionSize(170)
        self.tree_organizations_list.header().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tree_organizations_list, 2, 0, 1, 2)
        self.label_main = QtWidgets.QLabel(Choose_organization)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_main.setFont(font)
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.gridLayout.addWidget(self.label_main, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(291, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_cancel = QtWidgets.QPushButton(Choose_organization)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_add = QtWidgets.QPushButton(Choose_organization)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        self.retranslateUi(Choose_organization)
        self.pushButton_cancel.clicked.connect(Choose_organization.close) # type: ignore
        self.pushButton_add.clicked.connect(Choose_organization.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Choose_organization)

    def retranslateUi(self, Choose_organization):
        _translate = QtCore.QCoreApplication.translate
        Choose_organization.setWindowTitle(_translate("Choose_organization", "Dialog"))
        self.label_username_login_role.setText(_translate("Choose_organization", "username_login_role"))
        self.label_main.setText(_translate("Choose_organization", "Выбор организации"))
        self.pushButton_cancel.setText(_translate("Choose_organization", "Отмена"))
        self.pushButton_add.setText(_translate("Choose_organization", "OK"))
