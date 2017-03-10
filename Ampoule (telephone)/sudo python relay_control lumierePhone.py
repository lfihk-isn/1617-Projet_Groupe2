import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(23, GPIO.OUT)

while (True):

    # Turn all relays ON
    GPIO.output(23, GPIO.HIGH)
   
    # Sleep for 5 seconds
    sleep(5) 
    # Turn all relays OFF
    GPIO.output(23, GPIO.LOW)
  )   
    # Sleep for 5 seconds
    sleep(5)
	
	sudo python relay_control lumierePhone.py