from graph_lib import Graph

grafo = Graph.from_file('input.txt', representation='list')

# Executar BFS a partir do vértice 0
parent_bfs, level_bfs = grafo.bfs(0)

# Executar DFS a partir do vértice 0
parent_dfs, level_dfs = grafo.dfs(0)

# Mostrar os níveis dos vértices para BFS
print("Níveis dos vértices (BFS) a partir do vértice 0:")
for v in range(len(level_bfs)):
    print(f"Vértice {v}: Nível {level_bfs[v]}")

# Mostrar os níveis dos vértices para DFS
print("\nNíveis dos vértices (DFS) a partir do vértice 0:")
for v in range(len(level_dfs)):
    print(f"Vértice {v}: Nível {level_dfs[v]}")

# Mostrar a árvore de busca (pais de cada vértice) para BFS
print("\nÁrvore de busca (BFS) a partir do vértice 0:")
for v in range(len(parent_bfs)):
    if parent_bfs[v] != -1:
        print(f"Vértice {v}: Pai {parent_bfs[v]}")
    else:
        print(f"Vértice {v}: Sem pai (raiz ou inalcançável)")

# Mostrar a árvore de busca (pais de cada vértice) para DFS
print("\nÁrvore de busca (DFS) a partir do vértice 0:")
for v in range(len(parent_dfs)):
    if parent_dfs[v] != -1:
        print(f"Vértice {v}: Pai {parent_dfs[v]}")
    else:
        print(f"Vértice {v}: Sem pai (raiz ou inalcançável)")

# Função para reconstruir o caminho do vértice 0 até um vértice alvo
def reconstruir_caminho(parent, vertice_alvo):
    caminho = []
    atual = vertice_alvo
    while atual != -1:
        caminho.append(atual)
        atual = parent[atual]
    caminho.reverse()
    return caminho

# Exemplo: reconstruir o caminho do vértice 0 até o vértice 3 para BFS
vertice_alvo = 3
caminho_bfs = reconstruir_caminho(parent_bfs, vertice_alvo)
print(f"\nCaminho do vértice 0 até o vértice {vertice_alvo} (BFS): {caminho_bfs}")

# Exemplo: reconstruir o caminho do vértice 0 até o vértice 3 para DFS
caminho_dfs = reconstruir_caminho(parent_dfs, vertice_alvo)
print(f"Caminho do vértice 0 até o vértice {vertice_alvo} (DFS): {caminho_dfs}")
