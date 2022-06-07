import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import random
from numpy.linalg import eig
import numpy as np

stylesheet = """QPushButton:hover:!pressed{background-color:yellow; color:black;
border-radius:10px;
text-align: center;
font-weight: bold;
font: 75 15pt "Tahoma";
}
QPushButton {background-color:#ff0057;
color:white;
border-radius:10px;
text-align: center;
font-weight: bold;
font: 75 15pt "Tahoma";}

QPushButton:disabled {
        background: transparent #e5e9ee;
        color: black;
}
"""


class Eig(QDialog):
    def __init__(self):
        super(Eig, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.gui()

    def gui(self):
        self.calc.clicked.connect(self.compute)
        self.calc.setStyleSheet(stylesheet)
        self.CLEAR.clicked.connect(self.clear)
        self.CLEAR.setStyleSheet(stylesheet)
        self.rndm.clicked.connect(self.randomize)
        self.rndm.setStyleSheet(stylesheet)
        self.clear()

    def compute(self):
        strr = " "
        try:
            arr = np.array([[float(self.a1.text()), float(self.b1.text()), float(self.c1.text())],
                           [float(self.a2.text()), float(self.b2.text()), float(self.c2.text())],
                           [float(self.a3.text()), float(self.b3.text()), float(self.c3.text())] ] )
            v,vc = eig(arr)
            strr = "eigen values: "+ str(np.round(v[0])) + ' , ' + str(np.round(v[1])) + ' , ' +str(np.round(v[2]))
            strr += "\nEigenvectors: " + str(np.around(vc[:,0])) +'ᵀ\n' + str(np.around(vc[:,1])) + 'ᵀ\n' + str(np.around(vc[:,2])) +'ᵀ'
        except:
            strr += "you entered nonnumbers"
        finally:
            self.result.setStyleSheet("background-color:black; color:white; font: 75  18pt \"Consolas\" ")
            self.result.setText(strr)

    def clear(self):
        var = [self.a1,self.b1,self.c1,self.a2,self.b2,self.c2,self.a3,self.b3,self.c3]
        for i in var:
            i.setText('0')

    def randomize(self):
        var = [self.a1,self.b1,self.c1,self.a2,self.b2,self.c2,self.a3,self.b3,self.c3]
        for i in var:
            i.setText(str(round(random.random()*10)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Eig()
    # widget.resize(400, 200)
    #widget.setWindowIcon()
    widget.setWindowTitle("EigenValues")

    widget.show()
    sys.exit(app.exec())
