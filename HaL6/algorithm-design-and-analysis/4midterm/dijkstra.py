#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import helper

'''
Python program implementing Dijkstra's algoritm
'''

INF = 10**1000 - 1

# page 362
test_adjacency_matrix = [
                    [0, 3, 0, 7, 0],
                    [3, 0, 4, 2, 0],
                    [0, 4, 0, 5, 6],
                    [7, 2, 5, 0, 4],
                    [0, 0, 6, 4, 0]
                   ]

def dijkstra(adjacency_matrix, source_vertex):
    n = len(adjacency_matrix)
    V, Vt = set(), set()
    d, p, Q = dict(), dict(), dict()
    for v in range(n):
        V.add(v)
        d[v] = INF if v != source_vertex else 0
        p[v] = None
        Q[v] = d[v]
    
    for i in range(n):
        u_star = min(Q, key=Q.get)
        del Q[u_star]
        Vt.add(u_star)
        for u in V-Vt:
            weight = adjacency_matrix[u_star][u]
            if weight != 0 and d[u_star] + weight < d[u]:
                d[u] = d[u_star] + weight
                p[u] = u_star
                Q[u] = d[u]
    return (d, p)

if __name__ == "__main__":
    try:
        # g = helper.generate_random_graph(5)
        # adjacency_matrix = helper.to_adjacency_matrix(g)
        g = helper.adjacency_matrix_to_networkx_graph(test_adjacency_matrix)
        helper.draw_graph(g)
        d, p = dijkstra(test_adjacency_matrix, 0)
        print('d:', d)
        print('p:', p)
        if input('evaluate? (Y/n): ').lower() == 'y':
            helper.evaluate()
        else:
            print('bye :v')
    except:
        traceback.print_exc()