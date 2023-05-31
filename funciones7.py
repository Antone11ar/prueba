'''7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número.'''



numero=int(input('Diga un numero: '))
def imprimir_pares(numero):
    for numero in range(1,numero+1):
        if numero % 2 == 0:
            print(numero)
imprimir_pares(numero)