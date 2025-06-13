textoIngresado = input("Ingrese un texto: ")
letrasIngresadas = input("Ingrese 3 letras: ")
letrasIngresadasLista = list(letrasIngresadas)
listaTextoIngresado= textoIngresado.split(" ")

# Cuantas veces aparce cada letra que eligio
primeraLetra= letrasIngresadasLista[0]
segundaLetra = letrasIngresadasLista[1]
terceraLetra= letrasIngresadasLista[2]
cantidadPrimeraLetra = textoIngresado.lower().count(primeraLetra.lower())
cantidadSegundaLetra = textoIngresado.lower().count(segundaLetra.lower())
cantidadTerceraLetra = textoIngresado.lower().count(terceraLetra.lower())
# cuantas palabras hay en total
palabrasTotal = len(listaTextoIngresado)
# Primer letra y ultima letra del texto
primeraLetra = textoIngresado[0]
ultimaLetra = textoIngresado[-1]
# Palabras en orden inverso
ordenInverso = listaTextoIngresado.reverse()
# Aparece python dentro del texto
AparecePython = "python" in textoIngresado.lower()

print("El texto ingresado es:", textoIngresado)
print("La cantidad de veces que aparece la primera letra es:", cantidadPrimeraLetra)
print("La cantidad de veces que aparece la segunda letra es:", cantidadSegundaLetra)
print("La cantidad de veces que aparece la tercera letra es:", cantidadTerceraLetra)
print("Palabras totales:", palabrasTotal)
print(f"La primera palabra del texto es: {primeraLetra}, la utlima palabra del texto es: {ultimaLetra}")
print(f"Las palabras en orden inverso son: {listaTextoIngresado}")
print(f"¿Aparece la palabra 'python' en el texto? {'SI' if AparecePython else 'NO'}")

