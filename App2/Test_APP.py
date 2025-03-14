# représenter un élément individuel de l'arbre,c'est à dire un tuple (mot_fr , mot_ang)
import csv
import random

class Noeud:
    def __init__(self, tuples_mots):
        self.mot= tuples_mots
        self.enfant_gauche = None
        self.enfant_droite = None

class ArbreBinaire:
    def __init__(self):
        self.racine = None

    def insertion(self, tuples_mots ):
        if self.racine is None:
            self.racine = Noeud(tuples_mots)
        else:
            self.insertion_rec(self.racine,tuples_mots)

    def insertion_rec(self, noeud,  tuples_mots):
        if  tuples_mots[0] < noeud.mot[0]:
            if noeud.enfant_gauche is None:
                noeud.enfant_gauche = Noeud(tuples_mots)
            else:
                self.insertion_rec(noeud.enfant_gauche, tuples_mots)
        else:
            if noeud.enfant_droite is None:
                noeud.enfant_droite = Noeud(tuples_mots)
            else:
                self.insertion_rec(noeud.enfant_droite,tuples_mots)

    def recherche_mot(self, mot_fr):
        return self.recherche_mot_rec(self.racine, mot_fr)

    def recherche_mot_rec(self, noeud, mot_fr):
        if noeud is None:
            return None
        if noeud.mot[0] == mot_fr:
            return noeud.mot[1]
        elif mot_fr < noeud.mot[0]:
            return self.recherche_mot_rec(noeud.enfant_gauche, mot_fr)
        else:
            return self.recherche_mot_rec(noeud.enfant_droite, mot_fr)
        

    # Fonction récursive pour afficher les noeuds avec un espacement (niveau de profondeur)
    def enregistrer_arbre(self):
        with open("Arbre.txt", 'w') as fichier:
            if self.racine is None:
                fichier.write("L'arbre est vide.\n")
            else:
                self.enregistrer_rec(self.racine, 0, fichier)

    # Fonction récursive pour enregistrer l'arbre dans un fichier
    def enregistrer_rec(self, noeud, niveau, fichier):
        if noeud is not None:
            if noeud.enfant_droite is not None:
                self.enregistrer_rec(noeud.enfant_droite, niveau + 1, fichier)
            fichier.write("   " * niveau + f"{noeud.mot[0]}: {noeud.mot[1]}\n")
            if noeud.enfant_gauche is not None:
                self.enregistrer_rec(noeud.enfant_gauche, niveau + 1, fichier)

#Création de l'arbre à partie de notre dossier CSV
def ouverture_fichier(nom_fichier):
    with open(f'App2/{nom_fichier}',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=';')
        fichier = []
        for row in reader:
            fichier.append(tuple(row))
    return fichier

def creation_arbre():
    arbre=ArbreBinaire()
    liste_mot= ouverture_fichier("test_APP2.csv")
    while len(liste_mot) > 0: 
        if len(liste_mot) > 1:
            nb_aleatoire = random.randint(0, len(liste_mot) - 1)  # Plage corrigée
        else:
            nb_aleatoire = 0 
        mot=liste_mot[nb_aleatoire]
        arbre.insertion(mot)
        liste_mot.pop(nb_aleatoire)
    arbre.enregistrer_arbre()
       
creation_arbre() 

#Importations
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog,QHBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt
import csv
import shutil
import os

