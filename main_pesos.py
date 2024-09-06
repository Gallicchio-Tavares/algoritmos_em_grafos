from graph_lib import GrafoPeso
#TODO - Verificar caminho mínimo
grafo_peso = GrafoPeso.from_file('input_com_pesos.txt')

# Encontra menor caminho em grafo ponderado
distancia, caminho = grafo_peso.menor_caminho(0, 4)  # Exemplo: caminho do vértice 0 ao vértice 4
print(f"Distância: {distancia}, Caminho: {caminho}")

# Gera imagem do grafo ponderado
grafo_peso.cria_img_grafo_peso('images/grafo_peso_visualizacao.png')
