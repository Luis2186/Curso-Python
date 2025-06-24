mi_archivo= open('prueba.txt')

mi_archivo.read()
primera_linea = mi_archivo.readline()
print(primera_linea)
segunda_linea = mi_archivo.readline()
print(segunda_linea)
tercera_linea = mi_archivo.readline()
print(tercera_linea)

todas_las_lineas = mi_archivo.readlines() #Lista con todas las lineas










mi_archivo.close()
