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

    encontrado = False
    resultados = []
    #se itera por cada elemento de la lista de elementos
    for elemento in elementos:
        #se crea una copia de la lista de elementos eliminando el elemento a revisar
        elementos.remove(elemento)
        copia = elementos.copy()
        #por cada atomo del elememnto revisando
        for atomo in elemento:
            #se itera cada elemento de la copia
            for elementico in copia:
                #se revisa si el atomo del elemento que estamos revisando se encuentra en alguno otro elemento
                if atomo in elementico:
                    encontrado = True
                    #si esta entonces se llama al dijsktra para hallar el camino mas corto para conectar los elementos
                    energia,caminoMinimo = dijkstra(graph,atomo,atomo*-1)

                    #revisamos si estan en la misma posicion en sus listas
                    if elemento.index(atomo) == elementico.index(atomo):
                        nuevaLista = []
                        if elementico.index(atomo) == 1:
                            nuevaLista.append(atomo)
                            nuevaLista.append(elementico[0])
                        else:
                            nuevaLista.append(elementico[1])
                            nuevaLista.append(atomo)
                        resultado = (elemento,caminoMinimo,nuevaLista,energia)
                        resultados.append(resultado)
        if encontrado == False:
            return "NO SE PUEDE"
        
    return resultados, elementos
    #return atomoosLibres, graph

def arreglarLista(caminos, elementos):
    salida = []
    for camino in caminos:
        inicio, intermedios, final = camino
        salida.append(inicio)
        salida.append(intermedios)
        salida.append(final)
        otro = salida
        
    return salida

# Ejemplo de uso
#atomos, graph = p2([[1,3],[-6,3],[1,7]], 3, 5)
#print("Graph:", graph)
#start_node = 1
#end_node = -1
#min_distance, path = dijkstra(graph, start_node, end_node)
#print("Distancia mínima:", min_distance)
#print("Camino:", path)
#print(p2([[1,2],[-2,3],[3,-4]],2,3)) # Debe imprimir "NO SE PUEDE"
resultado, elementos = p2([[1,3],[-6,3],[1,7]],3,5)
print(resultado) # Debe imprimir un peso de 8
print(arreglarLista([([1, 3], [1, 7, -1], [7, 1]), ([1, 3], [3, -7, -3], [3, -6])], elementos))

