import heapq

def calculate_LTP(m1:int, m2:int, w1:int, w2:int):
    if ((m1 > 0 and m2 > 0) or (m1 < 0 and m2 < 0)):
        return 1 + (abs(abs(m1)-abs(m2))%w1)
    else:
        return w2 - (abs(abs(m1)-abs(m2))%w2)

def dijkstra(graph, start, end):
    # Diccionarios para guardar las distancias y los caminos
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    # Usar heap para almacenar todos los nodos y sus distancias actuales
    nodes = [(0, start)]

    while nodes:
        current_distance, current_node = heapq.heappop(nodes)

        # Si llegamos al nodo final, reconstruir el camino
        if current_node == end:
            path = []
            while previous_nodes[current_node]:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(current_node)
            return distances[end], path[::-1]

        # Visitamos los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Solo considerar este nuevo camino si es mejor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(nodes, (distance, neighbor))

    return float("inf"), []

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

    return atomoosLibres, graph

# Ejemplo de uso
atomos, graph = p2([[1,3],[-6,3],[1,7]], 3, 5)
print("Graph:", graph)
start_node = 1
end_node = -1
min_distance, path = dijkstra(graph, start_node, end_node)
print("Distancia mínima:", min_distance)
print("Camino:", path)
