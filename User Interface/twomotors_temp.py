#SerialLED.py

import serial
import sys
ser = serial.Serial('/dev/ttyACM0',9600)
ser1 = serial.Serial('/dev/ttyACM1',9600)

        
def MotorOn():
	ser.write(b'on')
	print("Hopefully the Motor 1 is on")
	
def MotorOff():
	ser.write(b'off')
	print("Hopefully the Motor 1 is off")

def Motor2On():
	ser1.write(b'on')
	print("Hopefully the Motor 2 is on")
	
def Motor2Off():
	ser1.write(b'off')
	print("Hopefully the motor 2 is off")

def TempRead():
        ser.write(b'temp')
        print("we want the temp now bitch")
        tempdat=ser.readline()
        print(tempdat)
        

if __name__ == '__main__':
	MotorOn()
	MotorOff()
	Motor2On()
	Motor2Off()
	TempRead()
	
