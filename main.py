from graph_lib import Graph


grafo = Graph.from_file('input.txt', representation='list')

parent, level = grafo.bfs(0) # busca em largura a partir do vértice 0

componentes = grafo.find_connected_components() # componentes conexos

grafo.to_file('output.txt')
grafo.draw_graph('images/grafo_visualizacao.png')
#print(parent)
#print(componentes)