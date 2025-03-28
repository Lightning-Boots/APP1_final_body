# représenter un élément individuel de l'arbre,c'est à dire un tuple (mot_fr , mot_ang)
import csv
import random
import sys
import chardet
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog,QHBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtGui import QIcon
import csv
import shutil
import os

class Noeud:
    def __init__(self, tuples_mots):
        self.mot= tuples_mots
        self.enfant_gauche = None
        self.enfant_droite = None
    
    def get_fils_gauche(self):
        return self.enfant_gauche
    
    def get_fils_droite(self):
        return self.enfant_droite
    
    def get_etiquette(self):
        return self.mot
    
    def get_traduction(self):
        return self.traduction

class ArbreBinaire:
    def __init__(self):
        self.racine = None
        self.langue = None
        
    def est_vide(self):
        return self.racine is None
 
    def est_feuille(self, noeud):
        return noeud is not None and noeud.enfant_gauche is None and noeud.enfant_droite is None
    
    def hauteur_arbre(self, noeud):
        if noeud is None:
            return 0
        if self.est_feuille(noeud):
            return 1
        return 1 + max(self.hauteur_arbre(noeud.enfant_gauche), self.hauteur_arbre(noeud.enfant_droite))
    
    def predecesseur(self, noeud):
        if noeud is None:
            return None
        predecesseur = None
        if noeud.enfant_gauche:
            predecesseur = noeud.enfant_gauche
            while predecesseur.enfant_droite:
                predecesseur = predecesseur.enfant_droite
            return predecesseur.mot[0]
    
    def successeur(self, noeud):
        if noeud is None:
            return None
        successeur = None
        if noeud.enfant_droite:
            successeur = noeud.enfant_droite
            while successeur.enfant_gauche:
                successeur = successeur.enfant_gauche
            return successeur.mot[0]

    
    def recherche_fr(self, noeud, mot):
        if noeud is None:
            return None
        if noeud.mot[0] == mot:
            return noeud
        elif mot < noeud.mot[0]:
            return self.recherche_fr(noeud.enfant_gauche, mot)
        else:
            return self.recherche_fr(noeud.enfant_droite, mot)


    def insertion(self, tuples_mots,langue):
        if langue == 'anglais':
            self.langue = 1
        if langue == 'français':
            self.langue = 0
        if self.racine is None:
            self.racine = Noeud(tuples_mots)
        else:
            self.insertion_rec(self.racine,tuples_mots, self.langue)

    def insertion_rec(self, noeud,  tuples_mots, langue):
        if  tuples_mots[langue] < noeud.mot[langue]:
            if noeud.enfant_gauche is None:
                noeud.enfant_gauche = Noeud(tuples_mots)
            else:
                self.insertion_rec(noeud.enfant_gauche, tuples_mots,langue)
        else:
            if noeud.enfant_droite is None:
                noeud.enfant_droite = Noeud(tuples_mots)
            else:
                self.insertion_rec(noeud.enfant_droite,tuples_mots,langue)

    def recherche_mot(self, mot, langue):
        if langue == 'anglais':
            self.langue = 1
        if langue == 'français':
            self.langue = 0
        return self.recherche_mot_rec(self.racine, mot,self.langue)

    def recherche_mot_rec(self, noeud, mot,langue):
        if noeud is None:
            return None
        if noeud.mot[langue] == mot:
            return noeud.mot[1-langue]
        elif mot < noeud.mot[langue]:
            return self.recherche_mot_rec(noeud.enfant_gauche, mot,langue)
        else:
            return self.recherche_mot_rec(noeud.enfant_droite, mot, langue)


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
def detecter_encodage(nom_fichier):
    """ Détecte automatiquement l'encodage du fichier """
    with open(f"App2\{nom_fichier}", 'rb') as f:
        resultat = chardet.detect(f.read())
    return resultat['encoding']

def ouverture_fichier(nom_fichier):
    """ Ouvre un fichier CSV peu importe son encodage """
    encodage = detecter_encodage(nom_fichier)
    print(f"Encodage détecté : {encodage}")

    with open(f"App2\{nom_fichier}", newline='', encoding=encodage, errors="replace") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        fichier = []
        for row in reader:
            if len(row) == 2:
                fichier.append(tuple(row))
            else:
                print(f"Ligne ignorée (mal formatée) : {row}")
    return fichier

