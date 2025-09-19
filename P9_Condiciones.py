# Sofía Galilea Morales Bejarano
# Practica 6: Condiciones en Python

edad = 21
peso = 66
altura = 1.71

if edad < 18:  # condición si la edad es menor a 18
    print("Eres menor de edad")
elif edad >= 18 and edad < 25:  # condición para rango de edad
    print("Eres joven adulta")
else:
    print("Eres adulta")

if peso < 60:  # condición con peso
    print("Peso bajo")
else:
    print("Peso adecuado o más")

if altura > 1.70:  # condición con altura
    print("Eres alta")
