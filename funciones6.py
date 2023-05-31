'''6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par.
'''
numero=int(input('Diga un numero: '))

def es_par(numero):
    if numero % 2 == 0:
        print(f'El {numero} es par.')
    else:
        print(f'El {numero} no es par.')

es_par(numero)
