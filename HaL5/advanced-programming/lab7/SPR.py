from math import sqrt

def sparseForm(t):
    l = len(t)
    dct = {}
    for i in range(l):
        if t[i] != 0:
            dct[i] = t[i]
    return l, dct

def revert(spr):
    res = [0] * spr[0]
    for k, v in spr[1].items():
        res[k] = v
    return res

def dot(spr1, spr2):
    t1 = revert(spr1)
    t2 = revert(spr2)
    res = 0
    for i in range(len(t1)):
        res += t1[i] * t2[i]
    return res

def norm(spr):
    res = 0
    t = revert(spr)
    for i in t:
        res += i ** 2
    return sqrt(res)


def getCosinSim(spr1, spr2):
    res = dot(spr1, spr2) / (norm(spr1) * norm(spr2))
    return res

if __name__ == '__main__':
    t = [0,0,0,0,0,1, 0, 0, 0, 0, 5, 0, 0, 0, 9, 0]
    spr = sparseForm(t)
    print(spr)
    print(revert(spr))
    print("done")