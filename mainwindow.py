# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnMANUAL = QtWidgets.QRadioButton(self.centralWidget)
        self.btnMANUAL.setGeometry(QtCore.QRect(10, 270, 82, 17))
        self.btnMANUAL.setObjectName("btnMANUAL")
        self.btnAUTO = QtWidgets.QRadioButton(self.centralWidget)
        self.btnAUTO.setGeometry(QtCore.QRect(100, 270, 82, 17))
        self.btnAUTO.setObjectName("btnAUTO")
        self.btnONOFF = QtWidgets.QRadioButton(self.centralWidget)
        self.btnONOFF.setGeometry(QtCore.QRect(190, 270, 82, 17))
        self.btnONOFF.setObjectName("btnONOFF")
        self.pshUP = QtWidgets.QPushButton(self.centralWidget)
        self.pshUP.setGeometry(QtCore.QRect(100, 300, 61, 23))
        self.pshUP.setObjectName("pshUP")
        self.pshLEFT = QtWidgets.QPushButton(self.centralWidget)
        self.pshLEFT.setGeometry(QtCore.QRect(40, 320, 61, 23))
        self.pshLEFT.setObjectName("pshLEFT")
        self.pshDOWN = QtWidgets.QPushButton(self.centralWidget)
        self.pshDOWN.setGeometry(QtCore.QRect(100, 340, 61, 23))
        self.pshDOWN.setObjectName("pshDOWN")
        self.pshRIGHT = QtWidgets.QPushButton(self.centralWidget)
        self.pshRIGHT.setGeometry(QtCore.QRect(160, 320, 61, 23))
        self.pshRIGHT.setObjectName("pshRIGHT")
        self.sldSPEED = QtWidgets.QSlider(self.centralWidget)
        self.sldSPEED.setGeometry(QtCore.QRect(40, 370, 181, 22))
        self.sldSPEED.setOrientation(QtCore.Qt.Horizontal)
        self.sldSPEED.setObjectName("sldSPEED")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 400, 181, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.viewPICTURE = QtWidgets.QGraphicsView(self.centralWidget)
        self.viewPICTURE.setGeometry(QtCore.QRect(10, 70, 256, 192))
        self.viewPICTURE.setObjectName("viewPICTURE")
        self.lcdTEMPSENS1 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdTEMPSENS1.setGeometry(QtCore.QRect(460, 110, 101, 31))
        self.lcdTEMPSENS1.setObjectName("lcdTEMPSENS1")
        self.lcdTEMPSENS1_2 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdTEMPSENS1_2.setGeometry(QtCore.QRect(460, 180, 101, 31))
        self.lcdTEMPSENS1_2.setObjectName("lcdTEMPSENS1_2")
        self.lcdTEMPSENS1_3 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdTEMPSENS1_3.setGeometry(QtCore.QRect(460, 250, 101, 31))
        self.lcdTEMPSENS1_3.setObjectName("lcdTEMPSENS1_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(320, 110, 131, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(320, 180, 131, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(320, 250, 131, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.btnELECTONOFF = QtWidgets.QRadioButton(self.centralWidget)
        self.btnELECTONOFF.setGeometry(QtCore.QRect(380, 150, 141, 17))
        self.btnELECTONOFF.setObjectName("btnELECTONOFF")
        self.radioButton = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(380, 220, 141, 17))
        self.radioButton.setObjectName("radioButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 581, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.btnIMAGEREFRESH = QtWidgets.QPushButton(self.centralWidget)
        self.btnIMAGEREFRESH.setGeometry(QtCore.QRect(320, 70, 241, 31))
        self.btnIMAGEREFRESH.setObjectName("btnIMAGEREFRESH")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnMANUAL.setText(_translate("MainWindow", "Manual"))
        self.btnAUTO.setText(_translate("MainWindow", "Auto"))
        self.btnONOFF.setText(_translate("MainWindow", "ON/OFF"))
        self.pshUP.setText(_translate("MainWindow", "UP"))
        self.pshLEFT.setText(_translate("MainWindow", "LEFT"))
        self.pshDOWN.setText(_translate("MainWindow", "DOWN"))
        self.pshRIGHT.setText(_translate("MainWindow", "RIGHT"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "0              Drill Speed               100"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Electronics Temperature"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Misc. Temperature"))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "Weight on Bit"))
        self.btnELECTONOFF.setText(_translate("MainWindow", "Electronics Heat ON/OFF"))
        self.radioButton.setText(_translate("MainWindow", "Misc. Heat ON/OFF"))
        self.btnIMAGEREFRESH.setText(_translate("MainWindow", "Refresh Image"))

