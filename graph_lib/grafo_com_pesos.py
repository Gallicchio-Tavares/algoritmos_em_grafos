from .representacao import criar_lista_de_adjacencia_peso, criar_matriz_de_adjacencia_peso
from .caminho_minimo import dijkstra, get_menor_caminho
from .io import escreve_grafo_com_peso

import networkx as nx
import matplotlib.pyplot as plt

class GrafoPeso:
    def __init__(self, num_vertices, representation="list"):
        self.num_vertices = num_vertices
        self.arestas = 0
        
        if representation == "matrix":
            self.grafo = criar_matriz_de_adjacencia_peso(num_vertices)
        else:
            self.grafo = criar_lista_de_adjacencia_peso(num_vertices)
    
    def _add_aresta(self, v1, v2, peso):
        self.arestas += 1
        if isinstance(self.grafo, list):
            self.grafo[v1].append((v2, peso))
            self.grafo[v2].append((v1, peso))
        else:
            self.grafo[v1][v2] = peso
            self.grafo[v2][v1] = peso
    
    @classmethod
    def from_file(cls, filename, representation="list"):
        with open(filename, 'r') as f:
            num_vertices = int(f.readline().strip())
            grafo = cls(num_vertices, representation)
            for line in f:
                v1, v2, peso = line.strip().split()
                grafo._add_aresta(int(v1) - 1, int(v2) - 1, float(peso))
        return grafo
    
    def to_file(self, filename):
        escreve_grafo_com_peso(self.num_vertices, self.arestas, self.grafo, filename)

    def menor_caminho(self, vertice_ini, vertice_alvo=None):
        # verificacao pra poder usar o alg de dijkstra
        if self._verifica_pesos_negativos():
            raise ValueError("O grafo contém pesos negativos. O algoritmo de Dijkstra não pode ser aplicado.")

        distancias, pai = dijkstra(self.grafo, vertice_ini)
        
        if vertice_alvo is not None:
            caminho = get_menor_caminho(pai, vertice_alvo)
            return distancias[vertice_alvo], caminho
        else:
            return distancias, pai

    def _verifica_pesos_negativos(self):
        for vizinhos in self.grafo:
            for _, peso in vizinhos:
                if peso < 0:
                    return True
        return False

    def cria_img_grafo_peso(self, filename="grafo_peso.png"):
        G = nx.Graph()

        # Adiciona arestas e pesos ao grafo
        if isinstance(self.grafo, list):
            for i, vizinhos in enumerate(self.grafo):
                for vizinho, peso in vizinhos:
                    if i < vizinho:  # Evitar duplicação de arestas
                        G.add_edge(i + 1, vizinho + 1, weight=peso)
        else:
            for i in range(self.num_vertices):
                for j in range(i + 1, self.num_vertices):
                    if self.grafo[i][j] != float('inf'):  # Se existe uma aresta
                        G.add_edge(i + 1, j + 1, weight=self.grafo[i][j])

        # Desenhar o grafo
        pos = nx.spring_layout(G)  # Layout de nós
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

        # Desenhar os pesos das arestas
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Salvar a imagem
        plt.savefig(filename)
        plt.close()