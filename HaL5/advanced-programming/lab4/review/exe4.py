#!/usr/bin/env python

def my_func():
    "This is the function docstring"
    print("hello world")

if __name__ == "__main__":
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)
    print(my_func.__doc__)

