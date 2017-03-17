

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(2, GPIO.OUT)
#faire un code pour faire comme interrupteur? 
If: 
GPIO.output(2,GPIO.LOW)

