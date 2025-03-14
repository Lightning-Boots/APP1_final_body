import csv

# Lecture du fichier csv contenant la banque de données de mots traduits

def ouverture_fichier(nom_fichier):
    with open(nom_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=';')
        fichier = []
        for row in reader:
            fichier.append(tuple(row))
    return fichier

print(ouverture_fichier('trad.csv'))
# Création de l'arbre binaire 

class ArbreBinaire:
   def __init__(self, valeur):
      self.valeur = valeur
      self.enfant_gauche = None
      self.enfant_droit = None

   def insert_gauche(self, valeur):
      if self.enfant_gauche == None:
         self.enfant_gauche = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_gauche = self.enfant_gauche
         self.enfant_gauche = new_node

   def insert_droit(self, valeur):
      if self.enfant_droit == None:
         self.enfant_droit = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_droit = self.enfant_droit
         self.enfant_droit = new_node

   def get_valeur(self):
      return self.valeur

   def get_gauche(self):
      return self.enfant_gauche

   def get_droit(self):
      return self.enfant_droit


def creer_arbre_fr_to_eng(fichier):
   liste = ouverture_fichier(fichier)
   arbre = ArbreBinaire(liste[len(fichier)//2])
   
      
