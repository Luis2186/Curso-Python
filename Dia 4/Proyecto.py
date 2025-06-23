from random import *

nombre_usuario = input('Cual es tu nombre? ')
intentos= 8
num_inicio = 1
num_final = 100
lista_numeros= range(num_inicio, num_final+1)
numero_random = choice(lista_numeros)

print(f"{nombre_usuario} eh pensado un numero entre el {num_inicio} y el {num_final} y tienes solo {intentos} intentos para adivinar cual es")

while intentos > 0:
    numero_ingresado = int(input("Ingresa el numero: "))
    if numero_ingresado < num_inicio or numero_ingresado > num_final:
        print(f"El numero ingresado no esta comprendido entre el {num_inicio} y el {num_final} ")
    elif numero_ingresado < numero_random:    
        print(f"El numero ingresado es menor al numero elegido")
    elif numero_ingresado > numero_random:    
        print(f"El numero ingresado es mayor al numero elegido")
    else:
        print(f"Correcto! el numero ingresado {numero_ingresado} corresponde al elegido {numero_random}, lo lograste en {intentos} intentos! ")
        break
        
    intentos = intentos - 1

if intentos == 0:
     print(f"Ya no quedan mas intentos, vuelve a intentarlo! ")
