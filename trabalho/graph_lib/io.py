def read_graph_data_from_file(filename):
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        edges = []
        for line in f:
            v1, v2 = map(int, line.strip().split())
            edges.append((v1, v2))
    return num_vertices, edges

def write_graph_data_to_file(num_vertices, edges, graph, filename):
    with open(filename, 'w') as f:
        f.write(f"# n = {num_vertices}\n")
        f.write(f"# m = {edges}\n")
        
        degree_sum = sum(len(neighbors) if isinstance(graph, list) else sum(row) 
                         for row, neighbors in zip(graph, graph))
        degree_avg = degree_sum / num_vertices
        f.write(f"# d_medio = {degree_avg:.1f}\n")
        
        degree_count = [0] * num_vertices
        for neighbors in graph:
            degree_count[len(neighbors) if isinstance(graph, list) else sum(neighbors)] += 1
        
        for degree, count in enumerate(degree_count):
            if count > 0:
                f.write(f"{degree} {count / num_vertices:.2f}\n")
