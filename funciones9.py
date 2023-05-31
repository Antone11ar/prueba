'''9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números.'''

lista_num=[]
contador=0
suma=0
def promedio(lista_num):
    while (contador < len(lista_num)):
        suma += lista_num[contador]
        contador +=1

    promedio= suma / contador
    print(promedio)

promedio(lista_num)