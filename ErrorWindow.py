from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_errorWindow(object):
    #Recives message from external class to display
    def __init__(self, message):
        self.message = message
    
    def setupUi(self, errorWindow):
        errorWindow.setObjectName("errorWindow")
        errorWindow.resize(200, 90)
        
        #Error Output Label
        self.label = QtWidgets.QLabel(errorWindow)
        self.label.setGeometry(QtCore.QRect(9, 9, 181, 41))
        self.label.setObjectName("label")
        
        #Close Button 
        self.close = QtWidgets.QPushButton(errorWindow)
        self.close.setGeometry(QtCore.QRect(9, 60, 181, 23))
        self.close.setObjectName("close")

        self.retranslateUi(errorWindow)
        QtCore.QMetaObject.connectSlotsByName(errorWindow)

    def retranslateUi(self, errorWindow):
        _translate = QtCore.QCoreApplication.translate
        errorWindow.setWindowTitle(_translate("errorWindow", "Error"))
        self.label.setText(_translate("errorWindow", self.message))
        self.close.setText(_translate("errorWindow", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    errorWindow = QtWidgets.QDialog()
    ui = Ui_errorWindow()
    ui.setupUi(errorWindow)
    errorWindow.show()
    sys.exit(app.exec_())
