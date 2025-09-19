# Sofía Galilea Morales Bejarano
# Practica 9: Bucles en Python

# Bucle for para repetir mi nombre
for i in range(3):  # range(3) genera los números 0,1,2 -> se repite 3 veces
    print("Sofía Galilea Morales Bejarano")  # imprime mi nombre en cada repetición

# Bucle while para contar hasta mi edad
contador = 1  # inicializamos la variable contador en 1
while contador <= 21:  # se ejecuta mientras contador sea menor o igual a mi edad (21)
    if contador == 21:  # condición: si contador llega a 21
        print("Ya llegué a mi edad:", contador)  # imprime mensaje indicando que llegó a la edad
    contador += 1  # incrementamos el contador en 1 en cada vuelta
