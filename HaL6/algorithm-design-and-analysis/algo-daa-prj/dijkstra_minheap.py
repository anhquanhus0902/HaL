#!/usr/bin/env python

'''
Dijkstra algorithm with Min Heap DS
'''

from heapq import heapify, heappush, heappop
import traceback
import helper
from math import inf
from typing import List, Tuple, Dict

test_weight_matrix = [
                    [0, 3, 0, 7, 0],
                    [3, 0, 4, 2, 0],
                    [0, 4, 0, 5, 6],
                    [7, 2, 5, 0, 4],
                    [0, 0, 6, 4, 0]
                   ]

def dijkstra_heap(weight_matrix: List[List[int]], source_vertex: int) -> Tuple[Dict[int,int]]:
    n = len(weight_matrix)
    V = set()
    d, p, flag = dict(), dict(), dict()
    min_heap = []
    heapify(min_heap)
    for v in range(n):
        V.add(v)
        d[v] = inf if v != source_vertex else 0
        flag[v] = False
        p[v] = None
    heappush(min_heap, (source_vertex, d[source_vertex]))
    for _ in range(n):
        u_star = heappop(min_heap)[0]
        flag[u_star] = True
        for u in V:
            if flag[u] == False:
                weight = weight_matrix[u_star][u]
                if weight != 0 and d[u_star] + weight < d[u]:
                    d[u] = d[u_star] + weight
                    p[u] = u_star
                    heappush(min_heap, (u, d[u]))
    return (d,p)  
    
if __name__ == "__main__":
    try:
        res = dijkstra_heap(test_weight_matrix, 0)
        print(res[0])
        print(res[1])
        if input('evaluate (Y/n) ').lower() == 'y':
            helper.evaluate(dijkstra_heap, 5, 1)
        else:
            print('glhf')
    except Exception:
        traceback.print_exc()   