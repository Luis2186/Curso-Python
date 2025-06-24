from random  import * 

palabras = [
    "cielo", "montana", "rio", "mar", "bosque", "nube", "sol", "luna", "estrella", "viento",
    "fuego", "tierra", "roca", "flor", "animal", "pajaro", "pez", "trueno", "lluvia", "nieve",
    "noche", "dia", "amanecer", "atardecer", "camino", "sendero", "puente", "arbol", "hierba", "arena",
    "playa", "desierto", "isla", "valle", "cueva", "laguna", "ciudad", "pueblo", "hogar", "viaje"
]


def ingresarLetra ():
    return input("Ingresa una letra: ")


def devolverPalabraLista(palabra_elegida):
    palabraListaOculta=[]
    for letra in list(palabra_elegida):
        palabraListaOculta.append({
                'valorActual': "_",
                'valorOculto': letra
            })

    return palabraListaOculta


def chequearLetra(letra_usuario, palabra_lista):

    for item in palabra_lista:
        if letra_usuario == item['valorOculto']:
            item['valorActual'] = item['valorOculto']
            return True
    return False

def palabra_adivinada(palabra_lista):

    for item in palabra_lista:
        if item['valorActual'] == "_":
            return False;

    return True
    

def imprimirResultado(palabra_lista):
    palabra = ''
    for item in palabra_lista:
        palabra += item['valorActual'] + " "
    print(palabra)



def iniciar_ahorcado():
    cantidad_de_vidas = 6
    palabra_elegida = choice(palabras)
    palabra_lista= devolverPalabraLista(palabra_elegida)
 
    print(f"Bienvenidos al juego Ahorcado, el juego consiste en adivinar una palabra oculta, cuentan con {cantidad_de_vidas} intentos para adivinarla !buena suerte!")

    while cantidad_de_vidas > 0:
        letra_ingresada= ingresarLetra()
        
        if palabra_elegida.lower() ==  letra_ingresada.lower():
            print(f"!Ha ganado! La palabra oculta era {palabra_elegida}, !Gracias por jugar!")
            return

        letra_encontrada = chequearLetra(letra_ingresada,palabra_lista)
        imprimirResultado(palabra_lista)

        if palabra_adivinada(palabra_lista):
            print(f"!Ha ganado! La palabra oculta era {palabra_elegida}, !Gracias por jugar!")
            return

        if not letra_encontrada :
            cantidad_de_vidas-=1

    if cantidad_de_vidas == 0:
        print(f"Se han terminado las vidas, la palabra oculta era {palabra_elegida}, !Vuelve a intentarlo!")
        return

iniciar_ahorcado()