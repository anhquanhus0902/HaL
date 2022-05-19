import RPi.GPIO as GPIO
import time

def main():
    clickBT2 = 1
    rangee = 20
    BT2 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    msg = 'Hello-World'
    tmp = ''
    while True:
        if GPIO.input(BT2) == GPIO.LOW:
            if clickBT2 == 1:
                msg1 = msg
                for k in range(len(msg)+1):
                    if k >= 1:
                        lPart = msg[:-k]
                        runChar = msg[-k]
                        for i in range(rangee):
                            msg1 = lPart + ' '*i + runChar
                            print(msg1, end='\r')
                            time.sleep(0.05)
                    else:
                        print(msg1, end='\r')
                        time.sleep(0.05)
                tmp = msg1 + msg[1:]
                clickBT2 = 2
                continue
            elif clickBT2 == 2:
                msg2 = tmp
                for k in range(len(msg)):
                    if k >= 0:
                        rPart = msg[k:]
                        runChar = msg[k]
                        for i in range(rangee-1, -1, -1):
                            msg2 = runChar + ' '*i + rPart
                            print(msg2 + ' ', end='\r')
                            time.sleep(0.05)
                    else:
                        print(msg2, end='\r')
                        time.sleep(0.05)
                clickBT2 = 3
                continue
            elif clickBT2 == 3:
                print(' '*len(msg), end='\r')
                clickBT2 = 1
                time.sleep(2)
                continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        GPIO.cleanup()
