# Ejercicio 4 - Algoritmo de Floyd-Warshall

# Enunciado: Cada grupo deberá inventar un problema de la vida real que pueda modelarse con un grafo ponderado,
# y resolverlo utilizando el algoritmo de Floyd-Warshall para obtener las distancias más cortas entre todos los pares de nodos.

# Caso Elegido: Planificación universitaria
# Cada nodo representa un aula o laboratorio, y las aristas el tiempo de traslado entre ellos.
# El objetivo es encontrar el tiempo mínimo de traslado entre todos los pares de aulas/laboratorios.

def floydWarshall(distancias):
    # Inicializar la matriz de distancias mínimas
    num_nodos = len(distancias)
    distanciaMinima = [[float('inf')] * num_nodos for _ in range(num_nodos)]

    # Inicializar la matriz de distancias mínimas con las distancias dadas
    for i in range(num_nodos):
        for j in range(num_nodos):
            distanciaMinima[i][j] = distancias[i][j]

    # Aplicar el algoritmo de Floyd-Warshall
    # Iterar sobre cada nodo como posible nodo intermedio
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                # Actualizar la distancia mínima si se encuentra un camino más corto a través del nodo k
                if distanciaMinima[i][j] > distanciaMinima[i][k] + distanciaMinima[k][j]:
                    distanciaMinima[i][j] = distanciaMinima[i][k] + distanciaMinima[k][j]

    return distanciaMinima

# --- EJEMPLO DE USO ---
distancias = [
    [0, 10, float('inf'), 30, 100],
    [10, 0, 50, float('inf'), float('inf')],
    [float('inf'), 50, 0, 20, 10],
    [30, float('inf'), 20, 0, 60],
    [100, float('inf'), 10, 60, 0],
]

resultado = floydWarshall(distancias)
print("Matriz de distancias mínimas entre aulas/laboratorios:")
for fila in resultado:
    print(fila)

# --- COMPLEJIDAD TEMPORAL ---
# Mejor caso: O(n^3).
# Peor caso: O(n^3).
# Caso promedio: O(n^3).