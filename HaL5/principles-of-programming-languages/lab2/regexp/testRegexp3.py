#!/usr/bin/env python

import re

if __name__ == "__main__":
    print(re.search(r"\.com", "anhquan.com"))
    print(re.search(r"\w*", "heoofs_sdfd_dsf"))
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    print(re.search(pattern, "_this_is_a_valid_name"))
