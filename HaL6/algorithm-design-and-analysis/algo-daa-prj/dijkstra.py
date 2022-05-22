#!/usr/bin/env python

'''
Original Dijkstra algorithm
'''

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

def dijkstra4v(weight_matrix: List[List[int]] = test_weight_matrix, source_vertex: int = 0) -> Tuple[Dict[int,int]]:
    steps_data = ''
    helper.set_g(weight_matrix)
    n = len(weight_matrix)
    V = set()
    d, p, flag = dict(), dict(), dict()
    for v in range(n):
        V.add(v)
        d[v] = inf if v != source_vertex else 0
        flag[v] = False
        p[v] = None
    for _ in range(n):
        maxdis = inf
        for v in range(n):
            if d[v] < maxdis and flag[v] == False:
                u_star = v
                maxdis = d[v]
        flag[u_star] = True
        steps_data += 'current vertex: {}\nd: {}\np: {}\nvisited: {}\n'.format(u_star, d, p, flag)
        helper.visualize_graph(u_star)
        for u in V:
            if (flag[u] == False):
                weight = weight_matrix[u_star][u]
                if weight != 0:
                    helper.visualize_graph(u_star, (u, u_star))
                    if d[u_star] + weight < d[u]:
                        d[u] = d[u_star] + weight
                        p[u] = u_star
                    steps_data += 'current vertex: {}\nd: {}\np: {}\nvisited: {}\n'.format(u_star, d, p, flag)
    helper.write_steps(steps_data)
    return (d,p)

def dijkstra(weight_matrix: List[List[int]] = test_weight_matrix, source_vertex: int = 0) -> Tuple[Dict[int,int]]:
    n = len(weight_matrix)
    V = set()
    d, p, flag = dict(), dict(), dict()
    for v in range(n):
        V.add(v)
        d[v] = inf if v != source_vertex else 0
        flag[v] = False
        p[v] = None
    for _ in range(n):
        maxdis = inf;
        for v in range(n):
            if d[v] < maxdis and flag[v] == False:
                u_star = v
                maxdis = d[v]
        flag[u_star] = True
        for u in V:
            if (flag[u] == False):
                weight = weight_matrix[u_star][u]
                if weight != 0:
                    if d[u_star] + weight < d[u]:
                        d[u] = d[u_star] + weight
                        p[u] = u_star
    return (d,p)


if __name__ == "__main__":
    try:
        #test2 = helper.generate_random_graph(7, 0.9)
        #test3 = helper.to_adjacency_matrix(test2)
        #res = dijkstra4v(test3, 4)
        res = dijkstra4v(test_weight_matrix, 0)
        print(res[0])
        print(res[1])
        # if input('evaluate (Y/n) ').lower() == 'y':
        #     helper.evaluate(dijkstra, 5, 1)
        # else:
        #     print('glhf')
    except Exception:
        traceback.print_exc()
