from random import *


aleatorio = randint(1,5)
print (aleatorio)

aleatorio_decimal = round(uniform(1,5),1) #Decimal
print (aleatorio_decimal)

aleatorio_random = random() # Entre 0 y 1 cualquier numero
print (aleatorio_random)


colores = ['azul','rojo','verde', 'amarillo']

aleatorio_choice = choice(colores) # aleatorio en lista
print (aleatorio_choice)

numeros = list(range(5, 50 , 5))
shuffle(numeros) # Mezcla la lista aleatoriamente
print (numeros)