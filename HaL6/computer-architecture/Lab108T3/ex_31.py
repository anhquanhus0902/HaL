import RPi.GPIO as GPIO
import time

def main():
    BT1 = 14
    BT2 = 4
    BT3 = 3
    BT4 = 2
    LED = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)
    isprBT3 = isprBT4 = False

    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print('BT1 press')
            isprBT3 = False
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.5)
        if GPIO.input(BT2) == GPIO.LOW:
            print('BT2 press')
            isprBT3 = False
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT3) == GPIO.LOW:
            print('BT3 press')
            isprBT3 = True
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT4) == GPIO.LOW:
            print('BT4 press')
            isprBT3 = False
            if isprBT4:
                GPIO.output(LED, GPIO.HIGH)
                isprBT4 = False
                time.sleep(0.5)
            else:
                GPIO.output(LED, GPIO.LOW)
                isprBT4 = True
                time.sleep(0.5)
        if isprBT3:
            print('During blinking')
            if GPIO.input(LED) == GPIO.LOW:
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)
            if GPIO.input(LED) == GPIO.HIGH:
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
