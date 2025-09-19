# Práctica: Variables 
# Sofia Galilea Morales Bejarano 6°E

frase1 = "Compa, que le parece esa morra"  # Literal de cadena con frase de canción
frase2 = "La que anda bailando sola me gusta pa mí"  # Otra frase

# Combinamos las frases
mensaje_completo = frase1 + ", " + frase2  # Concatenamos las dos frases usando +

# Número de palabras en la frase2
palabras = len(frase2.split())  # len y split para contar palabras

# Imprimimos todo
print("Mi mensaje:", mensaje_completo)  # Imprime el mensaje completo
print("Número de palabras en la segunda frase:", palabras)  # Imprime la cantidad de palabras
