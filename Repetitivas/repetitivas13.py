'''13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas.'''

numero_de_filas= int(input('Por favor diga un numero: '))
for i in range(numero_de_filas):
    print("*" * (i+1))
    