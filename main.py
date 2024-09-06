from graph_lib import Grafo

grafo = Grafo.from_file('txts/input.txt', representation='list')
grafo_desconexo = Grafo.from_file('txts/input_desconexo.txt', representation='matrix')

parent, level = grafo.bfs(0)  # Busca em largura a partir do vértice 0

componentes = grafo.achar_conexos()

grafo_desconexo.visualizar_componentes_conexos('images/grafo_desconexo_componentes_visualizacao.png')

grafo.to_file('txts/output.txt')
grafo.cria_img_grafo('images/grafo_visualizacao.png')
#grafo_desconexo.to_file('output_desconexo.txt') # erro

"""
Visualizar a Busca por Largura:
"""
print("Nível dos vértices a partir do vértice 0:")
for v in range(len(level)):
    print(f"Vértice número {v+1}: Nível {level[v]}")

print("\nÁrvore de busca (Pai de cada vértice):")
for v in range(len(parent)):
    if parent[v] != -1:  # exclui o vértice inicial e vértices inalcançáveis
        print(f"Vértice número {v+1}: Pai {parent[v]}")
    else:
        print(f"Vértice número {v+1}: Sem pai (raiz ou inalcançável)")

def reconstruir_caminho(parent, vertice_alvo):
    caminho = []
    atual = vertice_alvo
    while atual != -1:  # -1 indica que chegamos à raiz ou que não há caminho
        caminho.append(atual)
        atual = parent[atual]
    caminho.reverse()
    return caminho

vertice_alvo = 2
caminho = reconstruir_caminho(parent, vertice_alvo)
print(f"\nCaminho do vértice 0 até o vértice número{vertice_alvo+1}: {caminho}")

#TODO - Verificar caminho mínimo
