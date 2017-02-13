#SerialLED.py
from main1 import ser, ser1
import serial
import sys


#ser = serial.Serial('/dev/ttyACM0',9600)
#ser1 = serial.Serial('/dev/ttyACM1',9600)
#ser.flush() 
#print("Basic Control of LED via Serial connection")
#print("please type 'on' or 'off'")
#command = "off"
#while True:
#    command = input()
#    print(command)
#    if (command == "on") or (command == "off"):
#        ser.write(command)
#    elif command=="stop":
#       exit()
        
def LightOn():
	ser.write(b'on')
	print("wrote on")
	
def BLightOn():
	ser1.write(b'on')
	print("wrote on")
	
	
def LightOff():
	ser.write(b'off')
	print("wrote off")

def BLightOff():
	ser1.write(b'off')
	print("wrote off")	

	

if __name__ == '__main__':
	LightOn()
	LightOff()
	#note...somehow this worked without
	#BLightOn and BLightOff down here...
	#consider testing otherwise
