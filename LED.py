Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Led.py 
... import RPi.GPIO as GPIO
... import time
... GPIO.setmode(GPIO.BCM)
... GPIO.setwarnings(False)
... pinout = 19
... color = "Yellow"
... GPIO.setup(pinout,GPIO.OUT)
... print "LED on N" + str(pinout) + " " + color
... GPIO.output(pinout,GPIO.HIGH)
... time.sleep(1)
... print "LED off N" + str(pinout) + " " + color
... GPIO.output(pinout,GPIO.LOW)
