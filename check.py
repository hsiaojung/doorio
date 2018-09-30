import urllib.request
import urllib.parse
import RPi.GPIO as GPIO
import serial
import string
import mainloop
import re
import logging


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import socket
import urllib.request

# timeout in seconds
timeout = 8                                                                                                                                                                                  
socket.setdefaulttimeout(timeout)


def checkio(contype,conspeed, GATEIO):

    if GATEIO == mainloop.GATE1IO:
        GATE = 1
    if GATEIO == mainloop.GATE2IO:
        GATE = 2
    if GATEIO == mainloop.GATE3IO:
        GATE = 3
    if GATEIO == mainloop.GATE4IO:
        GATE = 4

    while (1):

        #print(get.GATE5)
        state = contype.readline()
        print(state)
        '''for value in state:
            print(value)'''

        #f = urllib.request.urlopen(url)
        #readback = f.read().decode('utf-8')
        #oprint(f.read().decode('utf-8'))
        readback = []
        readback = state.decode('utf-8','ignore')

        #strip_control_characters = lambda readback:"".join(i  for i in readback if 31<ord(i)<127)  
        #print(readback[1:]) #skip first one
        readback = readback.replace('\r', '')
        readback = readback.replace('\n', '')
        readback = readback.replace('\x02', '')
        readback = readback.replace('\x1b', '')
        #readback = readback[2:]
        urlstr = "http://www.wisoft.com.tw/reedot/checknow.jsp?id=%s&io=0&gate=1"%(readback)
        #http://www.wisoft.com.tw/reedot/checknow.jsp?id=E9CB810C&io=0&gate=1
        print(urlstr)
        try:
            f = urllib.request.urlopen(urlstr ,timeout=5)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            logging.info('the server could not be reached!')
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            logging.info('we failed to readch server!!!!!')
        else:
            readback_server = f.read().decode('utf-8')
            print("show = %s."%(readback_server) )
            print(readback_server.find("OK"))

            if readback_server.find("OK") >= 0:
                print ("%s is on the list! SET GATE%d (GPIO%d) to OPEN"%(readback,GATE,GATEIO))
                GPIO.output(GATEIO, mainloop.OPEN)
                logging.info('%s is on the list! SET GATE%d (GPIO%d) to OPEN'%(readback,GATE,GATEIO))
                #logging.info('Hello world again!')
            else:

                GPIO.output(GATEIO, mainloop.CLOSE)
                print ("%s is not on the list! SET GATE%d (GPIO%d) to LOW"%(readback,GATE,GATEIO))
                logging.info('%s isnt on the list! SET GATE%d (GPIO%d) to CLOSE'%(readback,GATE,GATEIO))
            
            
            readback_server = "init"

    return
'''
# bytes object
  b = b"example"
  
    # str object
      s = "example"
      
        # str to bytes
          bytes(s, encoding = "utf8")
          
            # bytes to str
              str(b, encoding = "utf-8")
              
                # an alternative method
                  # str to bytes
                    str.encode(s)
                    
                      # bytes to str
                        bytes.decode(b)
                        '''
