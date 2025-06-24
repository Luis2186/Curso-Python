archivo= open('Prueba1.txt','w')

archivo.write('soy el nuevo texto')
archivo.writelines(['hola', 'mundo', 'aqui','estoy'])

# print(archivo.readline())



archivo.close()