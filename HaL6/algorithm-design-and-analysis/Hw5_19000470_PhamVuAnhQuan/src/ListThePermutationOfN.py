#!/usr/bin/env python

import traceback

# Bài toán liệt kê tất cả các hoán vị của tập n phần tử

'''
- Phân tích bài toán:
    - Tập ta cần phân tích gồm các phần tử lần lượt từ 1..n
    - Tập sẽ có n! hoán vị

- Thuật toán:
    - Với mỗi hoán vị, ta chọn phần tử trong tập chưa có trong hoán vị đó.
    - Sau đó lưu nó vào hoán vịvà đánh dấu là phần tử này đã tồn tại trong hoán vị.
    - Lặp lại công việc trên cho đến khi đạt được 1 hoán vị hoàn chỉnh.
    - In ra màn hình hoán vị vừa tìm được và quay lui lại để tìm hoán vị khác.
'''

def solve(n: int) -> None:
    check = [False for i in range(n)]
    permutation = [0 for i in range(n)]
    solve1(n, check, permutation)

def solve1(n: int, check: list[bool], permutation: list[int], k: int = 0) -> None:
    for i in range(0, n):
        if check[i] == False:
            permutation[k] = i+1
            check[i] = True
            if k == n-1:
                print(permutation)
            else:
                solve1(n, check, permutation, k+1)
            check[i] = False


if __name__ == "__main__":
    try:
        n = int(input('n = ?\n'))
        solve(n) if n > 0 else print('n > 0, plz')
    except Exception:
        traceback.print_exc()
