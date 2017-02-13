#main.py for GUI

import sys
import serial
import SerialLED

# Qt packages
import PyQt5
from PyQt5.QtWidgets import *

#UI file generated from Qt
import mainwindow

#Raspberry Pi GUI class
ser = serial.Serial('/dev/ttyACM0',9600)
ser1 = serial.Serial('/dev/ttyACM1',9600)
ser.flush()
ser1.flush()


class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def drillOnButton(self):
		#use left button to turn on light
        SerialLED.LightOn()
        
    def BdrillOnButton(self):
		#use up button to turn blue light on
        SerialLED.BLightOn() 
        

    def drillOffButton(self):
		#use right button to turn off light
        SerialLED.LightOff()

    def BdrillOffButton(self):
		#use right button to turn off light
        SerialLED.BLightOff()
        

    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        
        
        self.pshLEFT.clicked.connect(lambda: self.drillOnButton())
        self.pshRIGHT.clicked.connect(lambda: self.drillOffButton())

        self.pshUP.clicked.connect(lambda: self.BdrillOnButton())
        self.pshDOWN.clicked.connect(lambda: self.BdrillOffButton())


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
