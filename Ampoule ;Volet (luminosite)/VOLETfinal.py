#!/usr/bin/python 
#Ce code permet de faire fonctionner le moteur du volet (38) avec le relais et d'allumer une LED (5) a partir de la luminosite 
import time  
import RPi.GPIO as GPIO  
  
GPIO.setmode(GPIO.BOARD)  
  
def RCtime (RCpin):  
        reading = 0  
        GPIO.setup(40, GPIO.OUT)  
        GPIO.output(40, GPIO.LOW)  
        time.sleep(5)  
  
        GPIO.setup(40, GPIO.IN)  
        while (GPIO.input(40) == GPIO.LOW):  
                reading += 1  
        return reading  

i = 0
while True:
        LDR = RCtime(21)
        print LDR
        x = LDR
        GPIO.setup(38, GPIO.OUT) 
        GPIO.output(38, GPIO.LOW)
        if (x<500):
		if (i <= 0):
                        GPIO.setup(5, GPIO.OUT) 
                        GPIO.output(5, GPIO.LOW)
                        GPIO.setup(38, GPIO.OUT)  
                        GPIO.output(38, GPIO.HIGH)
			i = 1
	if (x>500):
		if (i >= 1):
                        GPIO.setup(5, GPIO.OUT) 
                        GPIO.output(5, GPIO.HIGH)
			GPIO.setup(38, GPIO.OUT)  
                        GPIO.output(38, GPIO.HIGH)
			i = 0
	
 
