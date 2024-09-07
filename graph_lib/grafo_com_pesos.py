from .representacao import criar_lista_de_adjacencia_peso, criar_matriz_de_adjacencia_peso
from .caminho_minimo import dijkstra, get_menor_caminho

class GrafoPeso:
    def __init__(self, num_vertices, representation="list"):
        self.num_vertices = num_vertices
        self.arestas = 0
        
        if representation == "matrix":
            self.grafo = criar_matriz_de_adjacencia_peso(num_vertices)
        else:
            self.grafo = criar_lista_de_adjacencia_peso(num_vertices)
    
    def add_aresta(self, v1, v2, peso):
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
                grafo.add_aresta(int(v1) - 1, int(v2) - 1, float(peso))
        return grafo
    
    def to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"# n = {self.num_vertices}\n")
            f.write(f"# m = {self.arestas}\n")
            # Implementação similar para a saída com pesos

    def menor_caminho(self, vertice_ini, vertice_alvo=None):
        # verificacao pra poder usar o alg de dijkstra
        if self.verifica_pesos_negativos():
            raise ValueError("O grafo contém pesos negativos. O algoritmo de Dijkstra não pode ser aplicado.")

        distancias, pai = dijkstra(self.grafo, vertice_ini)
        
        if vertice_alvo is not None:
            caminho = get_menor_caminho(pai, vertice_alvo)
            return distancias[vertice_alvo], caminho
        else:
            return distancias, pai

    def verifica_pesos_negativos(self):
        for vizinhos in self.grafo:
            for _, peso in vizinhos:
                if peso < 0:
                    return True
        return False