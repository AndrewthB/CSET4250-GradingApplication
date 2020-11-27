from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_Edit(object):
    def editEntry(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "yourusername",
            password = "yourpassword",
            database = "TestDatabase")
        mycursor = mydb.cursor()

    #Passing LineEdit into Parameters
        #WHERE statement variables
        entryID = self.entryID.text()
        #SET statement variables
        firstName = self.firstName.text()
        lastName = self.lastName.text()
        year = self.year.text()
        className = self.className.text()
        assignType = self.assignType.text()
        assignName = self.assignName.text()
        gradeValue = self.gradeValue.text()

        #SQL INSERT statement
        try:
            set = "firstName = '" + firstName + "', lastName = '" + lastName + "', year = '" + year + "', Class = '" + className + "', Grade = '" + gradeValue + "', assignmentName = '" + assignName + "', assignmentType = '" + assignType + "'"
            query = "UPDATE TestTable SET "+ set +" WHERE firstName = "+ fnameEdit +", lastName = "+ lnameEdit +", assignmentName = "+ WasgnName +";"
            print(query)
            mycursor.execute(query)
            mydb.commit()
            mycursor.close()
        except:
            print("Something went wrong")

    def setupUi(self, Edit):
        Edit.setObjectName("Edit")
        Edit.resize(447, 384)
        
        #Submit button
        self.submit = QtWidgets.QPushButton(Edit)
        self.submit.setGeometry(QtCore.QRect(10, 350, 211, 23))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.editEntry)
        
        #Cancel button
        self.cancel = QtWidgets.QPushButton(Edit)
        self.cancel.setGeometry(QtCore.QRect(225, 350, 211, 23))
        self.cancel.setObjectName("cancel")
        
        #Layout/Grid Widget
        self.layoutWidget = QtWidgets.QWidget(Edit)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 10, 280, 330))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        #Header Label
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        
        #Change First Name Label
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        
        #Change First Name LineEdit
        self.firstName = QtWidgets.QLineEdit(self.layoutWidget)
        self.firstName.setObjectName("firstName")
        self.gridLayout.addWidget(self.firstName, 2, 0, 1, 1)
        
        #Change Last Name Label
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        
        #Change Last Name LineEdit
        self.lastName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lastName.setObjectName("lastName")
        self.gridLayout.addWidget(self.lastName, 4, 0, 1, 1)
        
        #Change Year Label
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        
        #Change Year LineEdit
        self.year = QtWidgets.QLineEdit(self.layoutWidget)
        self.year.setObjectName("year")
        self.gridLayout.addWidget(self.year, 6, 0, 1, 1)
        
        #Change Class Name Label
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        
        #Change Class Name EditLine
        self.className = QtWidgets.QLineEdit(self.layoutWidget)
        self.className.setObjectName("className")
        self.gridLayout.addWidget(self.className, 8, 0, 1, 1)
        
        #Change Assignment Type Label
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        
        #Change Assignment LineEdit 
        self.assignType = QtWidgets.QLineEdit(self.layoutWidget)
        self.assignType.setObjectName("assignType")
        self.gridLayout.addWidget(self.assignType, 10, 0, 1, 1)
        
        #Change Assignment Name Label
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)
        
        #Change Assignment Name LineEdit
        self.assignName = QtWidgets.QLineEdit(self.layoutWidget)
        self.assignName.setObjectName("assignName")
        self.gridLayout.addWidget(self.assignName, 12, 0, 1, 1)
        
        #Change Grade Value Label
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)
        
        #Change Grade Value LineEdit
        self.gradeValue = QtWidgets.QLineEdit(self.layoutWidget)
        self.gradeValue.setObjectName("gradeValue")
        self.gridLayout.addWidget(self.gradeValue, 14, 0, 1, 1)
        
        #Entry ID Label
        self.label_10 = QtWidgets.QLabel(Edit)
        self.label_10.setGeometry(QtCore.QRect(11, 30, 130, 16))
        self.label_10.setObjectName("label_10")
        
        #Entry ID LineEdit
        self.entryID = QtWidgets.QLineEdit(Edit)
        self.entryID.setGeometry(QtCore.QRect(11, 49, 133, 20))
        self.entryID.setObjectName("entryID")
        
        #Header Label
        self.label_9 = QtWidgets.QLabel(Edit)
        self.label_9.setGeometry(QtCore.QRect(11, 11, 139, 16))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Edit)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        _translate = QtCore.QCoreApplication.translate
        Edit.setWindowTitle(_translate("Edit", "Edit Entry"))
        self.submit.setText(_translate("Edit", "Enter"))
        self.cancel.setText(_translate("Edit", "Cancel"))
        self.label_8.setText(_translate("Edit", "Enter Values to Edit existing Entry"))
        self.label.setText(_translate("Edit", "Change First Name"))
        self.label_2.setText(_translate("Edit", "Change Last Name"))
        self.label_3.setText(_translate("Edit", " Change Education Level (eg. Freshman, Sophomore, etc)"))
        self.label_4.setText(_translate("Edit", "Change Class ID"))
        self.label_5.setText(_translate("Edit", "Change Assignment Type"))
        self.label_6.setText(_translate("Edit", "Change Assignment Name"))
        self.label_7.setText(_translate("Edit", "Change Grade"))
        self.label_10.setText(_translate("Edit", "Enter Entry ID"))
        self.label_9.setText(_translate("Edit", "Specifying Entry to be Edited"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edit = QtWidgets.QDialog()
    ui = Ui_Edit()
    ui.setupUi(Edit)
    Edit.show()
    sys.exit(app.exec_())