def creation_arbre_aleatoire(langue):
    arbre=ArbreBinaire()
    liste_mot= ouverture_fichier("test_APP2.csv")
    while len(liste_mot) > 0: 
        if len(liste_mot) > 1:
            nb_aleatoire = random.randint(0, len(liste_mot) - 1)  # Plage corrigée
        else:
            nb_aleatoire = 0 
        mot=liste_mot[nb_aleatoire]
        arbre.insertion(mot,langue)
        liste_mot.pop(nb_aleatoire)
    arbre.enregistrer_arbre()

def construire_arbre_recursif(liste, arbre, langue):
    if not liste:
        return

    milieu = len(liste) // 2
    arbre.insertion(liste[milieu],langue)
    #print(liste[milieu])

    # On répète pour les sous-listes gauche et droite
    construire_arbre_recursif(liste[:milieu], arbre,langue)
    construire_arbre_recursif(liste[milieu+1:], arbre,langue)

def creation_arbre_complet(nom_fichier,langue):
    arbre = ArbreBinaire()
    liste_mot = ouverture_fichier(nom_fichier)

    # Trie la liste si nécessaire pour avoir un arbre équilibré
    liste_mot.sort()

    construire_arbre_recursif(liste_mot, arbre,langue)

    #arbre.enregistrer_arbre()
    return arbre

# TEST
arbre=ArbreBinaire()
arbre.insertion(("m","m"),"français")
arbre.insertion(("g","g"),"français")
arbre.insertion(("h","h"),"français")
arbre.insertion(("i","i"),"français")
arbre.insertion(("v","v"),"français")
arbre.insertion(("x","x"),"français")
arbre.insertion(("c","c"),"français")
arbre.insertion(("b","b"),"français")
arbre.insertion(("d","d"),"français")
print('affichage successeur et predecesseur')
print(arbre.successeur(arbre.recherche_fr(arbre.racine,"g")))
print(arbre.predecesseur(arbre.recherche_fr(arbre.racine,"g")))

arbre_fr_to_en = creation_arbre_complet('Trad-final.csv','français')
arbre_en_to_fr = creation_arbre_complet('Trad-final.csv','anglais')


# Définir la fenêtre principale
class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        # Titre de la fenêtre
        self.setWindowTitle("Traducteur")

        self.box = QVBoxLayout()

        self.box1 = QHBoxLayout()
        self.box.addLayout(self.box1)

        self.box2 = QHBoxLayout()
        self.box.addLayout(self.box2)

        self.box3 = QHBoxLayout()
        self.box.addLayout(self.box3)

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
        self.box2.addWidget(self.textEdit)
        self.box3.addWidget(self.valider)

        self.reverse = QPushButton()
        self.reverse.clicked.connect(self.inverser)
        self.reverse.setFixedSize(30, 30)
        self.reverse.setIcon(QIcon("App2/fleche.png"))
        self.reverse.setIconSize(QSize(30,30))
        self.box1.addWidget(self.reverse)
        
        self.sup = QPushButton ('Supprimer')
        self.box3.addWidget(self.sup)


        self.anglais = QLabel("Anglais")
        self.anglais.setAlignment(Qt.AlignCenter)
        self.anglais.setStyleSheet("background-color: #B3D9F1;font-size: 20px")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 20px")
        self.textEdit1.setReadOnly(True)
        self.box1.addWidget(self.anglais)
        self.box2.addWidget(self.textEdit1)
        self.textEdit1.setText("")

        
        self.ajout = QPushButton('Ajouter un mot dans le dictionnaire')
        self.box3.addWidget(self.ajout)
        self.ajout.clicked.connect(self.ajout_mot)

        self.ajout1 = QPushButton('Ajouter un fichier dans le dictionnaire')
        self.box3.addWidget(self.ajout1)
        self.ajout1.clicked.connect(self.ajout_fichier)

        self.test1 = QPushButton('Test')
        self.box3.addWidget(self.test1)
        self.test1.clicked.connect(self.test)


        self.widget = QWidget()
        self.widget.setLayout(self.box)
        self.setCentralWidget(self.widget)

    def inverser(self):
        textval1 =  self.francais.text()
        textval2 =  self.anglais.text()
        self.francais.setText(textval2)
        self.anglais.setText(textval1)

    def keyPressEvent(self):
        langue = self.francais.text().lower()
        arbre = None
        if langue =='français':
            arbre = arbre_fr_to_en
        if langue == 'anglais':
            arbre = arbre_en_to_fr
        mot= self.textEdit.toPlainText()
        trad = arbre.recherche_mot(mot,langue)
        print(mot,trad)
        self.textEdit1.setText(trad)

    def ajout_mot(self):
        texte_francais = self.francais.text()
        self.fenetre2 = Fenetre2(texte_francais)
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
                self.fenetre=Fenetre_erreur()
                self.fenetre.show()

    def test(self):
        self.fenetre=Fenetre_test()
        self.fenetre.show()


