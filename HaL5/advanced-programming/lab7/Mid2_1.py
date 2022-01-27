from math import sqrt, factorial

def compare(el):
    return el[1], el[0]

def getTop2gram(filename, n):
    f = open(filename, 'r')
    dct = {}
    for line in f:
        line = line.strip().split()
        for i in range(len(line)-1):
            k = line[i] + ' ' + line[i+1]
            dct[k] = dct.get(k, 0) + 1
    f.close()
    lst = [(k, v) for k, v in dct.items()]
    lst.sort(key=compare)
    res = [k for (k, v) in lst[-n:]]
    return sorted(res, reverse=True)

def getVector(filename, top2gram):
    f = open(filename, 'r')
    dct = {}
    res = []
    for line in f:
        line = line.strip().split()
        for i in range(len(line)-1):
            k = line[i] + ' ' + line[i+1]
            dct[k] = dct.get(k, 0) + 1
    f.close()
    for i in top2gram:
        res.append(dct[i])
    return res

def getDistance(u, v):
    res = 0
    for i in range(len(u)):
        res += (u[i] - v[i])**2
    return sqrt(res)


def coshTaylor(x, e):
    P = 0
    P_pre = 0
    i = 0
    while True:
        P_pre = P
        P += (x**(2*i)) / factorial(2*i)
        if abs(P - P_pre) <= e:
            i += 1
            P += (x**(2*i)) / factorial(2*i)
            break
        i += 1
    return P

def testDemo():
    print(getTop2gram('D:\\Datas\\khac\\quan\\HaL\\HaL5\\advanced-programming\\lab7\\text.txt', 5))
    print(getVector('text.txt', getTop2gram('text.txt', 5)))
    print(round(getDistance([1, 2, 3, 4], [1, 2, 1, 1]), 5))
    # print(round(coshTaylor(5.5, 0.5), 5))
    print(round(coshTaylor(3.4, 0.0001), 5))
    print(round(coshTaylor(6, 0.5), 5))
    
#testDemo()