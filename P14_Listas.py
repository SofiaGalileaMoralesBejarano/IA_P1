# Sofía Galilea Morales Bejarano
# Practica 9: Listas en Python

# Creamos una lista con mis calificaciones
calificaciones = [9, 8, 10, 7]  # lista de enteros

# Creamos una lista con mis datos personales
datos = ["Sofía", 21, 66, 1.71]  # nombre, edad, peso, estatura

# Accedemos a un elemento de la lista por índice
print("Mi edad es:", datos[1])  # accede al segundo elemento (edad = 21)

# Modificamos un elemento de la lista
calificaciones[3] = 9  # cambiamos la última calificación (7 -> 9)

# Recorremos la lista con un bucle for
for nota in calificaciones:  # cada elemento de la lista se guarda en nota
    print("Calificación:", nota)  # imprime cada calificación