class Fenetre_test(QWidget):
    def __init__(self):
        super().__init__()
        self.mot="juste"
        self.hauteur = arbre_fr_to_en.hauteur_arbre( arbre_fr_to_en.racine)
        self.noeud_arbre = arbre_fr_to_en.recherche_fr(arbre_fr_to_en.racine,self.mot)
        self.predecesseur = arbre_fr_to_en.predecesseur(self.noeud_arbre)
        self.succeseur = arbre_fr_to_en.successeur(self.noeud_arbre)
        self.fils_gauche = self.noeud_arbre.get_fils_gauche()
        if self.fils_gauche != None:
            self.fils_gauche=self.fils_gauche.mot[0]
        self.fils_droite = self.noeud_arbre.get_fils_droite()
        if self.fils_droite != None:
            self.fils_droite=self.fils_droite.mot[0]

        self.box=QVBoxLayout()

        self.label=QLabel(f"Hauteur : {self.hauteur}")
        self.label5=QLabel(f"Mot étudié : {self.mot}")
        self.label1=QLabel(f"Prédecesseur: {self.predecesseur}")
        self.label2=QLabel(f"Succeseur : {self.succeseur}")
        self.label3=QLabel(f"Fils gauche : {self.fils_gauche}")
        self.label4=QLabel(f"Fils droite : {self.fils_droite}")

        self.box.addWidget(self.label)
        self.box.addWidget(self.label5)
        self.box.addWidget(self.label1)
        self.box.addWidget(self.label2)
        self.box.addWidget(self.label3)
        self.box.addWidget(self.label4)
        
       
        self.setLayout(self.box)



# Fenêtre pour ajouter un mot
class Fenetre2(QWidget):
    def __init__(self,langue):
        super().__init__()
        self.setWindowTitle("Ajout")
        self.langue=langue

        self.boite = QVBoxLayout()

        self.boite1 = QHBoxLayout()
        self.boite.addLayout(self.boite1)

        self.boite2 = QHBoxLayout()
        self.boite.addLayout(self.boite2)

        self.mot_francais = QLabel("Mot en français:")
        self.mot_francais.setStyleSheet("font-size: 16px")
        self.mot_francais.setAlignment(Qt.AlignCenter)
        self.mot_anglais = QLabel("Mot en anglais:")
        self.mot_anglais.setStyleSheet("font-size: 16px")
        self.mot_anglais.setAlignment(Qt.AlignCenter)
        self.boite1.addWidget(self.mot_francais)
        self.boite2.addWidget(self.mot_anglais)

        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("font-size: 16px")
        self.textEdit.setFixedSize(300, 30)
        self.textEdit.setText("")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 16px")
        self.textEdit1.setFixedSize(300, 30)
        self.textEdit1.setText("")

        self.boite1.addWidget(self.textEdit)
        self.boite2.addWidget(self.textEdit1)

        self.valider = QPushButton('Valider')
        self.valider.clicked.connect(self.ajout)
        self.boite.addWidget(self.valider)

        self.setLayout(self.boite)

    def ajout(self):
        mot= self.textEdit.toPlainText()
        recherche =arbre_fr_to_en.recherche_mot(mot,self.langue.lower())
        if recherche == None:
            mot_francais = self.textEdit.toPlainText()
            mot_anglais = self.textEdit1.toPlainText()
            arbre_fr_to_en.insertion((mot_francais,mot_anglais),"français")
            arbre_en_to_fr.insertion((mot_francais,mot_anglais),"anglais")
            self.close()
        else:
            self.label=QLabel("Ce mot est déjà dans le dictionnaire")
            self.label.setStyleSheet("font-size: 16px; color: red;")
            self.boite.addWidget(self.label)
        

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