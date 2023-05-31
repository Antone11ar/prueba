'''
3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10.
'''


numero = int( input( 'Diga un número: '))
i=0
for i in range(1,11):
    print(i * numero)