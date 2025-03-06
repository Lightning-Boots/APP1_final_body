import sys 
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QMessageBox, QPushButton, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import QCoreApplication 

class Fenetre(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Jeux de Nim") 
        self.setStyleSheet("background-color: black") 

        self.button1 = QPushButton("IA gagnante") 
        self.button1.clicked.connect(self.IAG)
        self.button2 = QPushButton("IA aléatoire") 
        self.button2.clicked.connect(self.IAA)  
        self.button1.setStyleSheet("color: white; background-color: black")
        self.button2.setStyleSheet("color: white; background-color: black")


        self.grid = QGridLayout() 
        self.grid.addWidget(self.button1,0,0) 
        self.grid.addWidget(self.button2,0,1) 
        
        self.widget = QWidget() 
        self.widget.setLayout(self.grid) 
        self.setCentralWidget(self.widget)


    def IAA(self): 
        global IA
        IA = "Aleatoire"
        Fenetre_principale.close()
        Fenetre_allumette.show()
    
    def IAG(self):
        global IA
        IA = "Gagnante" 
        Fenetre_principale.close()
        Fenetre_allumette.show()



class Choix_nombre_allumette(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Nombre d'allumette")
        self.setStyleSheet("background-color: black") 

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumette : ")
        self.text.setStyleSheet("color: white; font-size : 15px; background-color: black")

        self.textbox = QLineEdit(self)
        self.textbox.setText("0")
        self.textbox.setStyleSheet("color: white")

        self.button = QPushButton('Valider', self)
        self.button.clicked.connect(self.on_click)
        self.button.setStyleSheet("color: white; background-color: black")


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
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Erreur")
        msg_box.setStyleSheet("QLabel { color: white; }")  
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.addButton(QMessageBox.Ok)
        if textboxValue == "":
            msg_box.setText("Entrez un nombre")
            return msg_box.exec_() 
        elif textboxValue == "0":
            msg_box.setText("Entrez un nombre supérieur à 0")
            return msg_box.exec_() 
        for i in textboxValue :
            if i not in chiffre :
                msg_box.setText("Entrez un nombre")
                return msg_box.exec_() 
            elif i == "-" :
                msg_box.setText("Entrez un nombre positif")
                return msg_box.exec_() 
        global nombre_allumette
        nombre_allumette = int(textboxValue)
        Fenetre_allumette.close()
        Fenetre_coup.show()



class Choix_coup_max(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Coup max") 
        self.setStyleSheet("background-color: black") 

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumette maximum à retirer par tour : ")
        self.text.setStyleSheet("color: white; font-size : 15px; background-color: black")

        self.textbox = QLineEdit(self)
        self.textbox.setText("0")
        self.textbox.setStyleSheet("color: white")

        self.button = QPushButton('Valider', self)
        self.button.clicked.connect(self.on_click)
        self.button.setStyleSheet("color: white; background-color: black")


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
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Erreur")
        msg_box.setStyleSheet("QLabel { color: white; }")  
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.addButton(QMessageBox.Ok)
        if textboxValue == "":
            msg_box.setText("Entrez un nombre")
            return msg_box.exec_() 
        elif textboxValue == "0":
            msg_box.setText("Entrez un nombre supérieur à 0")
            return msg_box.exec_() 
        for i in textboxValue :
            if i not in chiffre :
                msg_box.setText("Entrez un nombre")
                return msg_box.exec_() 
            elif i == "-" :
                msg_box.setText("Entrez un nombre positif")
                return msg_box.exec_() 
        global Coup_max
        Coup_max = int(textboxValue)
        Fenetre_coup.close()


global IA, nombre_allumette, Coup_max

nombre_allumette = 0
Coup_max = 0
IA  = 0



app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)
 
Fenetre_principale = Fenetre()
Fenetre_allumette = Choix_nombre_allumette() 
Fenetre_coup = Choix_coup_max()
Fenetre_principale.show()

app.exec_()