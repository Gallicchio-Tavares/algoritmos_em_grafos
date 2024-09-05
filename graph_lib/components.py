def find_connected_components(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    components = []
    
    def dfs_component(vertex, component):
        visited[vertex] = True
        component.append(vertex)
        
        neighbors = range(num_vertices) if isinstance(graph, list) else graph[vertex]
        for neighbor in neighbors:
            if isinstance(graph, list) and neighbor not in graph[vertex]:
                continue
            if not visited[neighbor]:
                dfs_component(neighbor, component)
    
    for vertex in range(num_vertices):
        if not visited[vertex]:
            component = []
            dfs_component(vertex, component)
            components.append(component)
    
    components.sort(key=len, reverse=True)
    return components
