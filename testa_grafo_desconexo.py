from graph_lib import Grafo

grafo_desconexo = Grafo.from_file('txts/input_desconexo.txt', representation='matrix')
componentes = grafo_desconexo.achar_conexos()
print(componentes)
if len(componentes) > 1: 
    print("O grafo é desconexo")
    
grafo_desconexo.visualizar_componentes_conexos('images/grafo_desconexo_componentes.png')
