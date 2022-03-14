#!/usr/bin/env python

'''
III. Bài toán kiểm tra 1 số có phải là luỹ thừa của 2 hay không?

- Giải pháp: 
	- Nếu 1 số là lũy thừa của 2 thì nó có thể chia đệ quy cho 2 đến khi nó bằng 1
	- Nếu số đó là 0 hoặc nếu có bất kỳ số trung gian nào không chia hết cho 2 thì ta trả về False
- Độ phức tạp tính toán: O(log(n))
'''

def isPowOf2(n:int) -> bool:
	if n == 0:
		return False
	if n == 1:
		return True
	return (n%2 == 0 and isPowOf2(n//2))

if __name__ == "__main__":
	n = int(input('n = '))
	print(isPowOf2(n))
