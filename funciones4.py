'''4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.'''

numero=int(input('Diga un numero: '))

def es_capicua(numero):
    if str(numero) == str(numero)[::-1]:
        print(True)
    else:
        print(False)


es_capicua(numero)