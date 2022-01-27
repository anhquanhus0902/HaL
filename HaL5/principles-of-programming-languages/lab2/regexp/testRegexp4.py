#!/usr/bin/env python

import re

def rearrange_name(name):
    rs = re.search(r"^(\w*), (\w*)$", name)
    if rs is None:
        return name
    return "{} {}".format(rs[2], rs[1])

if __name__ == "__main__":
   name = input()
   print(rearrange_name(name))
