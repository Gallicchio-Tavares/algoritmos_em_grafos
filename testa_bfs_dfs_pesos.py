from graph_lib import GrafoPeso

grafo_peso = GrafoPeso.from_file('txts/input_com_pesos.txt')

parent_bfs, level_bfs = grafo_peso.bfs(0)
parent_dfs, level_dfs = grafo_peso.dfs(0)

print("Níveis dos vértices (BFS) a partir do vértice 0:")
for v in range(len(level_bfs)):
    print(f"Vértice {v}: Nível {level_bfs[v]}")

print("\nNíveis dos vértices (DFS) a partir do vértice 0:")
for v in range(len(level_dfs)):
    print(f"Vértice {v}: Nível {level_dfs[v]}")

print("\nÁrvore de busca (BFS) a partir do vértice 0:")
for v in range(len(parent_bfs)):
    if parent_bfs[v] != -1:
        print(f"Vértice {v}: Pai {parent_bfs[v]}")
    else:
        print(f"Vértice {v}: Sem pai (raiz ou inalcançável)")

print("\nÁrvore de busca (DFS) a partir do vértice 0:")
for v in range(len(parent_dfs)):
    if parent_dfs[v] != -1:
        print(f"Vértice {v}: Pai {parent_dfs[v]}")
    else:
        print(f"Vértice {v}: Sem pai (raiz ou inalcançável)")

def reconstruir_caminho(parent, vertice_alvo):
    caminho = []
    atual = vertice_alvo
    while atual != -1:
        caminho.append(atual)
        atual = parent[atual]
    caminho.reverse()
    return caminho

vertice_alvo = 3
caminho_bfs = reconstruir_caminho(parent_bfs, vertice_alvo)
print(f"\nCaminho do vértice 0 até o vértice {vertice_alvo} (BFS): {caminho_bfs}")

caminho_dfs = reconstruir_caminho(parent_dfs, vertice_alvo)
print(f"Caminho do vértice 0 até o vértice {vertice_alvo} (DFS): {caminho_dfs}")
