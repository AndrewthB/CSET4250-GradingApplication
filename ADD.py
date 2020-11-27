from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_ADD(object):
    def addEntry(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "yourusername",
            password = "yourpassword",
            database = "TestDatabase")
        mycursor = mydb.cursor()

        #Passing LineEdit into Parameters
        entryID = self.entryID.text()
        firstName = self.firstName.text()
        lastName = self.lastName.text()
        year = self.year.text()
        className = self.className.text()
        assignType = self.assignType.text()
        assignName = self.assignName.text()
        gradeValue = self.gradeValue.text()
        
        #SQL INSERT statement
        try:
            query = "INSERT INTO TestTable (entryID, firstName, lastName, year, Class, Grade, assignmentName, assignmentType) VALUES ('"+ entryID + "', '" + firstName + "', '" + lastName + "', '" + year + "', '" + className + "', '" + gradeValue + "', '" + assignName + "', '" + assignType + "');"
        #print(query)
            mycursor.execute(query)
            mydb.commit()
            mycursor.close()
            
        except:
            print("Something went wrong")
    
    #def close(self):
    #    self.close()

    def setupUi(self, ADD):
        ADD.setObjectName("ADD")
        ADD.resize(314, 469)
        self.centralwidget = QtWidgets.QWidget(ADD)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        #Header Label
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        
        #Enter ID Label
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        
        #Enter ID LineEdit
        self.entryID = QtWidgets.QLineEdit(self.centralwidget)
        self.entryID.setObjectName("entryID")
        self.gridLayout.addWidget(self.entryID, 2, 0, 1, 1)
        
        #First Name Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        
        #First Name LineEdit
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setObjectName("firstName")
        self.gridLayout.addWidget(self.firstName, 4, 0, 1, 1)
        
        #Last Name Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        
        #Last Name LineEdit
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setObjectName("lastName")
        self.gridLayout.addWidget(self.lastName, 6, 0, 1, 1)
        
        #Year Label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        
        #Year LineEdit
        self.year = QtWidgets.QLineEdit(self.centralwidget)
        self.year.setObjectName("year")
        self.gridLayout.addWidget(self.year, 8, 0, 1, 1)
        
        #Class Name Label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        
        #Class Name LineEdit
        self.className = QtWidgets.QLineEdit(self.centralwidget)
        self.className.setObjectName("className")
        self.gridLayout.addWidget(self.className, 10, 0, 1, 1)
        
        #AssignmentType Label
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)
        
        #AssignmentType LineEdit
        self.assignType = QtWidgets.QLineEdit(self.centralwidget)
        self.assignType.setObjectName("assignType")
        self.gridLayout.addWidget(self.assignType, 12, 0, 1, 1)
        
        #AssignmentName Label
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)
        
        #AssignmentName LineEdit
        self.assignName = QtWidgets.QLineEdit(self.centralwidget)
        self.assignName.setObjectName("assignName")
        self.gridLayout.addWidget(self.assignName, 14, 0, 1, 1)
    
        #Grade Label
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 15, 0, 1, 1)
        
        #Grade LineEdit
        self.gradeValue = QtWidgets.QLineEdit(self.centralwidget)
        self.gradeValue.setObjectName("gradeValue")
        self.gridLayout.addWidget(self.gradeValue, 16, 0, 1, 1)
        
        #Submit Button
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 17, 0, 1, 1)
        self.submit.clicked.connect(self.addEntry)
        
        #Cancel Button
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 18, 0, 1, 1)
        #self.cancel.clicked.connect(lambda:self.close)
        
        ADD.setCentralWidget(self.centralwidget)
        self.retranslateUi(ADD)
        QtCore.QMetaObject.connectSlotsByName(ADD)

    def retranslateUi(self, ADD):
        _translate = QtCore.QCoreApplication.translate
        ADD.setWindowTitle(_translate("ADD", "Add Entry"))
        self.label_8.setText(_translate("ADD", "Enter Values to be enter into Database"))
        self.label_9.setText(_translate("ADD", "Entry ID (number value)"))
        self.label.setText(_translate("ADD", "First Name"))
        self.label_2.setText(_translate("ADD", "Last Name"))
        self.label_3.setText(_translate("ADD", "Education Level (eg. Freshman, Sophomore, Junior, Senor)"))
        self.label_4.setText(_translate("ADD", "Class ID"))
        self.label_5.setText(_translate("ADD", "Assignment Type"))
        self.label_6.setText(_translate("ADD", "Assignment Name"))
        self.label_7.setText(_translate("ADD", "Grade"))
        self.submit.setText(_translate("ADD", "Enter"))
        self.cancel.setText(_translate("ADD", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ADD = QtWidgets.QMainWindow()
    ui = Ui_ADD()
    ui.setupUi(ADD)
    ADD.show()
    sys.exit(app.exec_())

