#!/usr/bin/env python

# II.3

import time
import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n:int) -> int:
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

def calculateExecutionTime(inputNumber:int) -> int:
	startTime = time.time()
	fibonacci(inputNumber)
	finishTime = time.time()
	return finishTime-startTime

def evaluate(k:int) -> None:
	inputPoints = timePoints = np.array([])
	for i in range(k+1):
		inputNumber = 5*i
		inputPoints = np.append(inputPoints, inputNumber)
		timePoints = np.append(timePoints, calculateExecutionTime(inputNumber))
	plt.xlabel('Input number')
	plt.ylabel('Execution Time (second)')
	plt.plot(inputPoints, timePoints, marker='o')
	plt.show()

if __name__ == "__main__":
	try:
		n = int(input('n?\n'))
		if (n < 0):
			print('Nhập số tự nhiên thôi mike pence')
		else:
			print('Số fibonacci thứ {} là: {}'.format(n, fibonacci(n)))
			ev = input('Bạn có muốn xem đánh giá (Lưu ý: Chạy hơi lâu :D)? (Y/n): ')
			if ev == 'Y' or ev == 'y':
				evaluate(8)
	except ValueError:
		print('Nhập số tự nhiên thôi mike pence')
