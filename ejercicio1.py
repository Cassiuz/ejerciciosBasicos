# Ejercicio 1
# Función que devuelve los divisores de un número.
def divisores(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(divisores(20))







