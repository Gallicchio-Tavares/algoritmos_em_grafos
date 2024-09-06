def le_grafo(filename):
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        arestas = []
        for linha in f:
            v1, v2 = map(int, linha.strip().split())
            arestas.append((v1, v2))
    return num_vertices, arestas

def escreve_grafo(num_vertices, arestas, grafo, filename):
    with open(filename, 'w') as f:
        f.write(f"# n = {num_vertices}\n")
        f.write(f"# m = {arestas}\n")
        
        grau_soma = sum(len(vizinhos) if isinstance(grafo, list) else sum(coluna) 
                         for coluna, vizinhos in zip(grafo, grafo))
        media_grau = grau_soma / num_vertices
        f.write(f"# d_medio = {media_grau:.1f}\n")
        
        conta_grau = [0] * num_vertices
        for vizinhos in grafo:
            conta_grau[len(vizinhos) if isinstance(grafo, list) else sum(vizinhos)] += 1
        
        for grau, cont in enumerate(conta_grau):
            if cont > 0:
                f.write(f"{grau} {cont / num_vertices:.2f}\n")
                
def le_grafo_com_peso(filename):
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        arestas = []
        for linha in f:
            v1, v2, peso = linha.strip().split()
            arestas.append((int(v1), int(v2), float(peso)))
    return num_vertices, arestas

def escreve_grafo_com_peso(num_vertices, arestas, grafo, filename):
    with open(filename, 'w') as f:
        f.write(f"# n = {num_vertices}\n")
        f.write(f"# m = {arestas}\n")
        for v1 in range(num_vertices):
            for v2, peso in grafo[v1]:
                f.write(f"{v1+1} {v2+1} {peso}\n")
