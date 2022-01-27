#!/usr/bin/env python

'''
Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi
người dùng.
Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1+11+111+1111 = 1234
'''

def solve(a):
    res = 0
    for i in range(1, 5):
        num = 0
        for j in range(i):
            num += a * (10**j)
        res += num
    print(res)

if __name__ == "__main__":
    a = int(input())
    solve(a)
