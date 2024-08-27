def create_adjacency_list(num_vertices):
    return [[] for _ in range(num_vertices)]

def create_adjacency_matrix(num_vertices):
    return [[0] * num_vertices for _ in range(num_vertices)]
