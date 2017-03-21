'''

    @author: Vikram Udyawer
    @date: 19th March 2017 Sunday
    @summary: Bike Light Alternate
    @description:
                  Code for a Raspberry Pi to switch ON LEDs by alternating
                  one after the other - of a bicycle light.
                  

'''

import RPi.GPIO as GPIO
from time import sleep

# Sets any warnings off
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)


# Settings LED pins to outputs and switch ON
for x in range(16, 24):
    # Setting to output
    GPIO.setup(x, GPIO.OUT)
    # Set the pin to True which switches the LED 'ON'
    GPIO.output(x, True)
    # Set a 1 seconds delay
    sleep(1)
    # Set the pin to False which switches the LED 'OFF'
    GPIO.output(x, False)



