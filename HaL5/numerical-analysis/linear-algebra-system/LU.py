import numpy as np

def LU(A):
    m = len(A)
    U = A.copy()
    L = np.identity(m)
    for k in range(m-1):
        if U[k][k] == 0:
            raise ValueError('Matrix is singular')
        for i in range(k+1, m):
            if U[i][k] == 0:
                continue
            L[i][k] = U[i][k] / U[k][k]
            U[i][k] = 0
            for j in range(k+1, m):
                U[i][j] -= L[i][k] * U[k][j]
    return L, U

def solve(b, L):
    m = len(L)
    for k in range(m-1):
        for i in range(k+1, m):
            if L[i][k] == 0:
                continue
            b[i] -= L[i][k] * b[k]
    return b

def LU2(A):
    m = len(A)
    U = A.copy()
    for k in range(m-1):
        if U[k][k] == 0:
            raise ValueError('Matrix is singular')
        for i in range(k+1, m):
            if U[i][k] == 0:
                continue
            U[i][k] /= U[k][k]
            for j in range(k+1, m):
                U[i][j] -= U[i][k] * U[k][j]
    return U

def solve2(b, U):
    m = len(U)
    # for k in range(m-1, 0, -1):
    #     for i in range(k-1, -1, -1):
    #         b[i] -= U[i][k] * b[k]
    # return b
    for k in range(1, m-1):
        for i in range(k+1, m):
            if U[k][k] == 0:
                raise ValueError('Matrix is singular')
            b[i] -= U[i][k] * b[k]
    return b

if __name__ == "__main__":
    # A = [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,10]
    #     ]
    A = np.array([[1,2,3],[4,5,6],[7,8,10]])
    b = np.array([1,4,7])
    print(LU(A)[0])
    print(LU(A)[1])
    print(solve(b, LU(A)[0]))
    print("===============")
    print(LU2(A))
    print(solve2(b, LU2(A)))