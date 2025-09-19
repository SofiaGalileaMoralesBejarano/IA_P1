# Sofía Galilea Morales Bejarano 6°E
# Practica 5: Input(), conversiones, operadores de cadena y operaciones prohibidas

nombre = input("Escribe tu nombre: ")       # entrada de texto
edad = int(input("Escribe tu edad: "))      # conversión de string a entero
calif = float(input("Escribe tu calificación: "))  # conversión a flotante

saludo = "Hola " + nombre   # operador de concatenación
eco = nombre * 2            # operador de repetición

# print(10 / 0)  # operación prohibida: división entre cero

print(saludo, "| Eco:", eco)                # salida con operadores de cadena
print("Edad como string:", str(edad))       # conversión entero -> string
print("Calificación entera:", int(calif))   # conversión flotante -> entero
print("LAB: calificación con bono:", calif + 1)  # LAB entradas y salidas
