'''15-Escribe un programa que pida al usuario una cadena de texto y determine
cuántas veces aparece cada letra en la cadena.
'''
texto= input('Por favor diga algo: ')
frecuencias = {
}

for letra in texto:
    if letra in frecuencias :
        frecuencias [letra] += 1

    else:
        frecuencias [letra] = 1

    print(frecuencias)

for letra, frecuencia in frecuencias.items():
    print(f'La letra {letra} aparece {frecuencia} veces')




