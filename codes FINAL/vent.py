import os
import glob
import time
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BOARD)  
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
    

while True:

    x = read_temp()
    print x
    time.sleep(1)
    i=0
    GPIO.setup(12, GPIO.OUT) 
    GPIO.output(12, GPIO.LOW)
    if (x>30):
		if (i <= 0):

                        GPIO.setup(12, GPIO.OUT)  
                        GPIO.output(12, GPIO.HIGH)
			i = 1
    if (x<30):
		if (i >= 1):

			GPIO.setup(12, GPIO.OUT)  
                        GPIO.output(12, GPIO.HIGH)
			i = 0
	
 
