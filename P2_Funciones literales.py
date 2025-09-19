# Practica 2: Literales de Python
# Sofia Galilea Morales Bejarano 6°E
# Practica 2: Literales de Python

# --- Literales enteros ---
edad = 21  # edad de Sofia
anios_restantes_carrera = 1.5  # años restantes para terminar la carrera
edad_graduacion = edad + anios_restantes_carrera
print("Sofia tendrá", edad_graduacion, "años al graduarse.")  # combina enteros y flotantes

# --- Literales flotantes ---
altura = 1.71  # altura en metros
peso = 66.0    # peso en kilogramos
imc = peso / (altura ** 2)  # cálculo del IMC usando flotantes
print("El IMC de Sofia es:", imc)

# --- Literales de cadena (strings) ---
nombre = "Sofia Galilea Morales Bejarano"
mensaje_bienvenida = f"Hola {nombre}, ¡bienvenida a tu práctica de Python!"
print(mensaje_bienvenida)

# --- Literales booleanos ---
mayor_edad = edad >= 18  # True si Soofia es mayor de edad
print("¿Sofia es mayor de edad?", mayor_edad)

# --- Ejemplo combinado ---
print(f"Nombre: {nombre}\nEdad: {edad}\nAltura: {altura}m\nPeso: {peso}kg\nMayor de edad: {mayor_edad}")
# Combina enteros, flotantes, strings y booleanos en un solo print con saltos de línea
