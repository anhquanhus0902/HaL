#!/usr/bin/env python

import traceback
from typing import List, Tuple

def isValidFilePath(path: str) -> bool:
    path = path.replace('\\', '/')
    try:
        f = open(path, 'r')
        f.close()
        return True
    except:
        return False

def getInput() -> Tuple[List[str], str]:
    textData = input('(if you enter a valid file path, you can keep it as text data or get text data from the file with that path)\nEnter the text data:\n')
    if isValidFilePath(textData):
        choiceSelectedByUser = input('you entered a valid file path. do you want to use text data from this file? (Y/n): ').lower()
        if choiceSelectedByUser == 'y':
            with open(textData) as f:
                textData = [line.rstrip() for line in f]
    if not type(textData) is list:
        textData = [textData]
    pattern = input('Enter the pattern string:\n')
    return (textData, pattern)

def solve(textData: List[str], pattern: str) -> Tuple[int, int]:
    lenOfTextData = len(textData)
    m = len(pattern)
    for i in range(lenOfTextData):
        n = len(textData[i])
        for j in range(n-m+1):
            k = 0
            while k < m and pattern[k] == textData[i][j+k]:
                k += 1
            if k == m:
                return (j+1, i+1)
    return (-1, -1)

if __name__ == "__main__":
    try:
        textData, pattern = getInput()
        res = solve(textData, pattern)
        print('column (index): {}, row: {}'.format(res[0], res[1]))
    except Exception:
        traceback.print_exc()
