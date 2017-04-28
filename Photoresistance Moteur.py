#!/usr/bin/python  
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
  
while True:
	LDR = RCtime(21)
    print LDR  
	i = 0
	x = LDR
	if (x<300):
		if i = 0:
			GPIO.setup(7, GPIO.OUT)  
            GPIO.output(7, GPIO.HIGH)
			i = 1
	if (x>300):
		if i = 1:
			GPIO.setup(7, GPIO.OUT)  
            GPIO.output(7, GPIO.LOW)
			i = 0
