import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QIcon
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        #button1
        self.btn1=QPushButton('Message',self)        
        self.btn1.clicked.connect(self.activateMessage)
        #button2
        self.btn2=QPushButton('Clear',self)        
        self.btn2.clicked.connect(self.clearMessage)

        hbox=QHBoxLayout()
        hbox.addStretch(1) #공백
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox=QVBoxLayout()        
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.setWindowIcon(QIcon('calc.png'))         
        self.setWindowTitle('계산기')
        self.resize(256,256)
        self.show()
    def activateMessage(self):
        #QMessageBox.information(self, "information","Button Clicked")
        self.te1.appendPlainText('Button Clicked')
    def clearMessage(self):        
        self.te1.clear()
if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
