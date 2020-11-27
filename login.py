from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from Main import Ui_MainWindow
from ErrorWindow import Ui_errorWindow
import globals

class Ui_loginWindow(object):
    def login(self):
        globals.hostname = self.host.text()
        globals.username = self.user.text()
        globals.passwordT = self.password.text()
        globals.databaseT = self.database.text()
        #print("Raw Output: Host: "+ globals.hostname +", User: " + globals.username + ", PW: " + globals.passwordT + ", DB: " + globals.databaseT)
        try:
            mydb = mysql.connector.connect(
                host = globals.hostname,
                user = globals.username,
                password = globals.passwordT,
                database = globals.databaseT)
            mycursor = mydb.cursor()

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except:
            self.window = QtWidgets.QMainWindow()
            self.message = "Invalid Login, Try Again."
            self.ui = Ui_errorWindow(self.message)
            self.ui.setupUi(self.window)
            self.window.show()
    
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(268, 301)
        self.gridLayout = QtWidgets.QGridLayout(loginWindow)
        self.gridLayout.setObjectName("gridLayout")
        
        #Submit Button
        self.submit = QtWidgets.QPushButton(loginWindow)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 10, 0, 1, 1)
        self.submit.clicked.connect(self.login)
        
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        
        #HostName LineEdit
        self.host = QtWidgets.QLineEdit(loginWindow)
        self.host.setObjectName("host")
        self.gridLayout.addWidget(self.host, 3, 0, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(loginWindow)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(loginWindow)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        
        self.label = QtWidgets.QLabel(loginWindow)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        
        #Database LineEdit
        self.database = QtWidgets.QLineEdit(loginWindow)
        self.database.setObjectName("database")
        self.gridLayout.addWidget(self.database, 9, 0, 1, 1)
        
        #Password LineEdit
        self.password = QtWidgets.QLineEdit(loginWindow)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 7, 0, 1, 1)
        
        #Username LineEdit
        self.user = QtWidgets.QLineEdit(loginWindow)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 5, 0, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(loginWindow)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.submit.setText(_translate("loginWindow", "Login"))
        self.label_2.setText(_translate("loginWindow", "Enter User Name"))
        self.label_3.setText(_translate("loginWindow", "Enter Password"))
        self.label_4.setText(_translate("loginWindow", "Enter Database Name"))
        self.label.setText(_translate("loginWindow", "Enter Host Name (eg. localhost)"))
        self.label_5.setText(_translate("loginWindow", "                                     Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

