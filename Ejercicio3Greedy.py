# Ejercicio 3 - Algoritmo Greedy

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

# --- EJEMPLO DE USO ---
conferencias = [(1, 3), (2, 5), (4, 6), (7, 8)]
resultado = seleccionarConferencias(conferencias)
print("Conferencias seleccionadas:", resultado)

# --- COMPLEJIDAD TEMPORAL ---
# Mejor caso: O(n log n).
# Peor caso: O(n log n).
# Caso promedio: O(n log n).