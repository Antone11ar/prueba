#Se te pide crear un programa que le pida al usuario que ingresar un texto
#cualquiera, por ejemplo, un artículo o una frase.

texto = input("Texto cualquiera: ")

#Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
#elección.
letras =[]
letras.append(input ("Ingrese letra 1: ".lower()))
letras.append(input ("Ingrese letra 2: ".lower()))
letras.append(input ("Ingrese letra 3: ".lower()))
print(letras)
# SE PIDE:
#1- Cantidad de veces que aparece EN EL TEXTO cada una de letras que eligió.
cantidad_letras1 = texto.count(letras[0]) #dentro de [] va el indice del elemento o lugar que ocupa en la lista.
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

#2- Cuantas palabras hay en total en todo el texto.
palabras = texto.split()
print(f"Se econtraron {len(palabras)} palabras en el texto")

#3- Cual es la primera letra y cuál es la última. (Indexación)
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La letra inicial es '{primera_letra}' y la letra final  '{ultima_letra}'")

#4- Mostrar el texto en orden inverso
palabras.reverse()
print(palabras)

#5- Decir si la palabra "python" aparece en el texto.
python_en_texto = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[python_en_texto]} se encuentra en el texto")