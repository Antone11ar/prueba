'''5-Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario.'''

numero1=int(input('Diga un numero: '))
numero2=int(input('Diga un numero: '))

def es_divisible(numero1, numero2):
    resto= numero1 % numero2
    if resto == 0 :
        print('Es divisible')
    else:
        print('No es divisible')
es_divisible(numero1, numero2)