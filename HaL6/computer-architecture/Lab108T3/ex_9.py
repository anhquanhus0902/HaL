import cv2
import RPi.GPIO as GPIO
import time

def main():
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global namewindow
    namewindow = 'Camera user'
    capture = cv2.VideoCaputre(0)
    print('capture is ok')
    while True:
        ret, frame = capture.read()
        if GPIO.input(BT1) == GPIO.LOW:
            while True:
                cv2.imshow('img', frame)
                cv2.waitKey()
                cv2.destroyWindow('img')
                break

try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyWindow(namewindow)
