import sys
from PyQt6 import uic
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from math import sqrt, pow

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
class Stat(QDialog):
    def __init__(self):
        super(Stat, self).__init__()
        uic.loadUi("statistics.ui", self)
        self.gui()

    def gui(self):

        self.mean.clicked.connect(self.calcmean)
        self.input.textChanged.connect(self.chn)
        self.mode.clicked.connect(self.calcmode)
        self.median.clicked.connect(self.calcmedian)
        self.range.clicked.connect(self.calcrange)
        self.stdev.clicked.connect(self.stndev)

        self.mean.setStyleSheet(stylesheet)
        self.median.setStyleSheet(stylesheet)
        self.range.setStyleSheet(stylesheet)
        self.mode.setStyleSheet(stylesheet)
        self.stdev.setStyleSheet(stylesheet)

    def chn(self):
        data = self.input.toPlainText()
        lst = []
        flag = True
        try:
            lst = list(map(str, data.split()))
            print(lst)
            self.error.setText("")
        except:
            flag = False
            self.error.setText("please enter numbers")

        for i in lst:
            try:
                if i == float(i):
                    pass
            except:
                lst.remove(i)
                flag = False
                self.error.setText("please enter numbers")

       # if not flag or data == "":
        #    self.mean.setEnabled(flag)
        #else:
         #   self.mean.setEnabled(flag)
        return lst

    def calcmean(self):
        print("mean function")
        lst = self.chn()
        print("mean functionw")
        res = 0
        for i in lst:
            res += float(i)
        res /= len(lst)
        print("mean is",res)
        self.result.setText(" mean is " + str(res))
        self.result.setStyleSheet("background-color:black; color:white; font: 75  18pt \"Consolas\" ")

        return res

    def calcmode(self):
        Lst = self.chn()
        tem = 0
        for i in range(len(Lst)):
            repeated = 1

            for j in range(i+1,len(Lst)):
                if Lst[i] == Lst[j]:
                    repeated +=1
                    print(Lst[i],repeated)
            if repeated > 1 and repeated >= tem:
                target= str(Lst[i])
                tem = repeated
            #else:
             #   target = "none"
        if tem <1:
            target = "none"
        self.result.setText(" mode is " + target + " repeated: "+ str(tem) +" times")
        self.result.setStyleSheet("background-color:black; color:white; font: 75  18pt \"Consolas\" ")

    def calcmedian(self):
        list = self.chn()
        if len(list) % 2!=0:
            median = list[len(list) // 2]
            index = "\n index no." + str(len(list)//2)
        else:
            median =( float(list[len(list) // 2]) + float(list[(len(list) // 2) - 1]) )/ 2
            index = "\n indexes no." + str((len(list) // 2) - 1) + "," + str(len(list) // 2)
        self.result.setText(" median is " + str(median) + index)
        self.result.setStyleSheet("background-color:black; color:white; font: 75  18pt \"Consolas\" ")

    def calcrange(self):
        list = self.chn()
        self.result.setText(" range is " + str(float(max(list)) - float(min(list)) ))
        self.result.setStyleSheet("background-color:black; color:white; font: 75  18pt \"Consolas\" ")

    def stndev(self):
        list = self.chn()
        mean = self.calcmean()
        total = 0
        for i in list:
            total += pow(float(i) - mean, 2)
        total = total/len(list)
        self.result.setText("standard deviation: " + str(sqrt(total)) +'\n' + "variance: "+ str(total))
        self.result.setStyleSheet("background-color:black; color:white; font: 75  18pt \"Consolas\" ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Stat()
    #widget.resize(400, 200)
    widget.setWindowTitle("Data Analysis")
    widget.setStyleSheet(stylesheet)
    widget.setGeometry(10, 10, 1075, 796)
    widget.show()
    sys.exit(app.exec())
