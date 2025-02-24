import sys 
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow, QMessageBox, QPushButton, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt, QCoreApplication 
from PyQt5 import QtCore

class Fenetre(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Jeux de Nim") 


        self.button1 = QPushButton("IA gagnante") 
        self.button1.clicked.connect(self.IAG)
        self.button2 = QPushButton("IA aléatoire") 
        self.button2.clicked.connect(self.IAA)  


        self.grid = QGridLayout() 
        self.grid.addWidget(self.button1,0,0) 
        self.grid.addWidget(self.button2,0,1) 
        
        self.widget = QWidget() 
        self.widget.setLayout(self.grid) 
        self.setCentralWidget(self.widget)


    def IAA(self): 
        window1.close()
        window2.show()
    
    def IAG(self): 
        window1.close()
        window2.show()



class Choix_nombre_allumette(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Nombre d'allumette") 

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumette : ")
        self.text.setStyleSheet("color: black; font-size : 15px; background-color: none")

        self.textbox = QLineEdit(self)

        self.button = QPushButton('Valider', self)
        self.button.clicked.connect(self.on_click)


        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.addWidget(self.text,0,0)
        self.grid.addWidget(self.textbox,1,0)
        self.grid.addWidget(self.button,2,0)

        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget) 

    
    def on_click(self):
        chiffre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        textboxValue = self.textbox.text()
        for i in textboxValue :
            if i not in chiffre :
                return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre", QMessageBox.Ok, QMessageBox.Ok)
            elif i == "-" :
                return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre positif", QMessageBox.Ok, QMessageBox.Ok)
        window2.close()
        window3.show()



class Choix_coup_max(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Coup max") 

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumette maximum à retirer par tour : ")
        self.text.setStyleSheet("color: black; font-size : 15px; background-color: none")

        self.textbox = QLineEdit(self)

        self.button = QPushButton('Valider', self)
        self.button.clicked.connect(self.on_click)


        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.addWidget(self.text,0,0)
        self.grid.addWidget(self.textbox,1,0)
        self.grid.addWidget(self.button,2,0)

        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget) 

    
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)




    
app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)
 

window1 = Fenetre()
window2 = Choix_nombre_allumette() 
window3 = Choix_coup_max()
window1.show() 
app.exec_()