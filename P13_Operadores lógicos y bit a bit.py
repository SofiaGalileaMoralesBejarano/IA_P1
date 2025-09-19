# Sofía Galilea Morales Bejarano
# Practica 8: Operadores lógicos y bit a bit

edad = 21                     # literal entero que representa mi edad
peso = 66                     # literal entero que representa mi peso en kg (usado para operaciones bit a bit)
es_estudiante = True          # literal booleano que representa si soy estudiante
aprobado = False              # literal booleano que representa si aprobé el examen

mask = 0b1010                 # literal entero en binario (máscara) -> 10 decimal
otro_mask = 0b0110            # literal binario -> 6 decimal

es_mayor = edad >= 18                         # comparación: True si mi edad es mayor o igual a 18
condicion_and = es_mayor and es_estudiante    # operador lógico AND entre booleans
condicion_or = aprobado or (peso > 60)        # operador lógico OR entre booleano y comparación
negacion = not aprobado                       # operador lógico NOT que invierte el booleano aprobado

and_bits = mask & otro_mask       # operador bit a bit AND entre mask y otro_mask
or_bits = mask | otro_mask        # operador bit a bit OR entre mask y otro_mask
xor_bits = mask ^ otro_mask       # operador bit a bit XOR entre mask y otro_mask
not_peso = ~peso                  # operador bit a bit NOT (complemento a dos, suele dar número negativo)
left_shift = mask << 1            # desplazamiento a la izquierda: multiplica por 2 (en binario)
right_shift = mask >> 2           # desplazamiento a la derecha: divide por 4 (entero)

es_peso_par = (peso & 1) == 0     # uso bit a bit para comprobar si mi peso es par (LSB igual a 0)
condicion_combinada = (es_mayor and es_peso_par) or not aprobado
                                  # combinación de condiciones lógicas y comprobación de bit

print("Edad:", edad)                                  # salida: muestra mi edad
print("¿Mayor de edad?:", es_mayor)                   # salida: resultado de la comparación
print("AND lógico (mayor y estudiante):", condicion_and)  # salida: resultado AND lógico
print("OR lógico (aprobado o peso>60):", condicion_or)     # salida: resultado OR lógico
print("NOT de aprobado:", negacion)                   # salida: inversión del booleano aprobado

print("Mask:", bin(mask), "Otro:", bin(otro_mask))    # salida: representaciones binarias de las máscaras
print("AND bit:", bin(and_bits))                      # salida: resultado AND en binario
print("OR bit:", bin(or_bits))                        # salida: resultado OR en binario
print("XOR bit:", bin(xor_bits))                      # salida: resultado XOR en binario
print("NOT peso (bitwise):", not_peso)                # salida: resultado NOT de peso (entero)
print("Left shift mask <<1:", bin(left_shift))        # salida: máscara desplazada a la izquierda
print("Right shift mask >>2:", bin(right_shift))      # salida: máscara desplazada a la derecha

print("¿Mi peso es par? (check bit):", es_peso_par)   # salida: indica si mi peso es par usando bitwise
print("Condición combinada:", condicion_combinada)    # salida: resultado final de la condición combinada
