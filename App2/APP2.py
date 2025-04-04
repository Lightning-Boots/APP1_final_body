
# Importations
import csv
import random
import sys
import chardet
import shutil
import os
import pickle

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog,QHBoxLayout, QRadioButton
from PyQt5.QtCore import QCoreApplication, Qt, QSize, QSettings
from PyQt5.QtGui import QIcon

# Nous avons stockés nos données (3000 mots) sous formes de 2 arbres implémentés en programmation orienté objet

# Une première classe Noeud qui sert à définir les noeuds de l'arbre qui sont un tuple de mot (mot_francais, mot_anglais)
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
   
    def get_traduction_fr_to_en(self):
        return self.mot[1]
    
    def get_traduction_en_to_fr(self):
        return self.mot[0]
    
# Une deuxième classe ArbreBinaire qui va permettre de définir nos 2 arbres et faire appel à différentes fonctions classiques des arbres binaires de recherche
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
   
    def rechercher(self, noeud, mot,langue): # Retourne le noeud dont le mot est passé en paramètre selon la langue de celui-ci
        if langue == 'anglais':
            self.langue = 1
        if langue == 'français':
            self.langue = 0

        if noeud is None:
            return None
        if noeud.mot[self.langue] == mot:
            return noeud
        elif mot < noeud.mot[self.langue]:
            return self.rechercher(noeud.enfant_gauche, mot,langue)
        else:
            return self.rechercher(noeud.enfant_droite, mot,langue)
 
    def insertion(self, tuples_mots,langue): # Insertion s'appuie sur insertion_rec pour inserérer un nouveau noeud
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
 
    def recherche_mot(self, mot, langue): # Recherche_mot s'appuie sur rechercher_mot_rec et renvoie la traduction du mot recherché
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
        
    def parent(self, noeud, mot): # Trouve le parent d'un noeud (sert pour la fonction supprimer)
        if isinstance(mot, tuple):
            mot = mot[0]
        if noeud is None or (noeud.enfant_gauche is None and noeud.enfant_droite is None):
            return None
        if (noeud.enfant_gauche and noeud.enfant_gauche.mot[0] == mot) or \
        (noeud.enfant_droite and noeud.enfant_droite.mot[0] == mot):
            return noeud
        print(mot, noeud.mot[0])
        if mot < noeud.mot[0]:
            return self.parent(noeud.enfant_gauche, mot)
        else:
            return self.parent(noeud.enfant_droite, mot)

    def rechercheMax(self, noeud): # Trouve le plus grand noeud du sous-arbre (sert pour la fonction supprimer)
        while noeud.enfant_droite is not None:
            noeud = noeud.enfant_droite
        return noeud
    
    def supprimer(self, nom,langue):

        # on commence par rechercher le noeud à supprimer
        noeud = self.rechercher(self.racine, nom,langue) 
        if noeud is None:
            print(f"Le noeud '{nom}' n'existe pas dans l'arbre")
            return  sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl"),sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl") 

        # on trouve le parent du noeud
        parent_noeud = self.parent(self.racine, nom)  

        # cas 1 : le noeud est une feuille 
        if noeud.enfant_gauche is None and noeud.enfant_droite is None:
            if parent_noeud:
                if parent_noeud.enfant_gauche == noeud:
                    parent_noeud.enfant_gauche = None
                else:
                    parent_noeud.enfant_droite = None
            else:  
                self.racine = None
            print(f"Le noeud '{nom}' a été supprimé")
            return  sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl"),sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")

        # cas 2 : le noeud est un enfant unique
        elif noeud.enfant_gauche is None or noeud.enfant_droite is None:
            enfant = noeud.enfant_gauche if noeud.enfant_gauche else noeud.enfant_droite
            if parent_noeud:
                if parent_noeud.enfant_gauche == noeud:
                    parent_noeud.enfant_gauche = enfant
                else:
                    parent_noeud.enfant_droite = enfant
            else:  
                self.racine = enfant
            print(f"Le noeud '{nom}' a été supprimé")
            return sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl"),sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")

        # cas 3 : on a deux enfants, on remplace donc par le plus grand noeud du sous-arbre gauche
        else:
            noeud_max = self.rechercheMax(noeud.enfant_gauche)
            parent_max = self.parent(noeud, noeud_max.mot)

            # on remplace les valeurs du noeud supprimé par celles du max du sous-arbre gauche 
            noeud.mot = noeud_max.mot

            # on supprime le noeud max, qui est toujours présent dans l'arbre mais sans le double lien 
            if parent_max:
                if parent_max.enfant_droite == noeud_max:
                    parent_max.enfant_droite = noeud_max.enfant_gauche
                else:
                    parent_max.enfant_gauche = noeud_max.enfant_gauche
            else:
                noeud.enfant_gauche = noeud_max.enfant_gauche  
            print(f"Le noeud '{nom}' a été supprimé et remplacé par '{noeud_max.mot}'")

    def modifier_traduction(self, arbre_francais_en_anglais, arbre_anglais_en_francais, mot_francais, mot_anglais):

        # vérifie si le mot existe dans l'arbre francais
        ancienne_traduction = arbre_francais_en_anglais.recherche_mot(mot_francais, "français")
        if ancienne_traduction is not None:

            # on supprime l'ancienne paire de traduction, avant de la remplacer
            arbre_francais_en_anglais.supprimer(mot_francais, "français")
            arbre_anglais_en_francais.supprimer(ancienne_traduction, "anglais")

            # on vient insérer la nouvelle traduction du mot
            arbre_francais_en_anglais.insertion((mot_francais, mot_anglais), "français")
            arbre_anglais_en_francais.insertion((mot_francais, mot_anglais), "anglais")

            sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl")
            sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")

            return f"Traduction de '{mot_francais}' mise à jour : '{ancienne_traduction}' -> '{mot_anglais}'"
        
        ancienne_traduction = arbre_anglais_en_francais.recherche_mot(mot_anglais, "anglais")
        if ancienne_traduction is not None:

            # on supprime l'ancienne paire de traduction, avant de la remplacer
            arbre_anglais_en_francais.supprimer(mot_anglais, "anglais")
            arbre_francais_en_anglais.supprimer(ancienne_traduction, "français")

            # on vient insérer la nouvelle traduction du mot
            arbre_francais_en_anglais.insertion((mot_francais, mot_anglais), "français")
            arbre_anglais_en_francais.insertion((mot_francais, mot_anglais), "anglais")

            
            sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl")
            sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")

            return f"Traduction de '{mot_anglais}' mise à jour : '{ancienne_traduction}' -> '{mot_francais}'"



 
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

    def exporter_liste(self, noeud=None):
        if noeud is None:
            noeud = self.racine
        if noeud is None:
            return []
        
        # Parcours en ordre infixe (gauche → racine → droite)
        return self.exporter_liste(noeud.enfant_gauche) + [noeud.mot] + self.exporter_liste(noeud.enfant_droite)
    

 
