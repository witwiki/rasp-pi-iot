'''

    @author: Vikram Udyawer
    @date: 19th March 2017 Sunday
    @summary: Bike Light Pulse
    @description:
                  Code for a Raspberry Pi to pulse LEDs like a bicycle light.

'''

import RPi.GPIO as GPIO
from time import sleep

# Sets any warnings off
GPIO.setwarnings(False)

def channelOn():
    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BCM)
    for x in range(16, 24):
        # Setting to output
        GPIO.setup(x, GPIO.OUT)    

def pulseOn():    
    # Settings LED pins to outputs and switch ON
    for x in range(16, 24):
        GPIO.output(x, True)

def pulseOff():
    for x in range(16, 24):
        GPIO.output(x, False)
 
    
# Pulse i times
channelOn()
for i in range(0, 10):
    pulseOn()
    sleep(0.1)
    pulseOff()

