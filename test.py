import urllib.request
import urllib.parse
import RPi.GPIO as GPIO

def checkio():

    GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom)
    
    GPIO.setup(17, GPIO.OUT)  # set up pin 17
    GPIO.setup(18, GPIO.OUT)  # set up pin 18
    
    GPIO.output(17, 1)  # turn on pin 17
    GPIO.output(18, 1)  # turn on pin 18


#url = 'http://www.wisoft.com.tw/reedot/checknow.jsp?id=ooooo&io=0&gate=1'
#f = urllib.request.urlopen(url)
#readback = f.read().decode('utf-8')

#print(f.read().decode('utf-8'))
    readback="13323"
#print(readback)

    if readback.find("123") == 0:
    print ("the number is on the list!")



    else:

    print ("the number is not authorized .")    
    return 1;

