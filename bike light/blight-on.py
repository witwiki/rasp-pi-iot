'''

    @author: Vikram Udyawer
    @date: 19th March 2017 Sunday
    @summary: Bike Light On
    @description:
                  Code for a Raspberry Pi to switch ON all LEDs of a bicycle light.
                  

'''

import RPi.GPIO as GPIO

# Sets any warnings off
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)


# Settings LED pins to outputs and switch ON
for x in range(16, 24):
    # Setting to output
    GPIO.setup(x, GPIO.OUT)
    # Set the pin to True which switches the LED 'ON'
    GPIO.output(x, True)
    


