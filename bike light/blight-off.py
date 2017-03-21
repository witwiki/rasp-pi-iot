'''

    @author: Vikram Udyawer
    @date: 19th March 2017 Sunday
    @summary: Bike Light Off
    @description:
                  Code for a Raspberry Pi to switch off all LEDs of a bicycle light.
                  

'''

import RPi.GPIO as GPIO
import time

# Sets any warnings off
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)


# Settings LED pins to outputs and switch off
for x in range(16, 24):
    # Setting to output
    GPIO.setup(x, GPIO.OUT)
    # Set the pin to False which switches it off
    GPIO.output(x, False)
    


