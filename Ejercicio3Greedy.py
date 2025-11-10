# Ejercicio 3 - Algoritmo Greedy

# Enunciado: Un estudiante tiene n actividades, cada una con un horario de inicio y fin.
# El objetivo es seleccionar la máxima cantidad de actividades que no se superpongan.

def seleccionar_conferencias(conferencias):
    # Ordenar conferencias por hora de fin
    conferencias.sort(key=lambda c: c[1])
    conferencias_seleccionadas = []
    hora_fin_ultima = 0

    for conf in conferencias:
        if conf[0] >= hora_fin_ultima:
            conferencias_seleccionadas.append(conf)
            hora_fin_ultima = conf[1]

    return conferencias_seleccionadas

# --- EJEMPLO DE USO ---
conferencias = [(1, 3), (2, 5), (4, 6), (7, 8)]
resultado = seleccionar_conferencias(conferencias)
print("Conferencias seleccionadas:", resultado)

# --- COMPLEJIDAD TEMPORAL ---
# Mejor caso: O(n log n).
# Peor caso: O(n log n).
# Caso promedio: O(n log n).