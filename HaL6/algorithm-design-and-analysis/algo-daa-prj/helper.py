import time
import random
import os
import string
from dijkstra import *
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import erdos_renyi_graph

dirid = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))
count = 0
visited = set()
os.makedirs(dirid)
f = open('path.txt', 'w')
f.write(dirid)
f.close()

def generate_random_graph(nums_of_vertices, p=round(random.uniform(0.5, 1), 2), min_distance=1, max_distance=20):
    random_graph = erdos_renyi_graph(nums_of_vertices, p)
    for (u, v) in random_graph.edges():
        random_graph.edges[u, v]['weight'] = random.randint(min_distance, max_distance)
    return random_graph
    
def to_adjacency_matrix(g):
    number_of_vertices = g.number_of_nodes()
    list_of_edges = list(g.edges)
    adjacency_matrix = [[0 for j in range(number_of_vertices)] for i in range(number_of_vertices)]
    for edge in list_of_edges:
        u, v = edge
        weight = g.edges[u, v]['weight']
        adjacency_matrix[u][v] = weight
        adjacency_matrix[v][u] = weight
    return adjacency_matrix
    
def adjacency_matrix_to_networkx_graph(adjacency_matrix):
    n = len(adjacency_matrix)
    g = nx.Graph()
    for i in range(n):
        g.add_node(i)
        for j in range(n):
            weight = adjacency_matrix[i][j]
            if weight != 0:
                g.add_edge(i, j, weight=weight)
    return g

def set_g(mtx):
    global g, pos, edge_labels, edges, nodes
    g = adjacency_matrix_to_networkx_graph(mtx)
    edges = list(g.edges)
    nodes = list(g.nodes)
    pos = nx.spring_layout(g)
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')
    plt.title('Graph')
    
def draw_graph():
    global g, pos, edge_labels
    plt.show()

def visualize_graph(current_node=None, edge=(-9312312321, 42342323)):
    if current_node != None:
        edge_color = ['#F0FF00' if (edge == edges[i] or edge[::-1] == edges[i]) else 'black' for i in range(len(edges))]
        node_color = [None for _ in range(len(nodes))]
        for i in range(len(nodes)):
            if nodes[i] in visited:
                node_color[i] = 'green'
            elif nodes[i] == current_node:
                node_color[i] = 'red'
            else:
                node_color[i] = 'white'
        nx.draw_networkx(g, pos, node_color=node_color, edge_color=edge_color)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')
        visited.add(current_node)
    save_graph_image()
    if len(visited) == len(nodes):
        visualize_graph(-19052022)

def write_steps(steps_data):
    f = open('steps.txt', 'w')
    f.write(steps_data)
    f.close()

def write_paths(paths):
    paths2 = '\n'.join(paths)
    f = open('path.txt', 'a')
    f.write('\n')
    f.write(paths2)
    f.close()

def save_graph_image():
    global count, dirid
    plt.savefig('{}/{}.jpg'.format(dirid, count))
    count += 1
    
def calculate_execution_time(func, g):
    adjacency_matrix = to_adjacency_matrix(g)
    start = time.time_ns()
    func(adjacency_matrix, 0)
    end = time.time_ns()
    return (end-start)/1e9
    
def evaluate(func, k=5, test_times=50):
    list_of_number_of_vertices = [100*i for i in range(1, k+1)]
    list_of_execution_times = list()
    
    for i in range(len(list_of_number_of_vertices)):
        total_execution_time = 0
        for j in range(test_times):
            g = generate_random_graph(list_of_number_of_vertices[i], 1)
            total_execution_time += calculate_execution_time(func, g)
        list_of_execution_times.append(total_execution_time/test_times)
    plt.clf()
    plt.plot(list_of_number_of_vertices, list_of_execution_times)
    plt.xlabel('Number of vertices')
    plt.ylabel('Execution time (sec)')
    plt.title('Evaluate')
    plt.show()
    
# testing
# g = generate_random_graph(5)
# print(to_adjacency_matrix(g))
# draw_graph(g)