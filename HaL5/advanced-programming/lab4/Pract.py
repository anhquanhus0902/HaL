#!/usr/bin/env python

def findUniq(a):
    sum_lst = 0
    st = set()
    for i in a:
        sum_lst += i
        st.add(i)
    return sum(st)*2 - sum_lst

if __name__ == "__main__":
    a = [1,2,3,2,3,1,4,5,4]
    print(findUniq(a))
