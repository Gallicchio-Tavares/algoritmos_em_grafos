def criar_lista_de_adjacencia(num_vertices):
    return [[] for _ in range(num_vertices)]

def criar_matriz_de_adjacencia(num_vertices):
    return [[0] * num_vertices for _ in range(num_vertices)]

def criar_lista_de_adjacencia_peso(num_vertices):
    return [[] for _ in range(num_vertices)]

def criar_matriz_de_adjacencia_peso(num_vertices):
    return [[float('inf')] * num_vertices for _ in range(num_vertices)]
