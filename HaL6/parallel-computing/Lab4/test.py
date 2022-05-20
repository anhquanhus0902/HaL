#!/usr/bin/env python

# global variables
password = None
characters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)]
#characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['a', 'b', 'c']
n = len(characters)
solved = False

def solve(r: int, pre: str = '') -> None:
    global solved
    if r==0:
        return
    for i in range(n):
        if solved:
            return
        prd = pre + characters[i]
        print(prd)
        if prd == password:
            print('your password is', prd)
            solved = True
        solve(r-1, prd)
    

if __name__ == '__main__':
    password = input('your password (a-z0-9 length=3..5): ')
    solve(3)
    if not solved:
        print('not found')
