'''
6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso.
'''
'''
#USANDO SLICING "::"
palabra=input('Diga una palabra: ')
palabra_alreves= palabra[::-1]
print(palabra_alreves)
'''
'''pedir me expliquen con for in'''
#USANDO ESTRUCTURAS REPETITIVAS
palabra= input('Diga una palabra: ')
palabra_invertida=''
for letra in palabra:
    palabra_invertida= letra + palabra_invertida
print(palabra_invertida)