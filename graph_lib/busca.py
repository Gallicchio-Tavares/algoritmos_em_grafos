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
        
        if isinstance(grafo[vertice], list) and isinstance(grafo[vertice][0], int):
            vizinhos = grafo[vertice]
        else:
            vizinhos = [vizinho for vizinho, _ in grafo[vertice]]

        for vizinho in vizinhos:
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

        if isinstance(grafo[vertice], list) and isinstance(grafo[vertice][0], int):
            vizinhos = grafo[vertice]
        else:
            vizinhos = [vizinho for vizinho, _ in grafo[vertice]]

        for vizinho in vizinhos:
            if not visitado[vizinho]:
                pai[vizinho] = vertice
                dfs_visit(vizinho, depth + 1)
    
    dfs_visit(vertice_ini, 0)
    return pai, nivel
