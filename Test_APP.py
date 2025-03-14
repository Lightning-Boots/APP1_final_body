# représenter un élément individuel de l'arbre,c'est à dire un tuple (mot_fr , mot_ang)
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
        
#Création de l'arbre à partie de notre dossier CSV
        
# Création de l'arbre
arbre = ArbreBinaire()

# Insertion de mots avec leur traduction
arbre.insertion(("chat", "cat"))
arbre.insertion(("chien", "dog"))
arbre.insertion(("voiture", "car"))
arbre.insertion(("maison", "house"))
# Recherche de mots
print(arbre.recherche_mot("chat"))  
print(arbre.recherche_mot("voiture"))  
print(arbre.recherche_mot("arbre"))  

# Interface graphique

#Importations
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog,QHBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt



# Definir la fenetre
class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        #Titre de la Fenetre 
        self.setWindowTitle("Traducteur")

        self.box = QHBoxLayout()

        self.box1 = QVBoxLayout()
        self.box.addLayout(self.box1)

        self.box2 = QVBoxLayout()
        self.box.addLayout(self.box2)

        self.francais = QLabel("Français")
        self.francais.setAlignment(Qt.AlignCenter)
        self.francais.setStyleSheet("background-color: #B3D9F1; font-size: 20px")
        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("font-size: 20px")
        self.box1.addWidget(self.francais)
        self.box1.addWidget(self.textEdit)
        self.textEdit.setText("")
        #self.textEdit.textChanged.connect(self.keyPressEvent)
        
        self.anglais = QLabel("Anglais")
        self.anglais.setAlignment(Qt.AlignCenter)
        self.anglais.setStyleSheet("background-color: #B3D9F1;font-size: 20px")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 20px")
        self.box2.addWidget(self.anglais)
        self.box2.addWidget(self.textEdit1)
        self.textEdit1.setText("")
        #self.textEdit1.textChanged.connect(self.keyPressEvent)
        
        self.widget = QWidget()
        self.widget.setLayout(self.box)
        self.setCentralWidget(self.widget)
    
    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            mot_francais = self.textEdit.toPlainText()
            print(mot_francais)

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Fenetre()
window.show()
app.exec_()