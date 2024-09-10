import heapq

def dijkstra(grafo, vertice_ini): #alg de dijkstra usando heap
    num_vertices = len(grafo)
    distancias = [float('inf')] * num_vertices
    distancias[vertice_ini] = 0
    pai = [-1] * num_vertices
    pq = [(0, vertice_ini)]  # (min-heap)
    
    while pq:
        atual_distancia, vertice = heapq.heappop(pq) 
        
        if atual_distancia > distancias[vertice]:
            continue
        
        for vizinho, peso in grafo[vertice]:
            distancia = atual_distancia + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                pai[vizinho] = vertice
                heapq.heappush(pq, (distancia, vizinho))
    
    return distancias, pai

def get_menor_caminho(pai, vertice_alvo):
    caminho = []
    atual = vertice_alvo
    while atual != -1:
        caminho.append(atual)
        atual = pai[atual]
    caminho.reverse()
    return caminho
