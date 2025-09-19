# Sofía Galilea Morales Bejarano
# Practica 10: Listas dentro de listas (arreglos multidimensionales)

# Creamos una lista de listas con calificaciones por materia
calificaciones = [
    [9, 8, 10],   # Matemáticas: tres parciales
    [7, 9, 8],    # Física: tres parciales
    [10, 10, 9]   # Programación: tres parciales
]

# Accedemos a un valor específico (segundo parcial de física)
print("Segundo parcial de Física:", calificaciones[1][1])  # índice [fila][columna]

# Recorremos la lista de listas con dos bucles anidados
for materia in calificaciones:        # recorre cada lista (cada materia)
    for nota in materia:              # recorre cada calificación dentro de la materia
        print("Calificación:", nota)  # imprime cada nota
