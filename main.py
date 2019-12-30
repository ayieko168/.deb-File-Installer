from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from MainDesign import *
import datetime
import os, sys
import subprocess

OS = sys.platform

class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SETUP
        self.consoleLog("Welcome")
        self.ui.installButton.setEnabled(False)

        # CONNECTIONS
        self.ui.searchSourceButton.clicked.connect(self.searchSourceButtonCMD)
        self.ui.installButton.clicked.connect(self.installButtonCMD)
        self.ui.sourceEntry.textChanged.connect(lambda: self.ui.installButton.setEnabled(True))

        # VARIABLES
        self.debFile = ""

    def searchSourceButtonCMD(self):

        self.consoleLog("Search")
        debFilePath = QFileDialog.getOpenFileName(filter="deb Package (*.deb)")
        debFileName = debFilePath.split("/")[-1]

        if len(debFileName) > 1:
            self.consoleLog(debFilePath)
            self.ui.sourceEntry.setText(debFileName)
            self.ui.installButton.setEnabled(True)
            self.debFile = debFilePath

    def installButtonCMD(self):

        self.consoleLog("install")

        if len(self.debFile) > 1:

            pwd, rtn = QInputDialog.getText(self, "Root Password", "Enter Your Root Pass:",
                                            mode=QLineEdit.Password)

            if rtn == True:
                print(self.debFile)
                command1 = "echo {} | sudo -S apt -f install \"{}\"".format(pwd, self.debFile)
                p1 = subprocess.run(command1, shell=True)
                
                self.consoleLog("command = ", p1.args)
                self.consoleLog("stdout = ", p1.stdout)
                self.consoleLog("retnCodep1 = ", p1.returncode)
                
            
            else:
                self.consoleLog("Exited", "no ouy")


    def consoleLog(self, log, log2="", log3=""):
        self.ui.debugConsoleText.insertPlainText("[{}] >>>{}\n".format(self.curTime, log))
        if log2 != "":
            self.ui.debugConsoleText.insertPlainText("[{}] >>>{}\n".format(self.curTime, log2))
        if log3 != "":
            self.ui.debugConsoleText.insertPlainText("[{}] >>>{}\n".format(self.curTime, log3))

    @property
    def curTime(self):
        return datetime.datetime.now().strftime("%H:%M:%S")






















if __name__ == '__main__':

    w = QApplication([])
    app = App()
    app.show()
    w.exec_()







