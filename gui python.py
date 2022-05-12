#pip install pyqt5
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

iconroot = os.path.dirname(__file__)

stylesheet = """
    App {
        background-image: url("D:/driv downloads/Project Compiler/Project Compiler/background.jpeg"); 
        
        
    }
"""

class App(QMainWindow):
    
 

    def __init__(self):
        super().__init__()
        self.title = 'Compiler Version (1)'
        self.left = 10
        self.top = 10
        self.width = 1689
        self.height = 700
        self.initUI()
    
    def initUI(self):
        
    
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.hlay = QtWidgets.QHBoxLayout(self)
        
        buckling_blabel = QLabel(self)
        pixmap = QtGui.QPixmap(os.path.join(iconroot, "D:/driv downloads/Project Compiler/Project Compiler/Arrow.png"))
        buckling_blabel.setPixmap(pixmap.scaled(buckling_blabel.size(), QtCore.Qt.KeepAspectRatio))
        pixmap = pixmap.scaledToWidth(100)
        buckling_blabel.setPixmap(pixmap)
        buckling_blabel.move(575, 200)
        self.hlay.addWidget(buckling_blabel)
        
        
        buckling_blabel = QLabel(self)
        pixmap = QtGui.QPixmap(os.path.join(iconroot, "D:/driv downloads/Project Compiler/Project Compiler/Arrow.png"))
        buckling_blabel.setPixmap(pixmap.scaled(buckling_blabel.size(), QtCore.Qt.KeepAspectRatio))
        pixmap = pixmap.scaledToWidth(100)
        buckling_blabel.setPixmap(pixmap)
        buckling_blabel.move(1000, 200)
        self.hlay.addWidget(buckling_blabel)        
        
        
        self.label_1 = QLabel('Step 1', self)
        self.label_1.move(225, 20)
        self.label_1.setFont(QFont('Arial', 20))
        
        self.label_1 = QLabel('OR', self)
        self.label_1.move(225, 460)
        self.label_1.setFont(QFont('Arial', 20))
        
        self.label_1 = QLabel('Step 2', self)
        self.label_1.move(800, 20)
        self.label_1.setFont(QFont('Arial', 20))  
        
        
        self.label_1 = QLabel('Step 3', self)
        self.label_1.move(1375, 20)
        self.label_1.setFont(QFont('Arial', 20))     
        
              
        
        
        # Create textbox
        self.textbox1 = QTextEdit(self)
        self.textbox1.move(20, 70)
        self.textbox1.resize(500,300)
        
        self.textbox2 = QTextEdit(self)
        self.textbox2.move(1170, 70)
        self.textbox2.resize(500,300)        
        
        
        # Create a button 0
        self.button0 = QPushButton('Run Code', self)
        self.button0.move(155,400)
        self.button0.resize(200,50)
        # connect button to function on_click
        self.button0.clicked.connect(self.getfiles)         
        
        
        
        # Create a button 1
        self.button1 = QPushButton('Upload text file', self)
        self.button1.move(155,500)
        self.button1.resize(200,50)
        # connect button to function on_click
        self.button1.clicked.connect(self.getfiles)        
        
        # Create a button 2
        self.button2 = QPushButton('Show laxiem', self)
        self.button2.move(750,70)
        self.button2.resize(200,50)
        # connect button to function on_click
        self.button2.clicked.connect(self.getfilelaxiem)         
        
        # Create a button 3
        self.button3 = QPushButton('Show tokins', self)
        self.button3.move(750,200)
        self.button3.resize(200,50)
        # connect button to function on_click
        self.button3.clicked.connect(self.getfiletokins)         
        
        # Create a button 4
        self.button4 = QPushButton('Show parsing', self)
        self.button4.move(750,330)
        self.button4.resize(200,50)
        # connect button to function on_click
        self.button4.clicked.connect(self.getfileparsing)         
        
       
        
        self.show()
   
            
    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.textbox1.setText(data)
            
            
    def getfilelaxiem(self):
        f = open('D:/driv downloads/Project Compiler/Project Compiler/Tokenizing_phase.txt','r')
        with f:
            data = f.read()
            self.textbox2.setText(data)  
                
                
    def getfiletokins(self):
       
        f = open('D:/driv downloads/Project Compiler/Project Compiler/Identification_phase.txt','r')
        with f:
            data = f.read()
            self.textbox2.setText(data)   
            
    def getfileparsing(self):

        f = open('D:/driv downloads/Project Compiler/Project Compiler/Parsing_phase.txt','r')
        with f:
            data = f.read()
            self.textbox2.setText(data)  
            
    

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet) 
    
    ex = App()
    sys.exit(app.exec_())
      
    
    
