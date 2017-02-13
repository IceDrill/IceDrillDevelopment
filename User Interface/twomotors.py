#SerialLED.py
from main_twomotors import ser, ser1
import serial
import sys

        
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

if __name__ == '__main__':
	MotorOn()
	MotorOff()
	Motor2On()
	Motor2Off()
	
