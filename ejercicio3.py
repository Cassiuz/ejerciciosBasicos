# Ejercicio 3
# encontrar el elemento más frecuente en un lista
from collections import Counter

def mas_frecuente(lista):
    frecuencia = Counter(lista)
    return max(frecuencia, key=frecuencia.get)

print(mas_frecuente([1, 2, 2, 3, 1, 2, 4, 2, 1]))








