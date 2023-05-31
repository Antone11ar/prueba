
numero = int( input( 'Diga un número: '))

contador = 1

suma = 0

while contador <= numero:
    suma += contador
    contador += 1

print(f'La suma de los numeros del 1 al {numero} es igual a {suma}')
