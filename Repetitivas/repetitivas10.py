'''10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con todas las vocales en mayúscula.'''

texto= (input('Escriba una frase: '))
texto_mayusculas=""
for letra in texto:
    if letra in "aeiouAEIOU":
        texto_mayusculas += letra.upper()
    else: texto_mayusculas += letra

print(texto_mayusculas)