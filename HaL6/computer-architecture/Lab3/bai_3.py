#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def main():
    BT1 = 14
    BT2 = 4
    BT3 = 3
    BT4 = 2
    LED = 22
    clickBT3 = False
    clickBT4 = False
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN)
    GPIO.setup(BT2, GPIO.IN)
    GPIO.setup(BT3, GPIO.IN)
    GPIO.setup(BT4, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)
    while True:
        if GPIO.input(BT1) == GPIO.HIGH:
            GPIO.output(LED, True)
            clickBT3 = False
            time.sleep(0.5)
        if GPIO.input(BT2) == GPIO.HIGH:
            time.sleep(0.5)
        if clickBT3:
            if GPIO.input(LED) == GPIO.LOW:
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)
            if GPIO.input(LED) == GPIO.HIGH:
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)
        if GPIO.input(BT4) == GPIO.HIGH:
            clickBT3 = False
            time.sleep(0.5)
            if clickBT4:
                GPIO.output(LED, GPIO.LOW)
                clickBT4 = False
                time.sleep(0.5)
                continue
            if not clickBT4:
                GPIO.output(LED, GPIO.HIGH)
                clickBT4 = True
                time.sleep(0.5)
                continue

# def peripheral_setup():
    # pio.terminal = Ports.SerialTerminal(9600)

# def main():
    # BT1 = 14
    # LED = 22
    # GPIO.setmode(GPIO.BCM)
    # peripheral_setup()
    # GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(LED, GPIO.OUT)
    # while True:
        # if GPIO.input(BT1) == GPIO.LOW:
            # pio.terminal.println("den bat")
            # GPIO.output(LED, GPIO.HIGH)
            # time.sleep(0.5)
        # else:
            # GPIO.output(LED, GPIO.LOW)
                
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()