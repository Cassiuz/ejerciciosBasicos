# Ejercicio 2
# implementacion de algoritmo de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(burbuja([64, 34, 25, 12, 22, 11, 90]))




