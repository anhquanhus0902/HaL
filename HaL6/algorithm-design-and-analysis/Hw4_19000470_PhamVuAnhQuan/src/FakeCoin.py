#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import traceback
from math import ceil

sys.stdout.reconfigure(encoding='utf-8')

# Fake-coin problem

'''
- Phân tích bài toán:
    - Có n đồng xu, trong đó có 1 đồng xu là giả (nó nhẹ hơn các đồng xu thật). 
    - Ta có một cái cân dùng để so sánh hai bộ đồng xu nhưng không cho ta biết mức độ chênh lệch của 2 bộ.
    
- Thuật toán:
    - Đầu tiên, ta chia n đồng xu thành 2 chồng, mỗi chồng có [n/2] đồng xu. Trong trường hợp n là số lẻ, đồng xu bịlẻ sẽ được bỏ sang một bên.
    - Sau đó, ta đặt 2 chồng này lên cân.
        - Nếu khối lượng 2 chồng là cân bằng, đồng xu bị lẻ là đồng xu giả.
        - Nếu có sự chênh lệch, ta thực hiện lại thao tác vừa rồi với chồng nhẹ hơn (vì chồng đó nhẹ hơn nên chắc chắn đồng xu giả nằm trong đó).
'''

def createRandomCoins(n: int) -> list:
    indexOfFakeCoin = random.randint(0, n-1)
    coins = [0 if i == indexOfFakeCoin else 1 for i in range(n)]
    return coins    

def findFakeCoin(coins: list, sizeOfPile=0) -> None:
    n = len(coins)
    n = n-1 if n%2 == 1 else n
    mid = ceil(n/2)
    pileOfCoins1 = coins[0:mid]
    pileOfCoins2 = coins[mid:n]
    weightOfCoinsPile1 = sum(pileOfCoins1)
    weightOfCoinsPile2 = sum(pileOfCoins2)
    if weightOfCoinsPile1 == weightOfCoinsPile2:
        print('Index of the fake coin is: {}'.format(n+sizeOfPile))
    else:
        findFakeCoin(pileOfCoins1, sizeOfPile) if weightOfCoinsPile1 < weightOfCoinsPile2 else findFakeCoin(pileOfCoins2, sizeOfPile+mid)
    
def solve(n: int) -> None:
    coins = createRandomCoins(n)
    print(coins)
    findFakeCoin(coins)

if __name__ == "__main__":
    try:
        n = int(input('Số lượng đồng xu: '))
        solve(n) if n > 0 else print('n phải lớn hơn 0')
    except Exception:
        traceback.print_exc()
