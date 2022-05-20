#!/usr/bin/env python

import time

def main():
    msg = 'Hello-World'
    counter = 0
    inpEqualTok = False
    while True:
        if input() == 'k':
            print(msg, end='\r')
            counter += 1
            msg = ' '*counter + msg
            time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('done')
