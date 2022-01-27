#!/usr/bin/env python

import re

def checkPassword(s):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@#$%^&*])[a-zA-Z0-9~!@#$%^&*]{8,}$"
    res = re.search(regex, s)
    if res is None:
        return False
    else:
        return True

if __name__ == "__main__":
    s = input()
    print(checkPassword(s))
