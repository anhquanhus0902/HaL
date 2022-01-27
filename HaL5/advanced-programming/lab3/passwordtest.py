#!/usr/bin/env python

def checkPassword(s):
    number='0123456789'
    Cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alp='abcdefghijklmnopqrstuvwxyz'
    special='~!@#$%^&*'

    checkNumber, checkCap, checkAlp, checkSpe = False, False, False, False

    if len(s) >= 8:
        for c in s:
            if c in number:
                checkNumber = True
            elif c in Cap:
                checkCap = True
            elif c in alp:
                checkAlp = True
            elif c in special:
                checkSpe = True
        return checkNumber and checkCap and checkAlp and checkSpe
    else:
        return False

