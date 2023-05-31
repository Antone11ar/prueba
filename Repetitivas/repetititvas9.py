'''9-Escribe un programa que pida al usuario un número y luego imprima la
secuencia de Fibonacci correspondiente a ese número.
'''

num = int(input('Escribe un numero: '))

a, b = 0, 1

while b <= num:
    print(b)
    a, b = b, a + b
