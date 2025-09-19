# Practica: ¡Hola Mundo!
#Sofia Galilea Morales Bejarano 6°E

# --- Uso básico de print() ---
print("Hola Mundo")  # Imprime el mensaje "Hola Mundo" en la consola

# --- Usando caracteres de escape ---
print("Hola\tMundo")  # \t agrega un tabulador entre palabras
print("Hola\nMundo")  # \n agrega un salto de línea

# --- Imprimiendo múltiples argumentos posicionales ---
print("Hola", "Mundo", 2025)  
# print() puede recibir varios argumentos separados por coma
# Cada argumento se imprime separado por un espacio por defecto

# --- Usando variables con print() ---
mensaje = "¡Bienvenida a Python!"  # almacenamos un string en la variable mensaje
print(mensaje)  # imprimimos la variable

# --- Combinando texto y variables con formato ---
nombre = "Sofía"
edad = 20
print("Nombre:", nombre, "Edad:", edad)
# Cada argumento separado por coma se imprime con un espacio automáticamente

# --- Otra forma de imprimir con formato (f-strings) ---
print(f"Nombre: {nombre}\nEdad: {edad}")
# f-strings permiten insertar variables dentro de un string
# \n genera un salto de línea
