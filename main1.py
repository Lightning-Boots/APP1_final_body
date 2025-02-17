import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QMovie, QColor, QPainter, QBrush, QPen, QPalette 
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtCore
# On passe une liste vide en argument 
# On crée notre fenêtre !


class Color(QWidget): 
    def __init__(self, color): 
        super().__init__() 
        self.setAutoFillBackground(True) 
        self.myPalette = self.palette() 
        self.myPalette.setColor(QPalette.Window, QColor(color)) 
        self.setPalette(self.myPalette)

class MainWindow(QMainWindow):

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


        self.label = [QLabel(self) for i in range(n)]
        self.labels = QHBoxLayout()
        self.labels.setSpacing(0)0
        self.movie = QMovie("vibe-cat.gif")

        for i in range(len(self.label)):
            self.label[i].setMovie(self.movie)
            self.label[i].setScaledContents(True)
            self.labels.addWidget(self.label[i])


        self.block = QHBoxLayout()
        self.block.addWidget(Color('blue'))
        
        
        self.movie.start()
        self.setLayout(self.labels)
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))

        self.rect = QHBoxLayout() 
        self.rect.addWidget(Color('gray')) 
        self.rect.setSpacing(0)
        self.widget = QWidget() 
        self.widget.setLayout(self.rect)
        self.setCentralWidget(self.widget)



    #painter.drawRect(0, 0, self.width(), self.height() // 3 + 40)


    def resizeEvent(self, event):
        self.labels.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()//3))
        self.text.setGeometry(0, self.height()//2, self.width(), 73)
        py = (self.width()**2 + self.height()**2)**(1/2) //30
        py = int(py)
        self.text.setStyleSheet("color: white; font-size : " + str(py) + "px; background-color: none") 

n = 20

def main ():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()