#Fonctions servants à la création des arbres
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
 
def creation_arbre_aleatoire(langue): # Premiere version où les mots étaient ajoutés aléatoirements
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
 
def construire_arbre_recursif(liste, arbre, langue): # Construit l'arbre de maniere à ce que les noeuds soient le mieux répartis possibles
    if not liste:
        return
 
    milieu = len(liste) // 2
    arbre.insertion(liste[milieu],langue)
    #print(liste[milieu])
 
    # On répète pour les sous-listes gauche et droite
    construire_arbre_recursif(liste[:milieu], arbre,langue)
    construire_arbre_recursif(liste[milieu+1:], arbre,langue)
 
def creation_arbre_complet(nom_fichier,langue): # Avec les fonctions précédentes, créer l'arbre à partir d'un fichier
    arbre = ArbreBinaire()
    liste_mot = ouverture_fichier(nom_fichier)
 
    # Trie la liste si nécessaire pour avoir un arbre équilibré
    liste_mot.sort()
 
    construire_arbre_recursif(liste_mot, arbre,langue)
 
    #arbre.enregistrer_arbre()
    return arbre
 
def sauvegarder_arbre(arbre, nom_fichier): # Sauvegarde les arbres de manière persistante
    with open(nom_fichier, "wb") as f:
        pickle.dump(arbre, f)

