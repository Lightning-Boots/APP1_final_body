import sys 
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow, QMessageBox, QPushButton, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt, QCoreApplication 
from PyQt5 import QtCore
class Fenetre(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Bouto's") 
        self.button = QPushButton("IA gagnante") 
        self.button.clicked.connect(self.IAG)
        self.button2 = QPushButton("IA aléatoire") 
        self.button2.clicked.connect(self.IAA)  



        self.layout = QGridLayout() 
        self.layout.addWidget(self.button,0,0) 
        self.layout.addWidget(self.button2,0,1) 

        self.widget = QWidget() 
        self.widget.setLayout(self.layout) 
        self.setCentralWidget(self.widget)


    def IAA(self): 
        window1.close()
        window2.show()
    
    def IAG(self): 
        window1.close()
        window2.show()
    

 
#window = Fenetre() 
#window.show() 



class Choix(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Bouto's") 


        
        self.text = QLabel(self)
        self.text.setText("Nombre de Bâton : ")
        self.text.setStyleSheet("color: black; font-size : 15px; background-color: none")




        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)

        self.button = QPushButton('Show text', self)
        self.button.clicked.connect(self.on_click)



        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.addWidget(self.text,0,0)
        self.layout.addWidget(self.textbox,1,0)
        self.layout.addWidget(self.button,2,0)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget) 






        


    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)




    
app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)
 

window1 = Fenetre()
window2 = Choix() 
window1.show() 
app.exec_()