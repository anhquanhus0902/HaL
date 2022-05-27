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

def get_paths(p, source_vertex):
    re = [[v] for v in p]
    for v in p:
        u = v
        while True:
            i = p[u]
            if i == None:
                re[v] = '{} to {}: No path'.format(source_vertex, v)
                break
            u = i
            re[v].insert(0, i)
            if i == source_vertex:
                re[v] = ' -> '.join([str(j) for j in re[v]])
                re[v] = '{} to {}: '.format(source_vertex, v) + re[v]
                break
    return re

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
        source_vertex = 0
        # test2 = helper.generate_random_graph(6, 0.5)
        # test3 = helper.to_adjacency_matrix(test2)
        # res = dijkstra4v(test3, source_vertex)
        res = dijkstra4v(test_weight_matrix, source_vertex)
        print(res[0])
        print(res[1])
        paths = get_paths(res[1], source_vertex)
        helper.write_paths(paths)
        for path in paths:
            print(path)
        # if input('evaluate (Y/n) ').lower() == 'y':
        #     helper.evaluate(dijkstra, 5, 1)
        # else:
        #     print('glhf')
    except Exception:
        traceback.print_exc()
