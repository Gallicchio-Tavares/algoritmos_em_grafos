from collections import deque

def bfs(grafo, vertice_ini):
    num_vertices = len(grafo)
    visitado = [False] * num_vertices
    pai = [-1] * num_vertices
    nivel = [-1] * num_vertices
    queue = deque([vertice_ini])
    
    visitado[vertice_ini] = True
    nivel[vertice_ini] = 0
    
    while queue:
        vertice = queue.popleft()
        
        vizinhos = range(num_vertices) if isinstance(grafo, list) else grafo[vertice]
        for vizinho in vizinhos:
            if isinstance(grafo, list) and vizinho not in grafo[vertice]:
                continue
            if not visitado[vizinho]:
                visitado[vizinho] = True
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1
                queue.append(vizinho)
    
    return pai, nivel

def dfs(grafo, vertice_ini):
    num_vertices = len(grafo)
    visitado = [False] * num_vertices
    pai = [-1] * num_vertices
    nivel = [-1] * num_vertices
    
    def dfs_visit(vertice, depth):
        visitado[vertice] = True
        nivel[vertice] = depth
        
        vizinhos = range(num_vertices) if isinstance(grafo, list) else grafo[vertice]
        for vizinho in vizinhos:
            if isinstance(grafo, list) and vizinho not in grafo[vertice]:
                continue
            if not visitado[vizinho]:
                pai[vizinho] = vertice
                dfs_visit(vizinho, depth + 1)
    
    dfs_visit(vertice_ini, 0)
    return pai, nivel
