from collections import deque

def bfs(graph, start_vertex):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    parent = [-1] * num_vertices
    level = [-1] * num_vertices
    queue = deque([start_vertex])
    
    visited[start_vertex] = True
    level[start_vertex] = 0
    
    while queue:
        vertex = queue.popleft()
        
        neighbors = range(num_vertices) if isinstance(graph, list) else graph[vertex]
        for neighbor in neighbors:
            if isinstance(graph, list) and neighbor not in graph[vertex]:
                continue
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = vertex
                level[neighbor] = level[vertex] + 1
                queue.append(neighbor)
    
    return parent, level

def dfs(graph, start_vertex):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    parent = [-1] * num_vertices
    level = [-1] * num_vertices
    
    def dfs_visit(vertex, depth):
        visited[vertex] = True
        level[vertex] = depth
        
        neighbors = range(num_vertices) if isinstance(graph, list) else graph[vertex]
        for neighbor in neighbors:
            if isinstance(graph, list) and neighbor not in graph[vertex]:
                continue
            if not visited[neighbor]:
                parent[neighbor] = vertex
                dfs_visit(neighbor, depth + 1)
    
    dfs_visit(start_vertex, 0)
    return parent, level
