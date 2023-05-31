'''14-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
'''
numero= int(input('Por favor diga un numero: '))
for i in range(1 , numero+1):
     print(f'{i} ' * i)


