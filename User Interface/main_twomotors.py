#main.py for GUI
import sys
import serial
import twomotors

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
    def MotorONEon(self):
	#use left button to turn motor 1 on
        twomotors.MotorOn()
    def MotorTWOon(self):
	#use up button to turn motor 2 on
        twomotors.Motor2On() 
        

    def MotorONEoff(self):
	#use right button to motor 1 off
        twomotors.MotorOff()
    def MotorTWOoff(self):
	#use right button to turn motor 2 off
        twomotors.Motor2Off()        

    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        

        #tell the program which func to implement when buttons are pressed
        self.pshLEFT.clicked.connect(lambda: self.MotorONEon())
        self.pshRIGHT.clicked.connect(lambda: self.MotorONEoff())
        self.pshUP.clicked.connect(lambda: self.MotorTWOon())
        self.pshDOWN.clicked.connect(lambda: self.MotorTWOoff())


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
