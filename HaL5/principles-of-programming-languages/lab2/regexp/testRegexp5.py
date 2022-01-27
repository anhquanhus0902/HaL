#!/usr/bin/env python

import re

if __name__ == "__main__":
    regexp = r"[.?!]"
    sentence = input()
    print(re.split(regexp, sentence))
    result = re.sub(r"[\w.%+-]+@[\w.-]+", "[CENSORED]", "My email is pvaquans22@gmail.com")
    print(result)
