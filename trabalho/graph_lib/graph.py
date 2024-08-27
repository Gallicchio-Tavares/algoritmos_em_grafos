from .representation import create_adjacency_list, create_adjacency_matrix
from .search import bfs, dfs
from .components import find_connected_components
from .io import read_graph_data_from_file, write_graph_data_to_file

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_vertices, representation="list"):
        self.num_vertices = num_vertices
        self.edges = 0
        
        if representation == "matrix":
            self.graph = create_adjacency_matrix(num_vertices)
        else:
            self.graph = create_adjacency_list(num_vertices)
    
    def add_edge(self, v1, v2):
        self.edges += 1
        if isinstance(self.graph, list):
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
        else:
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1
    
    def bfs(self, start_vertex):
        return bfs(self.graph, start_vertex)
    
    def dfs(self, start_vertex):
        return dfs(self.graph, start_vertex)
    
    def find_connected_components(self):
        return find_connected_components(self.graph)
    
    @classmethod
    def from_file(cls, filename, representation="list"):
        num_vertices, edges = read_graph_data_from_file(filename)
        graph = cls(num_vertices, representation)
        for v1, v2 in edges:
            graph.add_edge(v1 - 1, v2 - 1)
        return graph
    
    def to_file(self, filename):
        write_graph_data_to_file(self.num_vertices, self.edges, self.graph, filename)
        
    def draw_graph(self, filename="graph.png"):
        G = nx.Graph()

        # add arestas ao grafo
        if isinstance(self.graph, list):
            for i, neighbors in enumerate(self.graph):
                for neighbor in neighbors:
                    if i < neighbor:  # evitar duplicação de arestas
                        G.add_edge(i + 1, neighbor + 1)
        else:
            for i in range(self.num_vertices):
                for j in range(i + 1, self.num_vertices):
                    if self.graph[i][j] == 1:
                        G.add_edge(i + 1, j + 1)

        # Desenha o grafo e salva a imagem
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
        plt.savefig(filename)
        plt.close()
