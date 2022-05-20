#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

def main():
    dht11 = 24
    instance = DHT11(pin=dht11)
    while True:
        temperature, humidity = instance.read()
        if temperature == 0 and humidity == 0 and humidity < 20:
            continue
        print('temperature: %-3.1f C' % temperature)
        print('humidity: %-31.f %%' % humidity)

class DHT11:
    def __init__(self, pin):
        self.pin = pin
        self.temperature = None
        self.humidity = None

    def read(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        # high
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.05)
        # low
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.02)
        # chuyen no sang input va pull_up
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        count = 0
        last = -1
        data = []
        while True:
            current = GPIO.input(self.pin)
            data.append(current)
            if last != current:
                count = 0
                last = current
            else:
                count += 1
                if count > 100:
                    break
        # phan tich do dai cua du lieu
        pull_up_lengths = self.parse_data_pull_up_lengths(data)
        if len(pull_up_lengths) != 40:
            return (0, 0)
        # tinh toan cac bit
        bits = self.calculate_bits(pull_up_lengths)
        # khi co bit, tinh toan cac byte
        the_bytes = self.bits_to_bytes(bits)
        # y nghia cua cac gia tri cam bien duoc tra ve
        # the_bytes[0]: humidity int
        # the_bytes[1]: humidity decimal
        # the_bytes[2]: temperature int
        # the_bytes[3]: temperature decimal
        self.temperature = the_bytes[2] + float(the_bytes[3])/10
        self.humidity = the_bytes[0] + float(the_bytes[1])/10
        return self.temperature, self.humidity
    
    def parse_data_pull_up_lengths(self, data):
        STATE_INIT_PULL_DOWN = 1
        STATE_INIT_PULL_UP = 2
        STATE_DATA_FIRST_PULL_DOWN = 3
        STATE_DATA_PULL_UP = 4
        STATE_DATA_PULL_DOWN = 5
        state = STATE_INIT_PULL_DOWN
        lengths = [] # chua do dai du lieu truoc
        current_length = 0 # chua do dai du lieu sau
        for i in range(len(data)):
            current = data[i]
            current_length += 1
            if state == STATE_INIT_PULL_DOWN:
                if current == GPIO.LOW:
                    # ta da khoi tao no pull down
                    state = STATE_INIT_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_INIT_PULL_UP:
                if current == GPIO.HIGH:
                    # ta da khoi tao no pull up
                    state = STATE_DATA_FIRST_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_FIRST_PULL_DOWN:
                if current == GPIO.LOW:
                    # ta da khoi tao no pull down
                    # tiep thep se la du lieu pull up
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_UP:
                if current == GPIO.HIGH:
                    # data pulled up, do dai cua pull se quyet dinh dau la 0 hoac 1
                    current_length = 0
                    state = STATE_DATA_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_DOWN:
                if current == GPIO.LOW:
                    # data pulled down, ta luu tru do dai cua pull up truoc
                    lengths.append(current_length)
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
        return lengths
        
    def calculate_bits(self, pull_up_lengths):
        # tim khoang cach thoi gian ngan nhat va dai nhat
        shortest_pull_up = 1000
        longest_pull_up = 0
        for i in range(0, len(pull_up_lengths)):
            length = pull_up_lengths[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length
        # su dung halfway de xac dinh xem khoang thoi gian do la dai hay ngan
        halfway = shortest_pull_up + (longest_pull_up - shortest_pull_up)/2
        bits = []
        for i in range(0, len(pull_up_lengths)):
            bit = False
            if pull_up_lengths[i] > halfway:
                bit = True
            bits.append(bit)
        retur bits
        
    def bits_to_bytes(self, bits):
        the_bytes = []
        byte = 0
        for i in range(0, len(bits)):
            byte = byte << 1
            if bits[i]:
                byte = byte | 1
            else:
                byte = byte | 0
            if (i+1)%8 == 0:
                the_bytes.append(byte)
                byte = 0
        return the_bytes
        
try:
    main()
except KeyboardInterrupt:
    print('cleanup')
    GPIO.cleanup()