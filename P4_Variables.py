# Práctica: Variables 
# Sofia Galilea Morales Bejarano 6°E

frase1 = "Compa, que le parece esa morra"  # string almacena el texto
frase2 = "La que anda bailando sola me gusta pa mí"  # string

# Concatenamos frases
mensaje = frase1 + ", " + frase2

# Revisamos si la palabra 'bailando' está en frase2 usando 'in'
if "bailando" in frase2:
    print("Encontré la palabra 'bailando' en la frase!")  # palabra reservada print e if

# Contamos cuántas palabras tiene frase2 usando len()
numero_palabras = len(frase2.split())
print("Número de palabras en frase2:", numero_palabras)  # print como palabra reservada
