# Ejercicio 3 - Algoritmo Greedy

# Enunciado: Un ladrón tiene una mochila con capacidad de peso W. Hay N objetos, cada uno con un peso Wᵢ  y un valor V.
# El objetivo es seleccionar el subconjunto de objetos que maximice el valor total sin superar la capacidad de la mochila.

def knapsack_01(valor, peso, capacidad):
    n = len(valor)
    dp = [0] * (capacidad + 1)
    for i in range(n):
        wi, vi = peso[i], valor[i]
        for c in range(capacidad, wi - 1, -1):
            dp[c] = max(dp[c], vi + dp[c - wi])
    return dp[capacidad]

# --- Complejidad Temporal ---
# Peor caso: O(n * W)
# Mejor caso: O(n * W)
# Caso promedio: O(n * W)

# --- EJEMPLOS DE USO ---
valor = [10, 14, 16]
peso = [2, 3, 4]
capacidad = 7
print("Valor maximo obtenido en Ejemplo 1:" , knapsack_01(valor, peso, capacidad))

valor = [20, 5, 10, 40, 15, 25]
peso = [1, 2, 3, 8, 7, 4]
capacidad = 10
print("Valor maximo obtenido en Ejemplo 2:" , knapsack_01(valor, peso, capacidad))

valor = [5, 8, 14, 6, 12]
peso = [3, 5, 6, 2, 4]
capacidad = 10
print("Valor maximo obtenido en Ejemplo 3:" , knapsack_01(valor, peso, capacidad))
