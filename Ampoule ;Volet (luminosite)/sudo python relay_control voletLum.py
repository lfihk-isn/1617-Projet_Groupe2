import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(24, GPIO.OUT)

while (True):

    # Turn all relays ON
    GPIO.output(24, GPIO.HIGH)
   GPIO.output(25, GPIO.HIGH)
    # Sleep for 5 seconds
    sleep(5) 
    # Turn all relays OFF
    GPIO.output(24, GPIO.LOW)
	GPIO.output(25, GPIO.HIGH)
    # Sleep for 5 seconds
    sleep(5)
	
	sudo python relay_control voletTemp.py