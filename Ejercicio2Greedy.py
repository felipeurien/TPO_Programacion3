# Ejercicio 2 - Algoritmo Greedy

# Enunciado: Un estudiante tiene n actividades, cada una con un horario de inicio y fin.
# El objetivo es seleccionar la máxima cantidad de actividades que no se superpongan.

def seleccionarConferencias(conferencias):
    # Tenemos que ordenar las conferencias por hora de fin
    conferencias.sort(key=lambda c: c[1])
    conferenciasSeleccionadas = []
    hora_fin_ultima = 0

    # Iterar sobre las conferencias ordenadas
    for conf in conferencias:
        # Si la conferencia actual empieza después o cuando termina la última seleccionada. Agregarla a la lista.
        if conf[0] >= hora_fin_ultima:
            conferenciasSeleccionadas.append(conf)
            hora_fin_ultima = conf[1]

    return conferenciasSeleccionadas

# --- EJEMPLOS DE USO ---

# Ejemplo 1
conferencias = [(1, 3), (2, 5), (4, 6), (7, 8)]
resultado = seleccionarConferencias(conferencias)
print("Conferencias seleccionadas:", resultado)

# Ejemplo 2
conferencias = [(1, 2), (2, 3), (3, 4), (1, 5)]
resultado = seleccionarConferencias(conferencias)
print("Conferencias seleccionadas:", resultado)

# Ejemplo 3
conferencias = [(1, 3), (2, 3), (3, 4)]
resultado = seleccionarConferencias(conferencias)
print("Conferencias seleccionadas:", resultado)

# --- COMPLEJIDAD TEMPORAL ---
# Mejor caso: O(n).
# Peor caso: O(n log n).
# Caso promedio: O(n log n).