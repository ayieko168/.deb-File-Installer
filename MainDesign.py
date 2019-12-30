# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/_.deb-File-Installer/MainDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 571, 231))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.debugTab = QtWidgets.QWidget()
        self.debugTab.setObjectName("debugTab")
        self.debugConsoleText = QtWidgets.QTextBrowser(self.debugTab)
        self.debugConsoleText.setGeometry(QtCore.QRect(0, 0, 565, 195))
        self.debugConsoleText.setFrameShape(QtWidgets.QFrame.Box)
        self.debugConsoleText.setLineWidth(3)
        self.debugConsoleText.setObjectName("debugConsoleText")
        self.tabWidget.addTab(self.debugTab, "")
        self.consoleTab = QtWidgets.QWidget()
        self.consoleTab.setObjectName("consoleTab")
        self.tabWidget.addTab(self.consoleTab, "")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 581, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchSourceButton = QtWidgets.QPushButton(self.widget)
        self.searchSourceButton.setMaximumSize(QtCore.QSize(31, 31))
        self.searchSourceButton.setObjectName("searchSourceButton")
        self.horizontalLayout.addWidget(self.searchSourceButton)
        self.sourceEntry = QtWidgets.QLineEdit(self.widget)
        self.sourceEntry.setObjectName("sourceEntry")
        self.horizontalLayout.addWidget(self.sourceEntry)
        self.installButton = QtWidgets.QPushButton(self.widget)
        self.installButton.setObjectName("installButton")
        self.horizontalLayout.addWidget(self.installButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "deb Package Installer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debugTab), _translate("MainWindow", "Debug Console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.consoleTab), _translate("MainWindow", "Console"))
        self.searchSourceButton.setText(_translate("MainWindow", "*"))
        self.installButton.setText(_translate("MainWindow", "Install"))
        self.menuOptions.setTitle(_translate("MainWindow", "options"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
