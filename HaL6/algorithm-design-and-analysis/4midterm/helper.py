import time
import random
import dijkstra
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from networkx.generators.random_graphs import erdos_renyi_graph

def generate_random_graph(nums_of_vertices, p=round(random.uniform(0.2, 1), 2), min_distance=1, max_distance=20):
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
    
def draw_graph(g):
    pos = nx.spring_layout(g)
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')
    plt.title('Graph')
    plt.show()
    
def calculate_execution_time(g):
    adjacency_matrix = to_adjacency_matrix(g)
    start_time = time.time_ns()
    dijkstra.dijkstra(adjacency_matrix, 0)
    finish_time = time.time_ns()
    return finish_time-start_time
    
def evaluate(k=6, test_times=50):
    list_of_number_of_vertices = [10*i for i in range(1, k+1)]
    list_of_p = [0.1*i for i in range(1, 11)]
    list_of_execution_times = list()
    
    for i in range(len(list_of_number_of_vertices)):
        for j in range(len(list_of_p)):
            execution_time = list()
            for l in range(test_times):
                g = generate_random_graph(list_of_number_of_vertices[i], list_of_p[j])
                execution_time.append(calculate_execution_time(g))
            list_of_execution_times.append(sum(execution_time)/len(execution_time))

    list_of_p *= k
    list_of_number_of_vertices = sorted(list_of_number_of_vertices*10)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(list_of_number_of_vertices, list_of_p, list_of_execution_times)
    ax.set_xlabel('Number of vertices')
    ax.set_ylabel('Probability for edge creation')
    ax.set_zlabel('Execution time')
    plt.show()
    
# testing
# g = generate_random_graph(5)
# print(to_adjacency_matrix(g))
# draw_graph(g)