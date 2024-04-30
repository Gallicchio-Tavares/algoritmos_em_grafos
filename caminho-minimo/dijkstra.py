import heapq

infinito = float("inf")

def faz_grafo():
    # grafo do vídeo: https://youtu.be/_lHSawdgXpI
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }

def dijkstras_heap(G, inicio='A'):
    caminhos_mais_curtos = {} 
    visitado = set()
    heap = []

    for node in G.keys():
        caminhos_mais_curtos[node] = infinito

    caminhos_mais_curtos[inicio] = 0 
    visitado.add(inicio)

    heapq.heappush(heap, (0, inicio))

    while heap:
        distancia, node = heapq.heappop(heap)
        visitado.add(node)

        for custo, para_node in G[node]:
            if (para_node not in visitado) and (distancia + custo < caminhos_mais_curtos[para_node]):
                caminhos_mais_curtos[para_node] = distancia + custo
                heapq.heappush(heap, (caminhos_mais_curtos[para_node], para_node))

    return caminhos_mais_curtos

def dijkstras(G, inicio='A'):
    caminhos_mais_curtos = {}
    nao_visitado = dict.fromkeys(G.keys())

    for node in nao_visitado:
        caminhos_mais_curtos[node] = infinito

    caminhos_mais_curtos[inicio] = 0

    while nao_visitado:
        min_node = None

        for node in nao_visitado:
            if min_node is None or caminhos_mais_curtos[node] < caminhos_mais_curtos[min_node]:
                min_node = node

        for custo, para_node in G[min_node]:
            if custo + caminhos_mais_curtos[min_node] < caminhos_mais_curtos[para_node]:
                caminhos_mais_curtos[para_node] = custo + caminhos_mais_curtos[min_node]

        del nao_visitado[min_node]

    return caminhos_mais_curtos

def diametro_grafo(G):
    diametro = 0

    for inicio_node in G.keys():
        caminhos_mais_curtos = dijkstras(G, inicio_node)
        # Filtra os valores infinitos antes de calcular o máximo
        distancias_validas = [distancia for distancia in caminhos_mais_curtos.values() if distancia != infinito]
        if distancias_validas:
            max_distancia = max(distancias_validas)
            diametro = max(diametro, max_distancia)

    return diametro


def main():
    G = faz_grafo()
    inicio = 'A'

    caminhos_mais_curtos = dijkstras(G, inicio)
    caminhos_mais_curtos_heap = dijkstras_heap(G, inicio)
    
    diametro = diametro_grafo(G)

    #print(f'Caminho mais curto de {inicio}: {caminhos_mais_curtos}')
    print(f'Caminho mais curto de {inicio} usando heap: {caminhos_mais_curtos_heap}')
    print(f'Diâmetro do grafo: {diametro}')

main()
