import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

import Fenêtre_principale as Fenêtre_principale
from Fenêtre_principale import nombre_allumette, Coup_max, IA

import Graphique as Graphique









app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)