# Sofia Galilea Morales Bejarano 6°E
# Practica 12:Matemáticas

print("=== Portafolio Primer Parcial de Inteligencia Artificial ===")
print("Curso: PYTHON BASICO")
print("Autor: Sofia Galilea Morales Bejarano | Matrícula: 22310226 | Grupo: 6E")

print("1. +  -> Suma (también concatenación en otro capítulo).")
print("2. -  -> Resta.")
print("3. *  -> Multiplicación.")
print("4. /  -> División (siempre devuelve float).")
print("5. %  -> Módulo (resto de la división).")
print("6. // -> División entera (devuelve la parte entera, int).")
print("7. ** -> Potencia (exponente).")
print("8. Paréntesis para cambiar prioridad de evaluación.")
print("9. Orden de operaciones: (), **, *, /, +, -.")
print("10. Usa variables para hacer operaciones dinámicas.")
print("11. Usa guiones bajos en números largos para legibilidad (ej: 1_000_000).")

# --- CÓDIGO DE PRÁCTICA ---
# Operadores básicos
print("\n# --- Operadores básicos ---")
print(20 + 50)        # Suma -> 70
print(10 - 4)         # Resta -> 6
print(10 * 4)         # Multiplicación -> 40
print(10 / 3)         # División -> 3.3333333333333335

# Operaciones combinadas
print("\n# --- Operaciones combinadas ---")
operacion = 100 * 98 + 65 * 2 - 10 / 5
print(operacion)      # -> 9928.0

# Operando con variables
print("\n# --- Operando con variables ---")
numero1 = 100
numero2 = 500
resultado = numero1 + numero2
print(resultado)      # -> 600

# Operador módulo
print("\n# --- Operador módulo (%) ---")
a = 10
b = 3
print("Cociente (float):", a / b)
print("Resto (a % b):", a % b)

# División entera vs división normal
print("\n# --- División normal vs entera ---")
division_normal = a / b
division_entera = a // b
print("division_normal (a / b):", division_normal)   # 3.333...
print("division_entera (a // b):", division_entera)   # 3

# Calculando media de edades (float y entera)
print("\n# --- Media de edades ---")
edades = [15, 26, 54, 22, 17, 50, 33, 32]
suma_edades = sum(edades)
numero_edades = len(edades)
media_float = suma_edades / numero_edades
media_entera = suma_edades // numero_edades
print("En total hay:", numero_edades, "edades.")
print("Media (float):", media_float)
print("Media (entera):", media_entera)

# Potencia
print("\n# --- Potencia (**) ---")
print(2 ** 10)        # -> 1024
# Nota: 2 ** 5000 devuelve un número extremadamente grande; si quieres lo ejecutamos expresamente.
# print(2 ** 5000)

# Prioridad de operaciones y paréntesis
print("\n# --- Prioridad y paréntesis ---")
print(10 + 6 * 2)       # -> 22
print((10 + 6) * 2)     # -> 32
print(2 ** 10 / 2)      # -> 512.0
print(2 ** (10 / 2))    # -> 32.0

# Números largos con guiones bajos
print("\n# --- Números largos con guiones bajos ---")
numero_largo = 56_404_357_843_987
print(numero_largo)

numero_largo_decimal = 56_404_357_843_987.78
print(numero_largo_decimal)
