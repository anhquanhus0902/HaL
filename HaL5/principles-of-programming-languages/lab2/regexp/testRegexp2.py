#!/usr/bin/env python

import re

if __name__ == "__main__":
    print(re.search(r"Pyt*n", "Pyn"))
    print(re.search(r"Pyt+n", "Pyn"))
    print(re.search(r"Pyt+n", "Pytn"))
    print(re.search(r"Qua?n", "Quan"))
    print(re.search(r"Qua?n", "Qun"))
    print(re.search(r"an$", "Quan"))
    print(re.search(r"^Q", "Quan"))

