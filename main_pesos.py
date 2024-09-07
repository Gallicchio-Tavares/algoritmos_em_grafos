from graph_lib import GrafoPeso

grafo_peso = GrafoPeso.from_file('txts/input_com_pesos.txt', representation="list")

distancia, caminho = grafo_peso.menor_caminho(0, 4)
print(f"Distância: {distancia}, Caminho: {caminho}")

#grafo_peso.cria_img_grafo_peso('images/grafo_peso.png')
grafo_peso.to_file('txts/output_pesos.txt')

componentes = grafo_peso.achar_conexos()
print(componentes)
if len(componentes) == 1: 
    print("O grafo é conexo")
else:
    print('O grafo é desconexo')
    