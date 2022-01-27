#!/usr/bin/env python

import re
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"^q.", "Quan", re.IGNORECASE)
print(result)
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"dogs|cats", "I love dogs and cats"))
print(re.findall(r"dogs|cats", "I love dogs and cats"))
