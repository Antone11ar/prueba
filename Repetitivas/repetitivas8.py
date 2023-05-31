'''8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene.'''
cadena= input('Diga algo: ')
lista_palabras= cadena.split()
cantidad_palabras= len(lista_palabras)
print(cantidad_palabras)