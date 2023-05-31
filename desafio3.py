import random

nombre:input('Bienvenido al juego!, por favor ingrese su nombre: ')
print('El número a adivinar está entre 1 y 100, y tenes 8 intentos para adivinarlo')

intentos=8
intento=1
while intento <= 8:
    numero= int(input('Ingrese un nùmero: '))
    numero_aleatorio = random.randint(1, 100)
        
    if numero == numero_aleatorio:
        print(f'ganaste')
        break 
     
    elif numero > numero_aleatorio:
        print('El número a adivinar es menor. ')
        intento+=1
        intentos-=1
        print(f'Te quedan {intentos} intentos.')     

    elif numero < numero_aleatorio:
        print(f'El numero a adivinar es mayor')
    intento+=1
    intentos-=1
    print(f'Te quedan {intentos} intentos.')
else:
    print(f'Te quedan {intentos} intentos.')   

    
    


    
        
    
