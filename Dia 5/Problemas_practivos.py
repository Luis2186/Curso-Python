''''
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
'''

def devolver_distintos(num1,num2,num3):
    lista = [num1,num2,num3]
    lista_ordenada = sorted(lista)
    numero_mayor= lista_ordenada[2]
    numero_intermedio = lista_ordenada[1]
    numero_menor= lista_ordenada[0]
    suma_numeros = num1 + num2 + num3

    if suma_numeros > 15:
        return numero_mayor
    elif suma_numeros < 10:
        return numero_menor
    else :
        return numero_intermedio
    

print(devolver_distintos(1,5,6))

'''''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
'''

def format(palabra):
    lista= list(palabra)
    listaOrdenada= sorted(lista)
    lista_sin_repetir= []

    for letra in listaOrdenada:
        if letra not in lista_sin_repetir:
            lista_sin_repetir.append(letra)

    return lista_sin_repetir

print(format('entretenido'))

'''''
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def num_repetidos(*args):
    lista_num=[]
    contador_num_0 = 0
    for arg in args:

        if lista_num and lista_num[-1] == 0 and arg == 0:
            return True
        
        lista_num.append(arg)

    return False


print( num_repetidos(5,6,1,0,0,9,3,5) )
print( num_repetidos(6,0,5,1,0,3,0,1) )

''''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''

def contar_primos(num):
    cantidad_num_primos = 0

    for i in range(2, num + 1):  # Iteramos desde 2 hasta num
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):  # Probamos divisores hasta la raíz cuadrada de i
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            cantidad_num_primos += 1

    return cantidad_num_primos

print(contar_primos(20))