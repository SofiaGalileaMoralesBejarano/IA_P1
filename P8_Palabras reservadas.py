# Sofia Galilea Morales Bejarano 6°E
# Practica 8: Palabras reservadas

print("=== Portafolio Primer Parcial de Inteligencia Artificial ===")
print("Curso: PYTHON BASICO")
print("Autor: Sofia Galilea Morales Bejarano | Matrícula: 22310226 | Grupo: 6E")


# EJEMPLO INCORRECTO
# global = 10  # SyntaxError: invalid syntax

print("\n> Ejemplo correcto: usar un identificador que contenga la palabra reservada")
variable_global = 10
print("variable_global =", variable_global)

# IMPRIMIR LISTADO DE PALABRAS RESERVADAS Y SU NUMERO
import keyword

print("\n> Palabras reservadas (keyword.kwlist):")
print(keyword.kwlist)
print("Total de palabras reservadas:", len(keyword.kwlist))

# SOFT KEYWORDS
soft_keywords = [
    ("match", "3.10"),
    ("case", "3.10"),
    ("_", "3.10"),
    ("type", "3.12")
]
for kw, ver in soft_keywords:
    print(f"- {kw} (apareció en: {ver}) - ¿es keyword en este intérprete? -> {keyword.iskeyword(kw)}")

# EJEMPLOS SEGUROS PARA PRÁCTICA
print("\n> Ejemplos seguros (evitando usar palabras reservadas como identificadores):")
# En lugar de 'global = 10' o 'match = 10' (que podrían ser keywords en tu versión),
# usa nombres alternativos:
match_var = 10
case_var = 5
print("match_var =", match_var)
print("case_var =", case_var)

# Ejemplo de comprobación programática de si una palabra es keyword
palabras_a_comprobar = ["global", "match", "case", "def", "mi_variable"]
print("\n> Comprobación rápida con keyword.iskeyword():")
for p in palabras_a_comprobar:
    print(f"{p}: iskeyword -> {keyword.iskeyword(p)}")