def charger_arbre(nom_fichier):
    try:
        with open(nom_fichier, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return ArbreBinaire()

# Création/Chargement des deux arbres
# Un arbre où les mots sont classés selon le français et l'autre selon l'anglais

arbre_fr_to_en = charger_arbre("arbre_fr_to_en.pkl")
if arbre_fr_to_en.est_vide():
    arbre_fr_to_en = creation_arbre_complet('Trad-final.csv', 'français')

arbre_en_to_fr = charger_arbre("arbre_en_to_fr.pkl")
if arbre_en_to_fr.est_vide():
    arbre_en_to_fr = creation_arbre_complet('Trad-final.csv', 'anglais')

sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl")
sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")

# JEU DE TESTS DEMANDE
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
print(arbre.successeur(arbre.rechercher(arbre.racine,"g",'français')))
print(arbre.predecesseur(arbre.rechercher(arbre.racine,"g",'français')))
 
# Définir la fenêtre principale
class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        # Titre de la fenêtre
        self.setWindowTitle("Traducteur")

        self.configuration = QSettings('APP','Coffre',self) 
        self.valeur = self.configuration.value('test')
        #self.configuration.setValue('test', "")
 
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
        self.valider.clicked.connect(self.traduire)
 
        self.box1.addWidget(self.francais)
        self.box2.addWidget(self.textEdit)
        self.box3.addWidget(self.valider)
 
        self.reverse = QPushButton()
        self.reverse.clicked.connect(self.inverser)
        self.reverse.setFixedSize(30, 30)
        self.reverse.setIcon(QIcon("App2/fleche.png"))
        self.reverse.setIconSize(QSize(30,30))
        self.box1.addWidget(self.reverse)
       
 
        self.anglais = QLabel("Anglais")
        self.anglais.setAlignment(Qt.AlignCenter)
        self.anglais.setStyleSheet("background-color: #B3D9F1;font-size: 20px")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 20px")
        self.textEdit1.setReadOnly(True)
        self.box1.addWidget(self.anglais)
        self.box2.addWidget(self.textEdit1)
        self.textEdit1.setText("")
 
       
        self.ajout = QPushButton('Ajouter/Modifier un mot dans le dictionnaire')
        self.box3.addWidget(self.ajout)
        self.ajout.clicked.connect(self.ajout_mot)
 
        self.ajout1 = QPushButton('Ajouter un fichier dans le dictionnaire')
        self.box3.addWidget(self.ajout1)
        self.ajout1.clicked.connect(self.ajout_fichier)

        self.supp = QPushButton('Supprimer un mot dans le dictionnaire')
        self.box3.addWidget(self.supp)
        self.supp.clicked.connect(self.supp_mot)
 
        self.test1 = QPushButton('Infos')
        self.box3.addWidget(self.test1)
        self.test1.clicked.connect(self.test)
 
 
        self.widget = QWidget()
        self.widget.setLayout(self.box)
        self.setCentralWidget(self.widget)
 
    def inverser(self): #Change le sens de traduction
        textval1 =  self.francais.text()
        textval2 =  self.anglais.text()
        self.francais.setText(textval2)
        self.anglais.setText(textval1)
 
    def traduire(self):
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

    def supp_mot(self):
        texte_francais = self.francais.text()
        self.fenetre2 = Fenetre3(texte_francais)
        self.fenetre2.show()
 
    def ajout_fichier(self):
        self.boite = QFileDialog()
        self.chemin = self.boite.getOpenFileName(parent = None, caption = 'Ouvrir fichier',filter ='Fichiers CSV (*.csv)')
        self.list = self.chemin[0].split("/")
        chemin_du_script = os.getcwd()
        if self.chemin[0]:
            # Extraire le nom du fichier et l'afficher
            list_chemin = self.chemin[0].split("/")
            if list_chemin[-1] in self.valeur:
                self.fenetre = Fenetre_erreur()
                return self.fenetre.show()
            else:
                self.configuration.setValue('test', str(self.valeur) + " " + str(list_chemin[-1])) 
            shutil.copy(self.chemin[0], chemin_du_script)
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
 
    def test(self):
        langue = self.francais.text().lower()
        arbre = None
        if langue =='français':
            arbre = arbre_fr_to_en
        if langue == 'anglais':
            arbre = arbre_en_to_fr
        mot = self.textEdit.toPlainText()  # Récupérer le mot saisi
        self.fenetre = Fenetre_test(mot, arbre, langue)   # Passer le mot en argument
        self.fenetre.show()
 
# Fentre qui affiche les informations du mot écrit dans l'entrée texte
class Fenetre_test(QWidget):
    def __init__(self, mot, arbre, langue):
        super().__init__()
        self.mot = mot
        self.arbre = arbre
        self.langue = langue
        self.box = QVBoxLayout()  # Créer le layout ici

        # Chercher le mot dans l'arbre
        self.noeud_arbre = self.arbre.rechercher(self.arbre.racine, self.mot, self.langue)

        if self.noeud_arbre is None:  # Si le mot n'existe pas dans l'arbre
            self.label = QLabel(f"Le mot '{self.mot}' n'est pas dans l'arbre.")
            self.box.addWidget(self.label)
        else:
            self.hauteur = self.arbre.hauteur_arbre(self.arbre.racine)
            self.predecesseur = self.arbre.predecesseur(self.noeud_arbre)
            self.successeur = self.arbre.successeur(self.noeud_arbre)

            self.fils_gauche = self.noeud_arbre.get_fils_gauche()
            self.fils_gauche = self.fils_gauche.mot[0] if self.fils_gauche else "Aucun"

            self.fils_droite = self.noeud_arbre.get_fils_droite()
            self.fils_droite = self.fils_droite.mot[0] if self.fils_droite else "Aucun"

            # Ajouter les labels avec les infos de l'arbre
            self.box.addWidget(QLabel(f"Hauteur : {self.hauteur}"))
            self.box.addWidget(QLabel(f"Mot étudié : {self.mot}"))
            self.box.addWidget(QLabel(f"Prédecesseur : {self.predecesseur}"))
            self.box.addWidget(QLabel(f"Successeur : {self.successeur}"))
            self.box.addWidget(QLabel(f"Fils gauche : {self.fils_gauche}"))
            self.box.addWidget(QLabel(f"Fils droite : {self.fils_droite}"))

        self.setLayout(self.box)  # Appliquer le layout
 
 
# Fenêtre pour ajouter un mot ou le modifier
class Fenetre2(QWidget):
    def __init__(self,langue):
        super().__init__()
        self.setWindowTitle("Ajout/Modification")
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
        mot_francais = self.textEdit.toPlainText()
        recherche = arbre_fr_to_en.recherche_mot(mot_francais,'français')
        mot_anglais = self.textEdit1.toPlainText()
        recherche2 = arbre_en_to_fr.recherche_mot(mot_anglais,'anglais')

        if recherche is None and recherche2 is None:
            mot_francais = self.textEdit.toPlainText()
            mot_anglais = self.textEdit1.toPlainText()
            arbre_fr_to_en.insertion((mot_francais,mot_anglais),"français")
            arbre_en_to_fr.insertion((mot_francais,mot_anglais),"anglais")
            sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl")
            sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")
            self.label=QLabel(f"Le mot {mot_francais} a bien été ajouté dans le dictionnaire !")
            self.label.setStyleSheet("font-size: 16px;")
            self.boite.addWidget(self.label)
            self.close()
        else:
            message = arbre_en_to_fr.modifier_traduction(arbre_fr_to_en, arbre_en_to_fr, mot_francais, mot_anglais)
            self.label=QLabel(f"{message}")
            self.label.setStyleSheet("font-size: 16px;")
            self.boite.addWidget(self.label)
            self.close()

       
# Fenêtre pour supprimer un mot
class Fenetre3(QWidget):
    def __init__(self,langue):
        super().__init__()
        self.setWindowTitle("Supprimer")
        self.langue=langue
 
        self.boite = QVBoxLayout()
 
        self.boite1 = QHBoxLayout()
        self.boite.addLayout(self.boite1)
 
        self.boite2 = QHBoxLayout()
        self.boite.addLayout(self.boite2)

        self.mot1 = QLabel("Le mot à supprimer est :")
        self.mot1.setStyleSheet("font-size: 16px")
        self.mot1.setAlignment(Qt.AlignCenter)
        self.boite1.addWidget(self.mot1)

        self.button_fr = QRadioButton('français')
        self.boite1.addWidget(self.button_fr)
        self.button_en = QRadioButton('anglais')
        self.boite1.addWidget(self.button_en)
 
        self.mot = QLabel("Mot:")
        self.mot.setStyleSheet("font-size: 16px")
        self.mot.setAlignment(Qt.AlignCenter)
        self.boite2.addWidget(self.mot)
 
        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("font-size: 16px")
        self.textEdit.setFixedSize(300, 30)
        self.textEdit.setText("")
        self.textEdit1 = QTextEdit()
        self.textEdit1.setStyleSheet("font-size: 16px")
        self.textEdit1.setFixedSize(300, 30)
        self.textEdit1.setText("")
 
        self.boite2.addWidget(self.textEdit)
 
        self.valider = QPushButton('Valider')
        self.valider.clicked.connect(self.supprimer)
        self.boite.addWidget(self.valider)
 
        self.setLayout(self.boite)
 
    def supprimer(self):
        mot = self.textEdit.toPlainText()

        if self.button_fr.isChecked() :
            trad = arbre_fr_to_en.recherche_mot(mot,'français')
            arbre_fr_to_en.supprimer(mot,'français')
            arbre_en_to_fr.supprimer(trad,'anglais')

        if self.button_en.isChecked() :
            trad = arbre_en_to_fr.recherche_mot(mot,'anglais')
            arbre_en_to_fr.supprimer(mot,'anglais')
            arbre_fr_to_en.supprimer(trad,'français')

        sauvegarder_arbre(arbre_fr_to_en, "arbre_fr_to_en.pkl")
        sauvegarder_arbre(arbre_en_to_fr, "arbre_en_to_fr.pkl")


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
 
        self.label=QLabel("Erreur lors de l'ouverture du fichier : Le fichier a déjà été ouvert",self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(20,40)
 
 
 

# Initialisation de l'application            
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Fenetre()
window.show()
app.exec_()