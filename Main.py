from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import *
from ADD import Ui_ADD
from DEL import Ui_Delete
from EDT import Ui_Edit
from ErrorWindow import Ui_errorWindow
import globals


class Ui_MainWindow(object):
#Shows all table entries
    def show_ALL(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = globals.hostname,
            user = globals.username,
            password = globals.passwordT,
            database = globals.databaseT)
        mycursor = mydb.cursor()
        
        #Print TestTable to GUI Table
        query = "SELECT * FROM TestTable;"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        mycursor.close()

#Sort table entries by Assignment Name
    def sort_Assignment(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = globals.hostname,
            user = globals.username,
            password = globals.passwordT,
            database = globals.databaseT)
        mycursor = mydb.cursor()
        
        #Print TestTable to GUI Table
        query = "SELECT * FROM TestTable GROUP BY assignmentName;"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        mycursor.close()

#Sort table entires by Student Name (first name)
    def sort_Student(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = globals.hostname,
            user = globals.username,
            password = globals.passwordT,
            database = globals.databaseT)
        mycursor = mydb.cursor()
        
        #Print TestTable to GUI Table
        query = "SELECT * FROM TestTable GROUP BY firstName;"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        mycursor.close()

#Sort table by Class name
    def sort_Class(self):
        #Login to SQL Database
        mydb = mysql.connector.connect(
            host = globals.hostname,
            user = globals.username,
            password = globals.passwordT,
            database = globals.databaseT)
        mycursor = mydb.cursor()
        
        #Print TestTable to GUI Table
        query = "SELECT * FROM TestTable GROUP BY Class;"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        mycursor.close()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#Launch Popup Window displaying Add Entry forum
    def queryIN(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ADD()
        self.ui.setupUi(self.window)
        self.window.show()

#Launch Popup Window displaying Delete Entry forum
    def queryDL(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Delete()
        self.ui.setupUi(self.window)
        self.window.show()

#Launch Popup Window displaying Edit Entry forum
    def queryED(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Edit()
        self.ui.setupUi(self.window)
        self.window.show()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        #ADD entry to table
        self.query_IN = QtWidgets.QPushButton(self.centralwidget)
        self.query_IN.setObjectName("query_IN")
        self.gridLayout.addWidget(self.query_IN, 1, 4, 1, 1)
        self.query_IN.clicked.connect(self.queryIN)
        
        #Edit entry in table
        self.query_ED = QtWidgets.QPushButton(self.centralwidget)
        self.query_ED.setObjectName("query_ED")
        self.gridLayout.addWidget(self.query_ED, 1, 6, 1, 1)
        self.query_ED.clicked.connect(self.queryED)
        
        #Sort table by Student Name
        self.sortStudent = QtWidgets.QPushButton(self.centralwidget)
        self.sortStudent.setObjectName("sortStudent")
        self.gridLayout.addWidget(self.sortStudent, 1, 1, 1, 1)
        self.sortStudent.clicked.connect(self.sort_Student)
        
        #Sort table by Class
        self.sortClass = QtWidgets.QPushButton(self.centralwidget)
        self.sortClass.setObjectName("sortClass")
        self.gridLayout.addWidget(self.sortClass, 1, 3, 1, 1)
        self.sortClass.clicked.connect(self.sort_Class)
        
        #Delete entry from table
        self.query_DL = QtWidgets.QPushButton(self.centralwidget)
        self.query_DL.setObjectName("query_DL")
        self.gridLayout.addWidget(self.query_DL, 1, 5, 1, 1)
        self.query_DL.clicked.connect(self.queryDL)
        
        #Table Widget max 8 columns by 100 rows
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(100)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 7)
        
        #Show all entries in table
        self.show_table = QtWidgets.QPushButton(self.centralwidget)
        self.show_table.setObjectName("show_table")
        self.gridLayout.addWidget(self.show_table, 1, 0, 1, 1)
        self.show_table.clicked.connect(self.show_ALL)
        
        #Sort table by Assignment Name 
        self.sortAssignment = QtWidgets.QPushButton(self.centralwidget)
        self.sortAssignment.setObjectName("sortAssignment")
        self.gridLayout.addWidget(self.sortAssignment, 1, 2, 1, 1)
        self.sortAssignment.clicked.connect(self.sort_Assignment)
        
        #Status Bar  
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.query_IN.setText(_translate("MainWindow", "Add Item"))
        self.query_ED.setText(_translate("MainWindow", "Edit Item"))
        self.sortStudent.setText(_translate("MainWindow", "Sort By Student"))
        self.sortClass.setText(_translate("MainWindow", "Sort By Class"))
        self.query_DL.setText(_translate("MainWindow", "Delete Item"))
        self.show_table.setText(_translate("MainWindow", "Show All Grades"))
        self.sortAssignment.setText(_translate("MainWindow", "Sort By Asgmt"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
