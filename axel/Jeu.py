import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

import axel.Fenêtre_principale as Fenêtre_principale
from axel.Fenêtre_principale import nombre_allumette, Coup_max, IA

import axel.Graphique as Graphique









app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)