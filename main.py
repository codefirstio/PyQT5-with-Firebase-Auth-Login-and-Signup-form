import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

firebaseConfig={'apiKey': "AIzaSyD9Bgw0XS4Oj_9viko9Fy3fZ2Wd7W0u72k",
    'authDomain': "authdemo-16c35.firebaseapp.com",
    'databaseURL': "https://authdemo-16c35.firebaseio.com",
    'projectId': "authdemo-16c35",
    'storageBucket': "authdemo-16c35.appspot.com",
    'messagingSenderId': "752256979947",
    'appId': "1:752256979947:web:2f71846c1d795d09db3fae",
    'measurementId': "G-W4KNLK3307"}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid.setVisible(False)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        try:
            auth.sign_in_with_email_and_password(email,password)
        except:
            self.invalid.setVisible(True)
    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            try:
                auth.create_user_with_email_and_password(email,password)
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except:
                self.invalid.setVisible(True)




app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