# Définir la fenêtre principale
class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        # Titre de la fenêtre
        self.setWindowTitle("Traducteur")

        self.box = QHBoxLayout()

        self.box1 = QVBoxLayout()
        self.box.addLayout(self.box1)

        self.box2 = QVBoxLayout()
        self.box.addLayout(self.box2)

        # Contenu de la fenêtre principale
        self.francais = QLabel("Français")
        self.francais.setAlignment(Qt.AlignCenter)
        self.francais.setStyleSheet("background-color: #B3D9F1; font-size: 20px")
        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("font-size: 20px")
        self.textEdit.setText("")
        self.valider = QPushButton('Valider')
        self.valider.clicked.connect(self.keyPressEvent)

        self.box1.addWidget(self.francais)
        self.box1.addWidget(self.textEdit)
        self.box1.addWidget(self.valider)

        self.anglais = QLabel("Anglais")
        self.anglais.setAlignment(Qt.AlignCenter)
        self.anglais.setStyleSheet("background-color: #B3D9F1;font-size: 20px")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 20px")
        self.box2.addWidget(self.anglais)
        self.box2.addWidget(self.textEdit1)
        self.textEdit1.setText("")

        self.reverse = QPushButton('Inverse')
        self.box2.addWidget(self.reverse)

        self.ajout = QPushButton('Ajouter un mot dans le dictionnaire')
        self.box1.addWidget(self.ajout)
        self.ajout.clicked.connect(self.ajout_mot)

        self.ajout1 = QPushButton('Ajouter un fichier dans le dictionnaire')
        self.box2.addWidget(self.ajout1)
        self.ajout1.clicked.connect(self.ajout_fichier)


        self.widget = QWidget()
        self.widget.setLayout(self.box)
        self.setCentralWidget(self.widget)

    def keyPressEvent(self):
        mot_francais = self.textEdit.toPlainText()
        print(mot_francais)
        self.textEdit1.setText(mot_francais)

    def ajout_mot(self):
        self.fenetre2 = Fenetre2()
        self.fenetre2.show()

    def ajout_fichier(self):
        self.boite = QFileDialog()
        self.chemin = self.boite.getOpenFileName(parent = None, caption = 'Ouvrir fichier',filter ='Fichiers CSV (*.csv)')
        self.list = self.chemin[0].split("/")
        chemin_du_script = os.getcwd()
        shutil.copy(self.chemin[0], chemin_du_script)
        if self.chemin[0]:
            # Extraire le nom du fichier et l'afficher
            list_chemin = self.chemin[0].split("/")
            # Ouvrir le fichier CSV et lire la première ligne
            try:
                with open(list_chemin[-1], mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file,delimiter=';')
                    fichier = []
                    for row in reader:
                        fichier.append(tuple(row))
                    print(fichier)
                    self.fenetre=Fenetre_fichier()
                    self.fenetre.show()
                
            except Exception as e:
                self.fenetre=Fenetre_fichier()
                self.fenetre.show()
    
# Fenêtre pour ajouter un mot
class Fenetre2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajout")
        
        self.boite = QHBoxLayout()
    
        self.boite1 = QVBoxLayout()
        self.boite.addLayout(self.boite1)

        self.mot_francais = QLabel("Mot en français")
        self.mot_francais.setAlignment(Qt.AlignCenter)
        self.mot_anglais = QLabel("Mot en anglais")
        self.mot_anglais.setAlignment(Qt.AlignCenter)
        self.boite1.addWidget(self.mot_francais)
        self.boite1.addWidget(self.mot_anglais)

        self.boite2 = QVBoxLayout()
        self.boite.addLayout(self.boite2)

        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("font-size: 20px")
        self.textEdit.setFixedSize(300, 30)
        self.textEdit.setText("")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 20px")
        self.textEdit1.setFixedSize(300, 30)
        self.textEdit1.setText("")

        self.boite2.addWidget(self.textEdit)
        self.boite2.addWidget(self.textEdit1)

        self.valider = QPushButton('Valider')
        self.valider.clicked.connect(self.ajout)
        self.boite.addWidget(self.valider)

        self.setLayout(self.boite)

    def ajout(self):
        mot_francais = self.textEdit.toPlainText()
        mot_anglais = self.textEdit1.toPlainText()
        print((mot_francais,mot_anglais))

#Fenetre de validation de téléchargement
class Fenetre_fichier(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validation du téléchargement")
        self.resize(300,100)
    
        self.label=QLabel(" Votre fichier a bien été ajouté au dictionnaire ",self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(20,40)

#Fenetre message d'erreur de téléchargement
class Fenetre_erreur(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message d'erreur")
        self.resize(300,100)
    
        self.label=QLabel("Erreur lors de l'ouverture du fichier",self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(20,40)



# Initialisation de l'application            
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Fenetre()
window.show()
app.exec_()