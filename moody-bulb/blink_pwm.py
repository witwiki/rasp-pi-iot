'''

    @author: Vikram Udyawer
    @date: 25th March 2017 Saturday
    @summary: PWM controlled RGB LED
    @description:
                  Code for a Raspberry Pi to switch ON
                  an RGB LED its different colors using PWM.


'''

import RPi.GPIO as GPIO  
import threading  
import time  
import random

R = 19  
G = 20  
B = 21

PINS = [R,G,B]

ROTATION_IN_MS = 750


def initializeGpio():  
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)


def rgbTest(channel, frequency, speed, step):  
    p = GPIO.PWM(channel, frequency)
    p.start(0)
    while True:
        for dutyCycle in range(0, 101, step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)
        for dutyCycle in range(100, -1, -step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)


def rgbThread():  
    threads = []
    threads.append(threading.Thread(target=rgbTest, args=(R, 300, 0.02, 50)))
    threads.append(threading.Thread(target=rgbTest, args=(G, 300, 0.035, 50)))
    threads.append(threading.Thread(target=rgbTest, args=(B, 300, 0.045, 50)))
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()


def main():  
    try:
        initializeGpio()
        print("\nPress ^C (control-C) to exit the program.\n")
        rgbThread()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':  
    main()
