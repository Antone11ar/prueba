'''7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).
'''
palabra= input('Diga una palabra: ')
cantidad_letras= len(palabra)
es_palindromo = True

for i in range(cantidad_letras):
    if palabra[i] != palabra[-i-1]:
        es_palindromo = False
    break
if es_palindromo:
    print(f'La palabra {palabra} es un palindromo')
else: 
    print(f'La palabra {palabra} no es palindromo')