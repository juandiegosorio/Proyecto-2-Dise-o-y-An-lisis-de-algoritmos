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
        for neighbor, weight in graph[min_node].items():
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight

    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)