#!/usr/bin/python  
import time  
import RPi.GPIO as GPIO  
  
GPIO.setmode(GPIO.BOARD)  
  
def RCtime (RCpin):  
        reading = 0  
        GPIO.setup(11, GPIO.OUT)  
        GPIO.output(11, GPIO.LOW)  
        time.sleep(1)  
  
        GPIO.setup(11, GPIO.IN)  
        while (GPIO.input(11) == GPIO.LOW):  
                reading += 1  
        return reading  
i = 0

while True:
        LDR = RCtime(11)
        print LDR
        x = LDR 
        GPIO.setup(16, GPIO.OUT) 
        GPIO.output(16, GPIO.LOW)
        if (x<500):
		if (i <= 0):
                        GPIO.setup(36, GPIO.OUT) 
                        GPIO.output(36, GPIO.LOW)
                        GPIO.setup(16, GPIO.OUT)  
                        GPIO.output(16, GPIO.HIGH)
			i = 1
	if (x>500):
		if (i >= 1):
                        GPIO.setup(36, GPIO.OUT) 
                        GPIO.output(36, GPIO.HIGH)
			GPIO.setup(16, GPIO.OUT)  
                        GPIO.output(16, GPIO.HIGH)
			i = 0
	
 
