# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_List_organization.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_List_organization(object):
    def setupUi(self, List_organization):
        List_organization.setObjectName("List_organization")
        List_organization.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout(List_organization)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_edit_organization = QtWidgets.QPushButton(List_organization)
        self.pushButton_edit_organization.setObjectName("pushButton_edit_organization")
        self.gridLayout.addWidget(self.pushButton_edit_organization, 3, 1, 1, 1)
        self.pushButton_add_organization = QtWidgets.QPushButton(List_organization)
        self.pushButton_add_organization.setObjectName("pushButton_add_organization")
        self.gridLayout.addWidget(self.pushButton_add_organization, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.pushButton_delete_organization = QtWidgets.QPushButton(List_organization)
        self.pushButton_delete_organization.setObjectName("pushButton_delete_organization")
        self.gridLayout.addWidget(self.pushButton_delete_organization, 3, 2, 1, 1)
        self.tree_organizations_list = QtWidgets.QTreeWidget(List_organization)
        self.tree_organizations_list.setObjectName("tree_organizations_list")
        self.tree_organizations_list.headerItem().setText(0, "1")
        self.tree_organizations_list.header().setDefaultSectionSize(57)
        self.tree_organizations_list.header().setMinimumSectionSize(20)
        self.tree_organizations_list.header().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tree_organizations_list, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(List_organization)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 4)
        self.label_username_login_role = QtWidgets.QLabel(List_organization)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Cancel = QtWidgets.QPushButton(List_organization)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout.addWidget(self.pushButton_Cancel)
        self.pushButton_OK = QtWidgets.QPushButton(List_organization)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.horizontalLayout.addWidget(self.pushButton_OK)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 3, 2, 1)

        self.retranslateUi(List_organization)
        QtCore.QMetaObject.connectSlotsByName(List_organization)

    def retranslateUi(self, List_organization):
        _translate = QtCore.QCoreApplication.translate
        List_organization.setWindowTitle(_translate("List_organization", "Fast Community"))
        self.pushButton_edit_organization.setText(_translate("List_organization", "Редактировать"))
        self.pushButton_add_organization.setText(_translate("List_organization", "Добавить"))
        self.pushButton_delete_organization.setText(_translate("List_organization", "Удалить"))
        self.label.setText(_translate("List_organization", "Список организаций"))
        self.label_username_login_role.setText(_translate("List_organization", "username_login_role"))
        self.pushButton_Cancel.setText(_translate("List_organization", "Отмена"))
        self.pushButton_OK.setText(_translate("List_organization", "ОК"))
