def calculate_LTP(m1:int, m2:int, w1:int, w2:int):
    if (m1 > 0 and m2 > 0) or (w1 < 0 and w2 < 0):
        return 1 + abs(abs(m1)-abs(m2))%w1
    else:
        return w2 - abs(abs(m1)-abs(m2))%w2

def dijkstra(graph, start):
    # Inicializar las distancias de todos los nodos como infinito
    distances = {node: float('inf') for node in graph}
    # La distancia del nodo de inicio a sí mismo es 0
    distances[start] = 0
    # Mantener un conjunto de nodos visitados
    visited = set()

    while visited != set(graph):
        # Encontrar el nodo con la distancia mínima no visitado
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # Marcar el nodo actual como visitado
        visited.add(min_node)

        # Actualizar las distancias de los nodos adyacentes
        for vecino, weight in graph[min_node].items():
            if distances[min_node] + weight < distances[vecino]:
                distances[vecino] = distances[min_node] + weight

    return distances

def p2 (elementos: list,w1,w2):
    atomoosLibres = []
    for elemento in elementos:
        for atomoo in elemento:
            if atomoo not in atomoosLibres:
                atomoosLibres.append(atomoo)
            if (atomoo*-1) not in atomoosLibres:
                atomoosLibres.append(atomoo*-1)

    graph = {}
    for atomo in atomoosLibres:
        graph[atomo] = {}
        for vecino in atomoosLibres:
            if atomo != vecino and atomo*-1 != vecino:
                graph[atomo][vecino] = calculate_LTP(atomo,vecino, w1,w2)

    
    return atomoosLibres, graph, dijkstra(graph, 1)
    
print(p2([[-3,1],[1,-5]], 2, 3 ))
