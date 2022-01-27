#!/usr/bin/env python

def thuat_toan_khu(A, b):
    U = list(A)
    m = len(U)
    for k in range(m):
        for i in range(k+1, m):
            if U[i][k] == 0:
                continue
            l = U[i][k]/U[k][k]
            U[i][k] = 0
            for j in range(k+1, m):
                U[i][j] -= l * U[k][j]
            b[i] = b[i] - l * b[k]
    return (U, b)

def thuat_toan_the(U, b):
    m = len(U)
    x = [0 for i in range(m)]
    x[m-1] = b[m-1]/U[m-1][m-1]
    for k in range(m-1, -1, -1):
        for j in range(k+1, m):
            b[k] -= U[k][j] * x[j]
        x[k] = b[k]/U[k][k]
    return x

def solve(A, b):
    res1 = thuat_toan_khu(A, b)
    U = res1[0]
    b = res1[1]
    print(thuat_toan_the(U, b))
    
if __name__ == "__main__":
    A = [
            [1, -3, 2],
            [3, 2, 4],
            [2, 7, 6]    
        ]
    b = [4, 10, 5]
    solve(A, b)
