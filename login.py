from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from Main import Ui_MainWindow
import globals

class Ui_loginWindow(object):
    def login(self):
        globals.hostname = self.host.text()
        globals.username = self.user.text()
        globals.passwordT = self.password.text()
        globals.databaseT = self.database.text()
        print("Raw Output: Host: "+ globals.hostname +", User: " + globals.username + ", PW: " + globals.passwordT + ", DB: " + globals.databaseT)
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
            print("Invalid Login")

    
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(151, 300)
        
        self.host = QtWidgets.QLineEdit(loginWindow)
        self.host.setGeometry(QtCore.QRect(9, 71, 133, 20))
        self.host.setObjectName("host")
        
        self.user = QtWidgets.QLineEdit(loginWindow)
        self.user.setGeometry(QtCore.QRect(9, 128, 133, 20))
        self.user.setObjectName("user")
        
        self.password = QtWidgets.QLineEdit(loginWindow)
        self.password.setGeometry(QtCore.QRect(9, 185, 133, 20))
        self.password.setObjectName("password")
        
        self.database = QtWidgets.QLineEdit(loginWindow)
        self.database.setGeometry(QtCore.QRect(9, 242, 133, 20))
        self.database.setObjectName("database")
        
        self.label = QtWidgets.QLabel(loginWindow)
        self.label.setGeometry(QtCore.QRect(40, 40, 81, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(loginWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 75, 16))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(loginWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 105, 16))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(loginWindow)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 25, 16))
        self.label_5.setObjectName("label_5")
        
        self.submit = QtWidgets.QPushButton(loginWindow)
        self.submit.setGeometry(QtCore.QRect(40, 270, 75, 23))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.login)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.label.setText(_translate("loginWindow", "Enter Host Name"))
        self.label_2.setText(_translate("loginWindow", "Enter User Name"))
        self.label_3.setText(_translate("loginWindow", "Enter Password"))
        self.label_4.setText(_translate("loginWindow", "Enter Database Name"))
        self.label_5.setText(_translate("loginWindow", "Login"))
        self.submit.setText(_translate("loginWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

