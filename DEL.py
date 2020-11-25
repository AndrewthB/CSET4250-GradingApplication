from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_Delete(object):
    def deleteEntry(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "yourusername",
            password = "yourpassword",
            database = "TestDatabase")
        mycursor = mydb.cursor()

        #Passing LineEdit into Parameters
        entryID = self.entryID.text()
        
        #SQL INSERT statement
        query = "DELETE FROM TestTable WHERE (entryID = '" + entryID + "');"
        #print(query)
        mycursor.execute(query)
        mydb.commit()
        mycursor.close()
    
    def setupUi(self, Delete):
        Delete.setObjectName("Delete")
        Delete.resize(322, 128)
        
        #Submit Button
        self.submit = QtWidgets.QPushButton(Delete)
        self.submit.setGeometry(QtCore.QRect(7, 90, 147, 23))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.deleteEntry)

        #Cancel Button
        self.cancel = QtWidgets.QPushButton(Delete)
        self.cancel.setGeometry(QtCore.QRect(160, 90, 146, 23))
        self.cancel.setObjectName("cancel")
        
        #Header Label
        self.label_2 = QtWidgets.QLabel(Delete)
        self.label_2.setGeometry(QtCore.QRect(10, 8, 299, 16))
        self.label_2.setObjectName("label_2")
        
        #Enter ID LineEdit
        self.entryID = QtWidgets.QLineEdit(Delete)
        self.entryID.setGeometry(QtCore.QRect(10, 51, 299, 20))
        self.entryID.setObjectName("entryID")
        
        #Enter ID Label
        self.label = QtWidgets.QLabel(Delete)
        self.label.setGeometry(QtCore.QRect(10, 30, 147, 15))
        self.label.setObjectName("label")

        self.retranslateUi(Delete)
        QtCore.QMetaObject.connectSlotsByName(Delete)

    def retranslateUi(self, Delete):
        _translate = QtCore.QCoreApplication.translate
        Delete.setWindowTitle(_translate("Delete", "Delete Assignment Entry"))
        self.submit.setText(_translate("Delete", "Enter"))
        self.cancel.setText(_translate("Delete", "Cancel"))
        self.label_2.setText(_translate("Delete", "Specify an Entry by its ID for Deletion"))
        self.label.setText(_translate("Delete", "Enter Entry ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete = QtWidgets.QDialog()
    ui = Ui_Delete()
    ui.setupUi(Delete)
    Delete.show()
    sys.exit(app.exec_())

