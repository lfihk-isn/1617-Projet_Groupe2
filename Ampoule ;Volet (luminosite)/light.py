#!/usr/bin/python  
import time  
import RPi.GPIO as GPIO  
  
GPIO.setmode(GPIO.BOARD)  
  
def RCtime (RCpin):  
        reading = 0  
        GPIO.setup(11, GPIO.OUT)  
        GPIO.output(11, GPIO.LOW)  
        time.sleep(0.1)  
  
        GPIO.setup(11, GPIO.IN)  
        while (GPIO.input(11) == GPIO.LOW):  
                reading += 1  
        return reading  
  
while True:                                       
        print RCtime(11)  
