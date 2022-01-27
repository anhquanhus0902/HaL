#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    f = eval(equation)
    return f

def bisection_method(a, b, max_iteration):
    for _ in range(max_iteration):
        m = (a+b)/2
        if f(m) == 0:
            print(m)
            break
        elif f(m) * f(a) < 0:
            b = m
        elif f(m) * f(b) < 0:
            a = m
        if _ == max_iteration-1:
            print(m)

def phuong_phap_day_cung(a, b, max_iteration):
    x = a
    f_b = f(b)
    for _ in range(max_iteration):
        f_x = f(x)
        x = x - f_x * ((b - x)/(f_b - f_x))
    print(x)

def phuong_phap_cat_tuyen(a, b, max_iteration):
    x_pre = a
    x = x_pre + 0.01
    for _ in range(max_iteration):
        f_x = f(x)
        x_tmp = x
        if (f_x - f(x_pre) == 0):
            break
        x = x - f_x * ((x - x_pre)/(f_x - f(x_pre)))
        x_pre = x_tmp
    print(x)

def iteration_method(a, b, q,  max_iteration):
    pass

if __name__ == "__main__":
    equation = input("Nhap phuong trinh: ")
    x = np.linspace(start=-5, stop=5, num=100)
    y = f(x)
    plt.plot(x, y, color="black")
    x_tmp = np.zeros(y.shape)
    y_tmp = np.zeros(x.shape)
    plt.plot(x, y_tmp, color="black")
    plt.plot(x_tmp, y, color="black")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

    print("Ban muon giai bang phuong phap nao?")
    method = int(input("0: Chia doi | 1: Day cung | 2: Cat tuyen | 3: Lap don: "))
    a = float(input("a: "))
    b = float(input("b: "))
    max_iteration = int(input("So lan lap toi da: ")) 
    if method == 0:
        bisection_method(a, b, max_iteration)
    elif method == 1:
        phuong_phap_day_cung(a, b, max_iteration)
    elif method == 2:
        phuong_phap_cat_tuyen(a, b, max_iteration)
    elif method == 3:
        iteration_method(a, b, max_iteration)
