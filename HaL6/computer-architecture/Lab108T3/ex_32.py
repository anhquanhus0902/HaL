import RPi.GPIO as GPIO
import time

def main():
    clickBT1 = 1
    rangee = 20
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    msg = 'Hello-World'
    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            if clickBT1 == 1:
                msg1 = msg
                clickBT1 = 2
                for i in range(rangee):
                    print(msg1, end='\r')
                    msg1 = ' ' + msg1
                    time.sleep(0.1)
                continue
            elif clickBT1 == 2:
                msg2 = ' '*(rangee-1) + msg
                clickBT1 = 3
                for i in range(rangee):
                    print(msg2+' ', end='\r')
                    msg2 = msg2[1:]
                    time.sleep(0.1)
                continue
            elif clickBT1 == 3:
                print(' '*len(msg), end='\r')
                clickBT1 = 1
                time.sleep(2)
                continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        GPIO.cleanup()
