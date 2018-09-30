#!/usr/bin/python                                                                                                                                                                          
# Say hello, world.


import serial


ser = serial.Serial('/dev/ttyACM0', 115200)
while True :
    try:
        state = ser.readline()
        #print("hurra:", state) #this is exanple of error ,
        print(state) 
    except:
        pass
