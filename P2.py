import heapq
import sys

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
    energiaTotal =0
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

    elementos_copia = elementos.copy()

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
                    caminoMinimo.remove(caminoMinimo[0])

                    energiaTotal += energia

                    #revisamos si estan en la misma posicion en sus listas
                    if elemento.index(atomo) == elementico.index(atomo):
                        nuevaLista = []
                        if elementico.index(atomo) == 1:
                            nuevaLista.append(atomo)
                            nuevaLista.append(elementico[0])
                        else:
                            nuevaLista.append(elementico[1])
                            nuevaLista.append(atomo)

                        if elemento[0] == nuevaLista[1]:
                            resultado = (nuevaLista,caminoMinimo,elemento)
                        else:
                            resultado = (elemento,caminoMinimo,nuevaLista)
                        resultados.append(resultado)
        if encontrado == False:
            return "NO SE PUEDE"
    respuesta_arreglada = arreglarLista(resultados, elementos_copia)
        
    return respuesta_arreglada, energiaTotal 
    #return atomoosLibres, graph

def arreglarLista(caminos, elementos):
    salida = []
    for camino in caminos:
        inicio, intermedios, final = camino
        salida.append(inicio)
        salida.append(intermedios)
        salida.append(final)
    for lista in salida:
        copia = salida.copy()
        copia.remove(lista)
        if lista in copia:
            salida.remove(lista)
        
    tuplas_salida = list(tuple(x) for x in salida)
    tuplas_elementos = []
    for elemento in elementos:
        tuplas_elementos.append(tuple(elemento))
        reverse_elemento = elemento.copy()[::-1]
        tuplas_elementos.append(tuple(reverse_elemento))
    
    final = []
    
    for i in tuplas_salida:
        if i in tuplas_elementos:
            final.append(str(i))
        else:
            for j in i:
                final.append(str(j))
        
    return ", ".join(final)

def main_tiempo(name_file):
    import time
    with open(name_file, "r") as file:
        linea = file.readline().strip()
        ncasos = int(linea)
        linea = file.readline().strip()
        for _ in range(0,ncasos):
            n, w1, w2 = map(int, linea.split())
            compuestos = []
            for _ in range(n):
                a, b = map(int, file.readline().strip().split())
                compuestos.append([a, b])
            inicio = time.time()
            respuesta = p2(compuestos,w1, w2)
            fin = time.time()
            if isinstance(respuesta,tuple):
                print(str(respuesta[0]) + " " + str(respuesta[1]))
            else:
                print(str(respuesta))
            print("Tiempo de ejecución:", (fin-inicio)*1000)
            linea = file.readline().strip()


def main():
    linea = sys.stdin.readline().strip()
    ncasos = int(linea)
    linea = sys.stdin.readline().strip()
    for _ in range(0,ncasos):
        n, w1, w2 = map(int, linea.split())
        compuestos = []
        for _ in range(n):
            a, b = map(int, sys.stdin.readline().strip().split())
            compuestos.append([a, b])
        respuesta = p2(compuestos,w1, w2)
        if isinstance(respuesta,tuple):
            print(str(respuesta[0]) + " " + str(respuesta[1]))
        else:
            print(str(respuesta))
        linea = sys.stdin.readline().strip()


main_tiempo("1000.in")
# Ejemplo de uso
#atomos, graph = p2([[1,3],[-6,3],[1,7]], 3, 5)
#print("Graph:", graph)
#start_node = 1
#end_node = -1
#min_distance, path = dijkstra(graph, start_node, end_node)
#print("Distancia mínima:", min_distance)
#print("Camino:", path)
#print(p2([[1,2],[-2,3],[3,-4]],2,3)) # Debe imprimir "NO SE PUEDE"
#esultado, energia = p2([[1,3],[-6,3],[1,7]],3,5)
#print(elementos)
#print(resultado, energia) # Debe imprimir un peso de 8
#print(arreglarLista(resultado, elementos),energia)

