'''

    @author: Vikram Udyawer
    @date: 25th March 2017 Saturday
    @summary: No PWM controlled RGB LED
    @description:
                  Code for a Raspberry Pi to switch ON 
                  an RGB LED its different
                  colors without PWM.

'''


import RPi.GPIO as GPIO
import threading
import time
import random

red = 19
green = 20
blue = 21

PINS = [red, green, blue]		# R, G, B


def main():
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
		print("\nPress ^C (Ctrl-C) to exit program.\n")
		while True:
			pickNextPin()
			# the all() method is equivalent to an AND logical operator in this case
			if all(GPIO.input(pin) == GPIO.LOW for pin in PINS):
				pickNextPin()
			time.sleep(0.75)
	except KeyboardInterrupt:
		pass
	finally:
		GPIO.cleanup()
	

def pickNextPin():
'''	pick a random pin from the array PINS. 
	Random generator will pick a random integer 
	between 0 and 2 inclusive
'''
	nextPin = PINS[random.randint(0,2)]
	GPIO.output(nextPin, not GPIO.input(nextPin))

if __name__ == '__main__':
	main()