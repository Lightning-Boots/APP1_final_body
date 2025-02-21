import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import Qt, QCoreApplication 
class Fenetre(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Bouto's") 
        self.button = QPushButton("IA gagnante") 
        self.button.clicked.connect(self.onClick)
        self.button2 = QPushButton("IA aléatoire") 
        self.button2.clicked.connect(self.onClick)  



        self.layout = QGridLayout() 
        self.layout.addWidget(self.button,0,0) 
        self.layout.addWidget(self.button2,0,1) 

        self.widget = QWidget() 
        self.widget.setLayout(self.layout) 
        self.setCentralWidget(self.widget)


    def onClick(self): 
        print("clic!") 
app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)
 
window = Fenetre() 
window.show() 
app.exec_()