# Sofia Galilea Morales Bejarano 6°E
# Practica 11: Normas y convenciones en python

print("- Las reglas son obligatorias: si no las cumples, tendrás errores en el programa.")
print("- Las convenciones son buenas prácticas: ayudan a escribir código limpio y fácil de leer.")
print("- Python es sensible a mayúsculas/minúsculas: nombre_variable, NOMBRE_VARIABLE y Nombre_Variable son diferentes.")
print("- Los nombres de variables pueden contener letras, números y guion bajo (_), pero no pueden comenzar con un número.")
print("- No puedes usar palabras reservadas como nombres de variables.")
print("- Buenas prácticas: usar nombres descriptivos, en minúsculas y con snake_case para nombres compuestos.")
print("- No usar acentos, ñ ni caracteres especiales en nombres de variables por compatibilidad.")
print("- Se recomienda escribir nombres en inglés cuando tengas el nivel suficiente.")
print("- Usa MAYÚSCULAS solo para constantes (ej: PI = 3.14159).")

print("\n> Ejemplos de nombres válidos:")
numero1 = 10
fecha_actual = "2025-09-18"
resultado_final = 100
print("numero1 =", numero1)
print("fecha_actual =", fecha_actual)
print("resultado_final =", resultado_final)

print("\n> Ejemplos de nombres inválidos (NO EJECUTAR, provocan error):")
print("1numero  #No puede comenzar con número")
print("$resultado  #No puede contener símbolos especiales")
print("nombre-usuario  #No puede contener guiones")

print("\n> Ejemplo de sensibilidad a mayúsculas y minúsculas:")
nombre_variable = "python"
NOMBRE_VARIABLE = "PYTHON"
Nombre_Variable = "Python"
print("nombre_variable =", nombre_variable)
print("NOMBRE_VARIABLE =", NOMBRE_VARIABLE)
print("Nombre_Variable =", Nombre_Variable)

print("\n> Ejemplo de nombres descriptivos:")
saludo = "Hola"
numero = 7
numero_preciso = 7.5657
print("saludo =", saludo)
print("numero =", numero)
print("numero_preciso =", numero_preciso)

print("\n> Ejemplo de snake_case (convención recomendada):")
nombre_completo = "Rodrigo Lagos"
hora_actual = "06:45 AM"
print("nombre_completo =", nombre_completo)
print("hora_actual =", hora_actual)

print("\n> Ejemplo de constante (por convención en mayúsculas):")
PI = 3.14159
print("PI =", PI)

print("\n> Recomendación: evita acentos y caracteres especiales en nombres de variables.")
