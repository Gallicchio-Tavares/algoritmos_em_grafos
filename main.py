from graph_lib import Grafo

grafo = Grafo.from_file('txts/input.txt', representation='list')
grafo_maior = Grafo.from_file('txts/grafo_maior.txt', representation='matrix')

grafo.to_file('txts/output.txt')
grafo.cria_img_grafo('images/grafo.png')
grafo_maior.to_file('txts/output_grafo_maior.txt')
grafo_maior.cria_img_grafo('images/grafo_maior.png')

componentes = grafo.achar_conexos()
print(componentes)
if len(componentes) == 1: 
    print("O grafo é conexo")

componentes_m = grafo_maior.achar_conexos()
print(componentes_m)
if len(componentes_m) == 1: 
    print("O grafo maior é conexo")

vertice_ini = 0
vertice_alvo = 3

caminho = grafo.menor_caminho(vertice_ini, vertice_alvo)
print(f"Menor caminho do vértice {vertice_ini} ao vértice {vertice_alvo}: {caminho}")

caminho_grafo_maior = grafo_maior.menor_caminho(vertice_ini, vertice_alvo)
print(f"Menor caminho do vértice {vertice_ini} ao vértice {vertice_alvo} do grafo maior é: {caminho_grafo_maior}")
