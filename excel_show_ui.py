# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mutt/Documents/数据统计系统pyqt5/excel_show_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fil_show_treeview = QtWidgets.QTreeView(self.centralwidget)
        self.fil_show_treeview.setMinimumSize(QtCore.QSize(300, 0))
        self.fil_show_treeview.setMaximumSize(QtCore.QSize(305, 16777215))
        self.fil_show_treeview.setObjectName("fil_show_treeview")
        self.horizontalLayout_2.addWidget(self.fil_show_treeview)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_box = QtWidgets.QComboBox(self.centralwidget)
        self.search_box.setCurrentText("")
        self.search_box.setObjectName("search_box")
        self.horizontalLayout.addWidget(self.search_box)
        self.search_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_lineedit.setObjectName("search_lineedit")
        self.horizontalLayout.addWidget(self.search_lineedit)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.excel_show_tabelview = QtWidgets.QTableView(self.centralwidget)
        self.excel_show_tabelview.setMinimumSize(QtCore.QSize(700, 0))
        self.excel_show_tabelview.setObjectName("excel_show_tabelview")
        self.verticalLayout.addWidget(self.excel_show_tabelview)
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_lineedit.setPlaceholderText(_translate("MainWindow", "输入搜索条件"))
        self.search_btn.setText(_translate("MainWindow", "搜索"))
        self.info_label.setText(_translate("MainWindow", "info()"))

