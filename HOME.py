import sys
#from PyQt6 import uic
from PyQt6 import uic,QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        uic.loadUi("home.ui", self)
        widget.setWindowTitle("Home")
        self.btn_1.clicked.connect(self.gotoLinAlg)
        self.btn_2.clicked.connect(self.gotoStat)

    def gotoLinAlg(self):
        from uintf import Eig
        eqsol = Eig()
        widget.addWidget(eqsol)
        widget.setWindowTitle("Matrices")
        widget.setCurrentIndex(widget.currentIndex() + 1)
        eqsol.home.clicked.connect(self.__init__)
        eqsol.home.clicked.connect(lambda: widget.addWidget(home))
        eqsol.home.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() + 1))

    def gotoStat(self):
        from statTab import Stat
        stat = Stat()
        widget.addWidget(stat)
        widget.setWindowTitle("Data Analysis")
        widget.setCurrentIndex(widget.currentIndex() + 1)
        stat.home.clicked.connect(self.__init__)
        stat.home.clicked.connect(lambda: widget.addWidget(home))
        stat.home.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() + 1))



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
home = HomeScreen()
widget.addWidget(home)

widget.setGeometry(44, 24, 790, 700)
widget.show()
app.exec()
