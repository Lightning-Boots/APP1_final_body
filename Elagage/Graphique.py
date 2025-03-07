import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QGraphicsOpacityEffect, QGridLayout, QHBoxLayout,QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from Jeu import nombre_allumette, Coup_max, IA
from gagnant import trouver_meilleur_coup
from aleatoire import play_random_move_V2
from perdant import trouver_le_pire_coup




class Jeu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(700, 300, 1000, 500)


        self.button = QPushButton("Enlever") 
        self.button.clicked.connect(self.onClick)
        self.button.setStyleSheet("color: white; font-size : 25px; background-color: black")

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumettes : " + str(nombre_allumette))
        self.text.setGeometry(0, self.height()//2-20, self.width(), 60)
        self.text.setStyleSheet("color: white; font-size : 25px; background-color: none")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox = QLineEdit(self)
        self.textbox.setText("Entrez ici le nombre d'allumette à enlever")
        self.textbox.setGeometry(0, self.height()//2+60, self.width(), 40)
        self.textbox.setStyleSheet("color: white; font-size : 25px; background-color: black")
        self.textbox.setAlignment(QtCore.Qt.AlignCenter)

        self.central_widget = QWidget(self)
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
        self.central_widget.setLayout(self.vbox)
        self.central_widget.setGeometry(0, self.height()//2+100, self.width(), 40)
        self.vbox.addWidget(self.button)
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)

        

        self.band = QWidget(self)
        self.band.setStyleSheet("background-color: grey;")
        self.rect = QHBoxLayout(self.band)
        self.rect.setSpacing(0)
        self.band.setGeometry(0, 0, self.width(), self.height() // 3+40)


        self.label = [QLabel(self) for i in range(nombre_allumette)]
        self.labels = QHBoxLayout()
        self.labels.setSpacing(0)
        self.movie = QMovie("vibe-cat.gif")

        for i in range(len(self.label)):
            self.label[i].setMovie(self.movie)
            self.label[i].setScaledContents(True)
            self.labels.addWidget(self.label[i])


        self.movie.start()
        self.setLayout(self.labels)
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        

    def resizeEvent(self, event):
        self.band.setGeometry(0, 0, self.width(), self.height() // 3+40)
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        self.text.setGeometry(0, self.height()//2-20, self.width(), 60)
        self.textbox.setGeometry(0, self.height()//2+60, self.width(), 40)
        self.central_widget.setGeometry(0, self.height()//2+120, self.width(), self.height()//4)
        
        py = (self.width()**2 + self.height()**2)**(1/2) //30
        py = int(py)
        self.button.setStyleSheet("color: white; font-size : " + str(py) + "px; background-color: black")
        self.text.setStyleSheet("color: white; font-size : " + str(py) + "px; background-color: none") 
        self.text.setStyleSheet("color: white; font-size : "  + str(py) + "px; background-color: none")

    def onClick(self):
        global nombre_allumette

        textboxValue = self.textbox.text()
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
            elif int(textboxValue) > nombre_allumette:
                msg_box.setText("Entrez un nombre non supérieur au nombre d'allumette")
                return msg_box.exec_() 
            elif int(textboxValue) > Coup_max:
                msg_box.setText("Entrez un nombre inférieur ou égale à : " + str(Coup_max))
                return msg_box.exec_() 
            

        nombre_allumette -= int(textboxValue)
        if nombre_allumette == 0 :
            return fenetre.close()
        elif IA == "Gagnante":
            coup_IA = trouver_meilleur_coup(nombre_allumette, Coup_max)
        elif IA == "Aleatoire":
            coup_IA = play_random_move_V2(nombre_allumette, Coup_max)
        nombre_allumette -= coup_IA
        if nombre_allumette == 0 :
            return fenetre.close()
        for i in range (int(textboxValue) + coup_IA):
            derniere_image = self.labels.takeAt(self.labels.count() - 1)
            derniere_image.widget().deleteLater()
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        self.text.setText("Nombre d'allumettes : " + str(nombre_allumette))
        self.textbox.setText("L'IA a enlevée : " + str(coup_IA))


        return nombre_allumette








app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)


fenetre = Jeu()
fenetre.show()

app.exec_()