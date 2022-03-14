#!/usr/bin/env python

# II.1

import time
import numpy as np
import matplotlib.pyplot as plt

def dec2bin(n:int) -> str:
	if n >= 1:
		return dec2bin(n//2) + str(n%2)
	return ''

def calculateExecutionTime(inputNumber:int) -> int:
	startTime = time.time_ns()
	dec2bin(inputNumber)
	finishTime = time.time_ns()
	return finishTime-startTime

def evaluate(k:int) -> None:
	inputPoints = timePoints = np.array([])
	for i in range(k+1):
		inputNumber = 5*i
		inputPoints = np.append(inputPoints, inputNumber)
		timePoints = np.append(timePoints, calculateExecutionTime(inputNumber))
	plt.xlabel('Input number')
	plt.ylabel('Execution Time (nanosecond)')
	plt.plot(inputPoints, timePoints, marker='o')
	plt.show()

if __name__ == "__main__":
	try:
		n = int(input('n?\n'))
		if (n < 0):
			raise ValueError('Nhập số tự nhiên thôi mike pence')
		print('Hệ nhị phân của {} là: {}'.format(n, dec2bin(n)))
		ev = input('Bạn có muốn xem đánh giá	? (Y/n): ')
		if ev == 'Y' or ev == 'y':
			evaluate(200)
	except ValueError:
		raise ValueError('Nhập số tự nhiên thôi mike pence')
