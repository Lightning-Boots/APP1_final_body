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
        Fenetre_principale.close()
        Fenetre_allumette.show()
    
    def IAG(self): 
        Fenetre_principale.close()
        Fenetre_allumette.show()



class Choix_nombre_allumette(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Nombre d'allumette") 

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumette : ")
        self.text.setStyleSheet("color: black; font-size : 15px; background-color: none")

        self.textbox = QLineEdit(self)
        self.textbox.setText("0")

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
        if textboxValue == "":
            return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre", QMessageBox.Ok, QMessageBox.Ok)
        elif textboxValue == "0":
            return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre supérieur à 0", QMessageBox.Ok, QMessageBox.Ok)
        for i in textboxValue :
            if i not in chiffre :
                return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre", QMessageBox.Ok, QMessageBox.Ok)
            elif i == "-" :
                return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre positif", QMessageBox.Ok, QMessageBox.Ok)
        Fenetre_allumette.close()
        Fenetre_coup.show()



class Choix_coup_max(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Coup max") 

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumette maximum à retirer par tour : ")
        self.text.setStyleSheet("color: black; font-size : 15px; background-color: none")

        self.textbox = QLineEdit(self)
        self.textbox.setText("0")

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
        chiffre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        if textboxValue == "":
            return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre", QMessageBox.Ok, QMessageBox.Ok)
        elif textboxValue == "0":
            return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre supérieur à 0", QMessageBox.Ok, QMessageBox.Ok)
        for i in textboxValue :
            if i not in chiffre :
                return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre", QMessageBox.Ok, QMessageBox.Ok)
            elif i == "-" :
                return QMessageBox.question(self, 'Message - pythonspot.com', "Entrez un nombre positif", QMessageBox.Ok, QMessageBox.Ok)




    
app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)
 

Fenetre_principale = Fenetre()
Fenetre_allumette = Choix_nombre_allumette() 
Fenetre_coup = Choix_coup_max()
Fenetre_principale.show() 
app.exec_()