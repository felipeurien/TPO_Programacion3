# Ejercicio 1 - Algoritmo Divide y Conquista

# En un plano bidimensional se tienen n puntos con coordenadas (x, y).
# El objetivo es encontrar el par de puntos que estén a la menor distancia posible entre sí.
# Solución ingenua (O(n²))
# Solución con Divide & Conquer

def distancia(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx*dx + dy*dy

#  Seria la solución ingenua con complejidad O(n²)
def distancia_minima_bruta(puntos):
    n = len(puntos)
    min_d = 10**9
    par = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            d = distancia(puntos[i], puntos[j])
            if d < min_d:
                min_d = d
                par = (puntos[i], puntos[j])

    return par, min_d

def ordenar_por_x(puntos):
    # Ordena puntos por coordenada x (y luego por y para estabilidad).
    return sorted(puntos, key=lambda p: (p[0], p[1]))

def ordenar_por_y(puntos):
    # Ordena puntos por coordenada y (y luego por x para estabilidad).
    return sorted(puntos, key=lambda p: (p[1], p[0]))

def par_mas_cercano(puntos):
    # Encuentra el par de puntos más cercano usando Divide & Conquer.
    # Complejidad: O(n log n)
    
    # Pre-ordena por X e Y una sola vez, luego pasa ambas listas recursivamente.
    if len(puntos) < 2:
        return (None, None), float('inf')
    
    # Pre-ordenar una sola vez: O(n log n)
    Px = ordenar_por_x(puntos)
    Py = ordenar_por_y(puntos)
    
    return _recursivo(Px, Py)

def _recursivo(Px, Py):
    # Función recursiva que recibe puntos ordenados por X (Px) y por Y (Py).
    # Esto evita re-ordenar en cada nivel recursivo.
    n = len(Px)
    
    # Caso base: usar fuerza bruta para n pequeño
    if n <= 3:
        return distancia_minima_bruta(Px)

    # Dividir por la mediana en X
    mid = n // 2
    Qx = Px[:mid]  # Mitad izquierda ordenada por X
    Rx = Px[mid:]  # Mitad derecha ordenada por X
    mid_x = Px[mid][0]

    # Dividir Py en Qy y Ry manteniendo el orden por Y - O(n) lineal
    Qx_set = set(Qx)  # Para verificación rápida O(1)
    Qy = []
    Ry = []
    for p in Py:
        if p in Qx_set:
            Qy.append(p)
        else:
            Ry.append(p)

    # Resolver recursivamente
    (p1, q1), d1 = _recursivo(Qx, Qy)
    (p2, q2), d2 = _recursivo(Rx, Ry)

    # Tomar el mejor de ambos lados
    if d1 < d2:
        d = d1
        mejor_par = (p1, q1)
    else:
        d = d2
        mejor_par = (p2, q2)

    # Construir franja: puntos cuya coordenada X está cerca de mid_x
    # Comparamos (x - mid_x)² < d (distancia al cuadrado)
    import math
    delta = math.sqrt(d)  # Convertir a distancia lineal para comparar con coordenada
    strip = [p for p in Py if abs(p[0] - mid_x) < delta]

    # La franja YA está ordenada por Y (viene de Py)
    # Solo necesitamos comparar cada punto con los siguientes 7
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            d3 = distancia(strip[i], strip[j])
            if d3 < d:
                d = d3
                mejor_par = (strip[i], strip[j])

    return mejor_par, d


# --- Complejidad Temporal ---
    # Divide y Conquista:
        # Peor caso: O(n log n)
        # Mejor caso: O(n log n)
        # Caso promedio: O(n log n)
    # Ingenuo:
        # Peor caso: O(n²)
        # Mejor caso: O(n²)
        # Caso promedio: O(n²)

# --- Ejemplos de Uso ---
puntos1 = [(1,3),(2,4),(7,8),(10,2)]
mejor_par, distancia_minima_cuadrada = par_mas_cercano(puntos1)

print("Par más cercano ejemplo 1:", mejor_par)
print("Distancia al cuadrado mínima:", distancia_minima_cuadrada)

puntos2 = [(0,0),(5,0),(3,4),(0,2)]
mejor_par, distancia_minima_cuadrada = par_mas_cercano(puntos2)

print("Par más cercano ejemplo 2:", mejor_par)
print("Distancia al cuadrado mínima:", distancia_minima_cuadrada)

puntos3 = [(1,1),(2,2),(3,3),(2,1)]
mejor_par, distancia_minima_cuadrada = par_mas_cercano(puntos3)

print("Par más cercano ejemplo 3:", mejor_par)
print("Distancia al cuadrado mínima:", distancia_minima_cuadrada)

puntos4 = [(0,0),(1,0),(2,0),(10,10)]
mejor_par, distancia_minima_cuadrada = par_mas_cercano(puntos4)

print("Par más cercano ejemplo 4:", mejor_par)
print("Distancia al cuadrado mínima:", distancia_minima_cuadrada)

puntos5 = [(-1,-1),(-2,-3),(4,5),(-1,0),(2,2)]
mejor_par, distancia_minima_cuadrada = par_mas_cercano(puntos5)

print("Par más cercano ejemplo 5:", mejor_par)
print("Distancia al cuadrado mínima:", distancia_minima_cuadrada)