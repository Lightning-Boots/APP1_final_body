import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout,QWidget
from PyQt5.QtGui import QPixmap, QMovie, QColor, QPainter, QBrush, QPen, QPalette 
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
# On passe une liste vide en argument 
# On crée notre fenêtre !



class Jeu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(700, 300, 1000, 500)




        self.text = QLabel(self)
        self.text.setText("Nombre de Bâton : " + str(n))
        self.text.setGeometry(0, self.height()//2, self.width(), 73)
        self.text.setStyleSheet("color: white; font-size : 25px; background-color: none")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.band = QWidget(self)
        self.band.setStyleSheet("background-color: grey;")
        self.rect = QHBoxLayout(self.band)
        self.rect.setSpacing(0)
        self.band.setGeometry(0, 0, self.width(), self.height() // 3+40)


        self.label = [QLabel(self) for i in range(n)]
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
        self.text.setGeometry(0, self.height()//2, self.width(), 73)
        py = (self.width()**2 + self.height()**2)**(1/2) //30
        py = int(py)
        self.text.setStyleSheet("color: white; font-size : " + str(py) + "px; background-color: none") 

n = 10

app = QCoreApplication.instance() 
if app is None: 
    app = QApplication(sys.argv)


fenetre = Jeu()
fenetre.show()

app.exec_()