"""Codes pour l'interface graphique du jeu et son bon fonctionnement"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout,QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from Jeu import nombre_allumette, Coup_max, IA
from gagnant import trouver_meilleur_coup
from aleatoire import play_random_move_V2




class Jeu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(700, 300, 1000, 500)


        self.button = QPushButton("Enlever") 
        self.button.clicked.connect(self.onClickEnlever)
        self.button.setStyleSheet("color: white; font-size : 25px; background-color: black")

        self.text = QLabel(self)
        self.text.setText("Nombre d'allumettes : " + str(nombre_allumette))
        self.text.setGeometry(0, self.height()//2-20, self.width(), 60)
        self.text.setStyleSheet("color: white; font-size : 25px; background-color: none")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox = QLineEdit(self)
        self.textbox.setText("Entrez ici le nombre d'allumette à enlever")
        self.textbox.setGeometry(0, self.height()//2+60, self.width(), 40)
        self.textbox.setStyleSheet("color: gray; font-size : 25px; background-color: black")
        self.textbox.setAlignment(QtCore.Qt.AlignCenter)

        self.central_widget = QWidget(self)
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
        self.central_widget.setLayout(self.vbox)
        self.central_widget.setGeometry(0, self.height()//2+100, self.width(), 40)
        self.vbox.addWidget(self.button)
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)

        
        #rectangle gris, background des gif chats
        self.band = QWidget(self)
        self.band.setStyleSheet("background-color: gray;")
        self.rect = QHBoxLayout(self.band)
        self.rect.setSpacing(0)
        self.band.setGeometry(0, 0, self.width(), self.height() // 3+40)


        self.label = [QLabel(self) for i in range(nombre_allumette)] #Liste de label
        self.labels = QHBoxLayout()
        self.labels.setSpacing(0)
        self.movie = QMovie("APP1_final_body/vibe-cat.gif")

        #Une boucle qui pour chaque élément de la liste de QLabel, prend cet élément le change en chat et l'ajoute à la QHBox
        for i in range(len(self.label)):
            self.label[i].setMovie(self.movie)
            self.label[i].setScaledContents(True)
            self.labels.addWidget(self.label[i])


        self.movie.start()#démare les gif
        self.setLayout(self.labels)
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        
    #Fonction qui rend la fenetre dynamique
    def resizeEvent(self, event):
        self.band.setGeometry(0, 0, self.width(), self.height() // 3+40)
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        self.text.setGeometry(0, self.height()//2-20, self.width(), 60)
        self.textbox.setGeometry(0, self.height()//2+60, self.width(), 40)
        self.central_widget.setGeometry(0, self.height()//2+120, self.width(), self.height()//4)
        
        #Utilisation de Pythagore pour avoir un texte à la bonne taille
        py = (self.width()**2 + self.height()**2)**(1/2) //30
        py = int(py)
        self.button.setStyleSheet("color: white; font-size : " + str(py) + "px; background-color: black")
        self.text.setStyleSheet("color: white; font-size : " + str(py) + "px; background-color: none") 
        self.text.setStyleSheet("color: white; font-size : "  + str(py) + "px; background-color: none")

    #Fonction qui s'active lorsque qu'on valide le nombre d'allumettes à enlever
    def onClickEnlever(self):
        global nombre_allumette

        #Vérification que la donnée rentrée soit un nombre correct
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
            
        #Partie qui effectue les actions d'un tour de jeu
        nombre_allumette -= int(textboxValue)
        if nombre_allumette == 0 :
            return fenetre.close()
        #L'IA agit en fonction du mode de jeu choisi au début
        elif IA == "Gagnante":
            coup_IA = trouver_meilleur_coup(nombre_allumette, Coup_max)
        elif IA == "Aleatoire":
            coup_IA = play_random_move_V2(nombre_allumette, Coup_max)
        nombre_allumette -= coup_IA #L'IA joue
        if nombre_allumette == 0 :
            return fenetre.close()
        
        #On enlève un par un les chats à enlever dans la QVBox
        for i in range (int(textboxValue) + coup_IA):#Ajout des deux coups pour savoir le nombre d'allumettes total à enlever
            derniere_image = self.labels.takeAt(self.labels.count() - 1)
            derniere_image.widget().deleteLater()
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        #On change le texte pour indiquer le coup de l'IA et le nombre d'allumettes restantes
        self.text.setText("Nombre d'allumettes : " + str(nombre_allumette))
        self.textbox.setText("L'IA a enlevée : " + str(coup_IA))


        return nombre_allumette #actualise le nombre d'allumettes








app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)

#On défini la fenetre et on la montre
fenetre = Jeu()
fenetre.show()

app.exec_()