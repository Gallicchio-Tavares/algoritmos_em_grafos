from graph_lib import GrafoPeso

grafo_desconexo = GrafoPeso.from_file('txts/grafo_peso_desconexo.txt', representation='list')
componentes = grafo_desconexo.achar_conexos()
print(componentes)
if len(componentes) > 1: 
    print("O grafo é desconexo")
    
grafo_desconexo.visualizar_componentes_conexos('images/grafo_peso_componentes.png')
