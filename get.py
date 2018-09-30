#!/usr/bin/python                                                                                                                                                                          
#from check.pyo import checkio
from time import sleep
import serial
import RPi.GPIO as GPIO  
from threading import Thread
import check
import os
import logging



'''   Winsoft custom setting '''

hostname = "8.8.8.8" #example
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s',filename='/var/log/gate.log',filemode='w')
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s',filename='/var/log/gate.log',filemode='w')
GATE1 = 17
GATE2 = 18
GATE3 = 19
GATE4 = 20
GATE5 = 21

CLOSE = 0
OPEN = 1





def main():
    logging.info('Hello pi!')
    while(1):
        response = os.system("ping -c 1 " + hostname)

        #and then check the response...
        if response == 0:
            print ("hostname, is up!")
            break
        else:
            print ("hostname, is down!")
            sleep(5)


    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(GATE1, GPIO.OUT)  # set up pin 17
    GPIO.setup(GATE2, GPIO.OUT)  # set up pin 18
    GPIO.setup(GATE3, GPIO.OUT)  # set up pin 18
    GPIO.setup(GATE4, GPIO.OUT)  # set up pin 18

    acm0 = serial.Serial('/dev/ttyACM0', 115200)
    t1 = Thread(target=check.checkio, args=(acm0,115200, GATE1,))
    t1.start()

    acm1 = serial.Serial('/dev/ttyACM1', 115200)
    t2 = Thread(target=check.checkio, args=(acm1,115200, GATE2,))
    t2.start()


    usb0 = serial.Serial('/dev/ttyUSB0', 9600)
    t3 = Thread(target=check.checkio, args=(usb0,9600,GATE3,))
    t3.start()

    '''
    usb1 = serial.Serial('/dev/ttyUSB1', 9600)
    t4 = Thread(target=check.checkio, args=(contype,))
    t4.start()
    '''
    while True :
        try:
            sleep(1); 
        except:
            pass


if __name__ == "__main__":
    main()
