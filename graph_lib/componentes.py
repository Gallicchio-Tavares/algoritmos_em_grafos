def achar_conexos(grafo):
    num_vertices = len(grafo)
    visited = [False] * num_vertices
    componentes = []
    
    def dfs_component(vertice, componente):
        visited[vertice] = True
        componente.append(vertice)
        
        vizinhos = range(num_vertices) if isinstance(grafo, list) else grafo[vertice]
        for vizinho in vizinhos:
            if isinstance(grafo, list) and vizinho not in grafo[vertice]:
                continue
            if not visited[vizinho]:
                dfs_component(vizinho, componente)
    
    for vertice in range(num_vertices):
        if not visited[vertice]:
            componente = []
            dfs_component(vertice, componente)
            componentes.append(componente)
    
    componentes.sort(key=len, reverse=True)
    return componentes
