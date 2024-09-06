from .representacao import criar_lista_de_adjacencia, criar_matriz_de_adjacencia
from .busca import bfs, dfs
from .componentes import achar_conexos
from .io import le_grafo, escreve_grafo
from .grafo_com_pesos import GrafoPeso

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_vertices, representation="list"):
        self.num_vertices = num_vertices
        self.arestas = 0
        
        if representation == "matrix":
            self.grafo = criar_matriz_de_adjacencia(num_vertices)
        else:
            self.grafo = criar_lista_de_adjacencia(num_vertices)
    
    def add_aresta(self, v1, v2):
        self.arestas += 1
        if isinstance(self.grafo, list):
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
        else:
            self.grafo[v1][v2] = 1
            self.grafo[v2][v1] = 1
    
    def bfs(self, vertice_ini):
        return bfs(self.grafo, vertice_ini)
    
    def dfs(self, vertice_ini):
        return dfs(self.grafo, vertice_ini)
    
    def achar_conexos(self):
        return achar_conexos(self.grafo)
    
    @classmethod
    def from_file(cls, filename, representation="list"):
        num_vertices, arestas = le_grafo(filename)
        grafo = cls(num_vertices, representation)
        for v1, v2 in arestas:
            grafo.add_aresta(v1 - 1, v2 - 1)
        return grafo
    
    def to_file(self, filename):
        escreve_grafo(self.num_vertices, self.arestas, self.grafo, filename)
        
    def cria_img_grafo(self, filename="grafo.png"):
        G = nx.Graph()

        # add arestas ao grafo
        if isinstance(self.grafo, list):
            for i, vizinhos in enumerate(self.grafo):
                for vizinho in vizinhos:
                    if i < vizinho:  # evitar duplicação de arestas
                        G.add_edge(i + 1, vizinho + 1)
        else:
            for i in range(self.num_vertices):
                for j in range(i + 1, self.num_vertices):
                    if self.grafo[i][j] == 1:
                        G.add_edge(i + 1, j + 1)

        # Desenha o grafo e salva a imagem
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
        plt.savefig(filename)
        plt.close()
        
    def encontra_menor_caminho(self, vertice_ini, target_vertex=None):
        if isinstance(self, GrafoPeso):
            return self.menor_caminho(vertice_ini, target_vertex)  # usa Dijkstra
        else:
            return self.bfs(vertice_ini, target_vertex)  # usa BFS
