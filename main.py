from graph_lib import Grafo

grafo = Grafo.from_file('txts/input.txt', representation='list')
grafo_desconexo = Grafo.from_file('txts/input_desconexo.txt', representation='matrix')

parent, level = grafo.bfs(0)  # Busca em largura a partir do vértice 0

componentes = grafo.achar_conexos()

grafo_desconexo.visualizar_componentes_conexos('images/grafo_desconexo_componentes_visualizacao.png')

grafo.to_file('txts/output.txt')
grafo.cria_img_grafo('images/grafo.png')


vertice_ini = 0  # Exemplo: vértice inicial 0
vertice_alvo = 3  # Exemplo: vértice alvo 3

caminho = grafo.menor_caminho(vertice_ini, vertice_alvo)
print(f"Menor caminho do vértice {vertice_ini} ao vértice {vertice_alvo}: {caminho}")

