import random
from .representacao import criar_lista_de_adjacencia, criar_matriz_de_adjacencia
from .busca import bfs, dfs
from .componentes import achar_conexos
from .io import le_grafo, escreve_grafo
from .grafo_com_pesos import GrafoPeso

import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
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
            return self.bfs_menor_caminho(vertice_ini, target_vertex)  # usa BFS
    
    def bfs_menor_caminho(self, vertice_ini, vertice_alvo=None):
    # Usa o BFS para calcular o menor caminho (grafo não ponderado)
        pai, _ = bfs(self.grafo, vertice_ini)
        
        if vertice_alvo is not None:
            caminho = []
            atual = vertice_alvo
            while atual != -1:
                caminho.append(atual)
                atual = pai[atual]
            caminho.reverse()
            return caminho
        else:
            return pai
        
    def visualizar_componentes_conexos(self, filename="grafo_componentes.png"):
        componentes = self.achar_conexos()  # Obtém os componentes conexos
        G = nx.Graph()

        # Adiciona as arestas ao grafo NetworkX
        if isinstance(self.grafo, list):
            for i, vizinhos in enumerate(self.grafo):
                for vizinho in vizinhos:
                    if i < vizinho:  # Evitar duplicação de arestas
                        G.add_edge(i + 1, vizinho + 1)
        else:
            for i in range(self.num_vertices):
                for j in range(i + 1, self.num_vertices):
                    if self.grafo[i][j] == 1:
                        G.add_edge(i + 1, j + 1)

        # Gerar cores diferentes para cada componente
        cores_componentes = {}
        for idx, componente in enumerate(componentes):
            cor = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
            for vertice in componente:
                cores_componentes[vertice + 1] = cor  # Adiciona +1 para ajustar o índice ao `networkx`

        # Desenhar o grafo com cores para os componentes
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=[cores_componentes[node] for node in G.nodes()],
                edge_color='gray', node_size=500, font_size=10)

        # Salvar a imagem
        plt.savefig(filename)
        plt.close()
