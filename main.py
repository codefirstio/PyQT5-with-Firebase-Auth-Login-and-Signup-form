
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sys
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.clickhere.clicked.connect(self.createAcc)
        self.login.clicked.connect(self.loginnow)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def createAcc(self):
        create=CreateAcc()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loginnow(self):
        email=self.email.text()
        password=self.password.text()
        print("Successfully logged in with email: ", email, "and password: ", password)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.confirmacc.clicked.connect(self.confirm)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    
    def confirm(self):
        email=self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Success. New account user: ", email, "password: ",password)
            self.backtologin()

    def backtologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(620)
widget.setFixedWidth(480)
widget.show()
app.exec_()