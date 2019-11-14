# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/ayieko/684a8749-710f-4d95-9b24-aeacc1654b31/home/ayieko/Projects And  Research/PycharmProjects/_.deb-File-Installer/MainDesign.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 400)
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 571, 231))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.debugTab = QtGui.QWidget()
        self.debugTab.setObjectName(_fromUtf8("debugTab"))
        self.debugConsoleText = QtGui.QTextBrowser(self.debugTab)
        self.debugConsoleText.setGeometry(QtCore.QRect(0, 0, 565, 195))
        self.debugConsoleText.setFrameShape(QtGui.QFrame.Box)
        self.debugConsoleText.setLineWidth(3)
        self.debugConsoleText.setObjectName(_fromUtf8("debugConsoleText"))
        self.tabWidget.addTab(self.debugTab, _fromUtf8(""))
        self.consoleTab = QtGui.QWidget()
        self.consoleTab.setObjectName(_fromUtf8("consoleTab"))
        self.tabWidget.addTab(self.consoleTab, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 581, 33))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchSourceButton = QtGui.QPushButton(self.widget)
        self.searchSourceButton.setMaximumSize(QtCore.QSize(31, 31))
        self.searchSourceButton.setObjectName(_fromUtf8("searchSourceButton"))
        self.horizontalLayout.addWidget(self.searchSourceButton)
        self.sourceEntry = QtGui.QLineEdit(self.widget)
        self.sourceEntry.setObjectName(_fromUtf8("sourceEntry"))
        self.horizontalLayout.addWidget(self.sourceEntry)
        self.installButton = QtGui.QPushButton(self.widget)
        self.installButton.setObjectName(_fromUtf8("installButton"))
        self.horizontalLayout.addWidget(self.installButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "deb Package Installer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debugTab), _translate("MainWindow", "Debug Console", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.consoleTab), _translate("MainWindow", "Console", None))
        self.searchSourceButton.setText(_translate("MainWindow", "*", None))
        self.installButton.setText(_translate("MainWindow", "Install", None))
        self.menuOptions.setTitle(_translate("MainWindow", "options", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

