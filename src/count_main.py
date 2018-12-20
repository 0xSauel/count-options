# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
import os, sys
from collections import Counter
import re


encoding = 'utf-8'
class Ui_MainWindow(object):
    results_s = ""
    results_s2 = ''
    patterns = ['Стандарт (Smart)', 'Стандарт (промо)', 'Стандарт (корп. промо)', 'Стандарт (подарок)', 'Оптимум (подарок)', 'Оптимум (промо)', 'Оптимум (промо 2018)', 'Премиум (промо)',"10,0001 ГБ 112013","100 ГБ 2018"]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(331, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.listWidget = QtWidgets.QTextEdit(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setAutoFillBackground(False)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget.setReadOnly(True)
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 4, 0, 1, 1)
        self.pushButton3.setSizePolicy(sizePolicy)
        self.pushButton3.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 5, 0, 1, 1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Count Options"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton2.setText(_translate("MainWindow", "Разделить файл"))
        self.btnBrowse.setText(_translate("MainWindow", "Сделать хорошо"))
        self.pushButton3.setText(_translate("MainWindow", "Список номеров в файл"))
        self.btnBrowse.clicked.connect(self.openfile)
        self.pushButton.clicked.connect(self.savefile)
        self.pushButton2.clicked.connect(self.split)
        self.pushButton3.clicked.connect(self.number_list)



    def openfile(self, fileName):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Choose File", "","CSV Files (*.csv);;All Files (*)", options=options)
        if fileName:
            self.count(fileName, self.patterns)
        

    def count(self, fileName, patterns):
        myfile = open(fileName, 'r', encoding=encoding)
        results = {pattern:Counter() for pattern in self.patterns}
        for line in myfile:
            for pattern in self.patterns:
                if pattern in line:
                    results[pattern][line] += 1
       
        myfile.close() 
       


        for key, value in results.items():
            self.listWidget.append(key+": "+str(len(value)))

        self.listWidget.append('\n\n\n======================\n======================\n\n\n')
       
        
        
       
        for key, value in results.items():
            self.results_s += (key+": "+str(len(value))+"\n")
        return self.results_s
        return self.patterns

    def number_list(self, patterns):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName_n, _ = QFileDialog.getOpenFileName(None,"Choose File", "","CSV Files (*.csv);;All Files (*)", options=options)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName_nw, _ = QFileDialog.getSaveFileName(None,"Number List Save", "","CSV Files (*.csv);;All Files (*)", options=options)
        if fileName_n:
            n_results = []
            if fileName_nw:
                resultfile2 = open(fileName_nw, 'w', encoding=encoding)
                resultfile2.close()
                resultfile2 = open(fileName_nw, 'a', encoding=encoding)
            
            with open(fileName_n, 'r', encoding=encoding) as fp:
                lines = fp.read().splitlines()
                c = 0
                for l in lines:
                    if self.patterns[0] in l:
                       
                        resultfile2.write(l+"\n")
                    if self.patterns[0] in l: c += 1
                self.listWidget.append('\nКоличество номеров в файле: '+ str(c))
                self.listWidget.append('\n\n\n======================\n======================\n')

            fp.close()
            resultfile2.close()


    def savefile(self, results_s):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName_w, _ = QFileDialog.getSaveFileName(None,"Save", "","CSV Files (*.csv);;All Files (*)", options=options)
        
        if fileName_w:
            resultfile = open(fileName_w, "w", encoding=encoding)
            resultfile.write(self.results_s)
        

    def split(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName3, _ = QFileDialog.getOpenFileName(None,"Choose File", "","CSV Files (*.csv);;All Files (*)", options=options)
        if fileName3:
            lines_per_file = 500000
            smallfile = None
            count = 0
            with open(fileName3, 'r', encoding=encoding) as bigfile:
                for lineno, line in enumerate(bigfile):
                    if lineno % lines_per_file == 0:
                        count += 1
                        if smallfile:
                            smallfile.close()
                        small_filename = '{}_500k_{}.csv'.format(fileName3, count)
                        smallfile = open(small_filename, "w", encoding=encoding)
                    smallfile.write(line)
                if smallfile:
                    smallfile.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

