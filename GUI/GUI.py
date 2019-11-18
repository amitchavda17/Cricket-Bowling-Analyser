import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget
import csv
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt




class Ui_MainWindow(object):
    def abc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi1(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 860)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 90, 551, 61))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 390, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.abc)#############################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        self.menuStart_Page = QtWidgets.QMenu(self.menubar)
        self.menuStart_Page.setObjectName("menuStart_Page")
        self.menuStats = QtWidgets.QMenu(self.menubar)
        self.menuStats.setObjectName("menuStats")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLine = QtWidgets.QAction(MainWindow)
        self.actionLine.setObjectName("actionLine")
        self.actionLength = QtWidgets.QAction(MainWindow)
        self.actionLength.setObjectName("actionLength")
        self.menuStats.addAction(self.actionLine)
        self.menuStats.addAction(self.actionLength)
        self.menubar.addAction(self.menuStart_Page.menuAction())
        self.menubar.addAction(self.menuStats.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cricket Bowling Analyser"))
        self.label_2.setText(_translate("MainWindow", "-By Team Ultraa"))
        self.pushButton.setText(_translate("MainWindow", "Start!"))
        self.menuStart_Page.setTitle(_translate("MainWindow", "Start Page"))
        self.menuStats.setTitle(_translate("MainWindow", "Stats"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
        self.actionLength.setText(_translate("MainWindow", "Length"))

##Stats page##
class Ui_Dialog(object):
    def abd(self):
        lst_leng=[]
        with open("people.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data=dict(row)
                lst_leng.append([data['lengthx'],data['lengthy']])
                
        csvfile.close()
        print(lst_leng)
        
        length=[]
        for lst in lst_leng:
            lst=int(lst[0])
            if(lst<=2):
                length.append('Yoker')
            elif(lst<=6): 
                length.append('Full')
            elif(lst<=10): 
                length.append('Good')
            else:
                length.append('Short')
        print(length)
        
        over=list(range(1,7))
        print(over)
        plt.figure(1, figsize=(18,18), dpi=250)
        plt.scatter(over,length,s=150,c='r')
        plt.xlabel("Balls",fontsize=13)
        plt.ylabel('Length of delivery',fontsize=13)
        plt.savefig('test1.jpg')
       
        plt.show()
        print(5)
       # self.window = QtWidgets.QDialog()
       # self.ui = Ui_Dialoge()
       # self.ui.setupUi2(self.window)
       # Dialog.hide()
       # self.window.show()
    def abline(self):
        
        lst_line=[]
        with open("people.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data=dict(row)
                
                lst_line.append([data['linex'],data['liney']])
        csvfile.close()
        
        line=[]
        
        
        for lst in lst_line:
            lst=int(lst[1])
            if(lst<=3):
                line.append('Off side')
            elif(lst<=6): 
                line.append('Middle')
            else: 
                line.append('LEG side')
        print(line)        
        over=list(range(1,7))
        print(over)
        
        plt.figure(2, figsize=(18, 18), dpi=250)
        plt.scatter(over,line,s=150)
        plt.xlabel("Balls")
        plt.ylabel('Line of delivery')
        plt.savefig('test2.jpg')
        plt.show()
        print(5)
    #def abx(self):
       # self.window = QtWidgets.QDialog()
       # self.ui = Ui_Dialoge()
       # self.ui.setupUi2(self.window)
       # Dialog.hide()
       # self.window.show()
    def setupUi1(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1120, 860)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 90, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Centaur")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 300, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 470, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.abline)#############################################################
        self.pushButton_2.clicked.connect(self.abd)#############################################################

        self.retranslateUi1(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi1(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Your Preference"))
        self.pushButton.setText(_translate("Dialog", "Line"))
        self.pushButton_2.setText(_translate("Dialog", "Length"))

        ##graph page##
class Ui_Dialoge(object):
    def abe(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi1(self.window)
        Dialoge.hide()
        self.window.show()
    def setupUi2(self, Dialoge):
        Dialoge.setObjectName("Dialoge")
        Dialoge.resize(1120, 860)
        Dialoge.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton = QtWidgets.QPushButton(Dialoge)
        self.pushButton.setGeometry(QtCore.QRect(490, 810, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.abe)#############################################################

        self.retranslateUi2(Dialoge)
        QtCore.QMetaObject.connectSlotsByName(Dialoge)

    def retranslateUi2(self, Dialoge):
        _translate = QtCore.QCoreApplication.translate
        Dialoge.setWindowTitle(_translate("Dialoge", "Dialoge"))
        self.pushButton.setText(_translate("Dialoge", "BACK"))
        #image#







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QMainWindow()
    Dialoge = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
