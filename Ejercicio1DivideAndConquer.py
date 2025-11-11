def distancia(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx*dx + dy*dy

#  O(n^2) 
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
    n = len(puntos)
    for i in range(1, n):
        j = i
        while j > 0 and puntos[j-1][0] > puntos[j][0]:
            puntos[j-1], puntos[j] = puntos[j], puntos[j-1]
            j -= 1
    return puntos

def ordenar_por_y(puntos):
    n = len(puntos)
    for i in range(1, n):
        j = i
        while j > 0 and puntos[j-1][1] > puntos[j][1]:
            puntos[j-1], puntos[j] = puntos[j], puntos[j-1]
            j -= 1
    return puntos

def par_mas_cercano(puntos):
    puntos = ordenar_por_x(puntos)
    return _recursivo(puntos)

def _recursivo(puntos):
    n = len(puntos)
    if n <= 3:
        return distancia_minima_bruta(puntos)

    mid = n // 2
    mitad_izq = puntos[:mid]
    mitad_der = puntos[mid:]

    (p1, q1), d1 = _recursivo(mitad_izq)
    (p2, q2), d2 = _recursivo(mitad_der)

    if d1 < d2:
        d = d1
        mejor_par = (p1, q1)
    else:
        d = d2
        mejor_par = (p2, q2)

    x_med = puntos[mid][0]
    strip = []
    for p in puntos:
        if abs(p[0] - x_med) < d:
            strip.append(p)

    strip = ordenar_por_y(strip)

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d3 = distancia(strip[i], strip[j])
            if d3 < d:
                d = d3
                mejor_par = (strip[i], strip[j])

    return mejor_par, d




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