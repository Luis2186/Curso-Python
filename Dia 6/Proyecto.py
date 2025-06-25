from pathlib import Path, PureWindowsPath

#ruta = Path("B:\Cursos-Programacion\Curso Python\Dia 6\Recetas")
ruta = Path("D:\Cursos Programacion\Curso-Python\Dia 6\Recetas")
abecedario='abcedefghijklmnopqrstuvwxyz'

print("Bienvenido al recetario")

def seleccionarOpcionMenu():
    opcion_es_valida = False

    while not opcion_es_valida:
        opcion_seleccionada=input(" Por favor seleccione una opcion: \n\n" \
                                    "[1] - Leer receta \n" \
                                    "[2] - Crear receta \n" \
                                    "[3] - Crear categoria \n" \
                                    "[4] - Eliminar receta \n" \
                                    "[5] - Eliminar categoria \n"\
                                    "[6] - Finalizar Programa \n"\
                                    )
        opcion_seleccionada_int = int(opcion_seleccionada)

        if opcion_seleccionada_int >=1 and opcion_seleccionada_int <=6:
            opcion_es_valida=True
        else:
            print("Por favor seleccione una opcion valida, se encuentran numeradas en el menu")

    return opcion_seleccionada


def iniciar_programa_recetas():
    opcion_seleccionada= 0

    print(opcion_seleccionada)
    while opcion_seleccionada != 6:
        opcion_seleccionada = int(seleccionarOpcionMenu())

        if opcion_seleccionada == 1:
            leer_receta()
        elif opcion_seleccionada == 2:
            crear_receta()
        elif opcion_seleccionada == 3:
            crear_categoria()
        elif opcion_seleccionada == 4:
            eliminar_receta()
        elif opcion_seleccionada == 5:
            eliminar_categoria()
        elif opcion_seleccionada == 6:
            print("¡Gracias por usar el programa de recetas!")
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 6.")


# def obtener_sub_directorio(ruta):
#     sub_directorios = [item.name for item in ruta.iterdir() if item.is_dir()]
#     return list(enumerate(sub_directorios)) 

def obtener_directorio(ruta):
    sub_directorios_rutas = [str(item.resolve()) for item in ruta.iterdir() if item.is_dir()]
    sub_directorios_nombres = [item.name for item in ruta.iterdir() if item.is_dir()]

    return list(enumerate(sub_directorios_nombres)), sub_directorios_rutas

def obtener_menu_sub_directorio(sub_directorios):

    opciones ="\n".join([f"{categoriaNro}: {categoria}" for categoriaNro, categoria in sub_directorios])
    return opciones

def obtener_posicion_opcion_elegida(directorio):
    opciones = obtener_menu_sub_directorio(directorio)
    cantidad_opciones = len(directorio)
    
    while True:
        try:
            opcion_elegida = int(input(f"Por favor elija una opción:\n{opciones}\n> "))
            if 0 <= opcion_elegida < cantidad_opciones:
                return opcion_elegida
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def salir_de_menu(letra):
    while letra not in abecedario:
        letra = input("Para salir precione cualquier letra")    
    

def obtener_ruta_directorio_elegido(sub_directorios_nombres,sub_directorios_rutas):  
    opcion_posicion =obtener_posicion_opcion_elegida(sub_directorios_nombres)
    opcion_elegida= sub_directorios_rutas[opcion_posicion]
    return opcion_elegida


def leer_receta_elegido(ruta_archivo):
    archivo = open(ruta_archivo)
    print(archivo.read())

def crear_receta_archivo(ruta_categoria_elegida,nombre_receta,contenido_receta):
    ruta_receta_nueva = Path(ruta_categoria_elegida,nombre_receta)
    archivo = open(ruta_receta_nueva ,'w')
    archivo.write(contenido_receta)
    archivo.close()

def eliminar_receta_elegida(ruta_archivo):
    ruta_archivo = Path(ruta_archivo)
    ruta_archivo.unlink()

def eliminar_categoria_elegida(ruta_categoria):
    ruta_categoria = Path(ruta_categoria)
    ruta_categoria.rmdir()

def crear_categoria_nueva(ruta,nombre_categoria):
    ruta_categoria_nueva = Path(ruta,nombre_categoria)
    ruta_categoria_nueva.mkdir(parents=True, exist_ok=True)


def obtener_archivos_directorio(ruta):
    p = Path(ruta)  # ← Convertir string a Path
    archivos_directorio = [str(item.resolve()) for item in p.iterdir() if item.is_file() and item.suffix == ".txt"]

    archivos = [item.stem for item in p.iterdir() if item.is_file() and item.suffix == ".txt"]
    return list(enumerate(archivos)),archivos_directorio

def leer_receta():
    letra ='1'
    sub_directorio_nombres, sub_directorio_rutas= obtener_directorio(ruta)
    ruta_categoria_elegida = obtener_ruta_directorio_elegido(sub_directorio_nombres,sub_directorio_rutas)

    archivos_nombres,archivos_directorio= obtener_archivos_directorio(ruta_categoria_elegida)
    ruta_archivo = obtener_ruta_directorio_elegido( archivos_nombres,archivos_directorio)
    leer_receta_elegido(ruta_archivo)

    salir_de_menu(letra)
    return

def crear_receta():
    
    letra ='1'
    sub_directorio_nombres, sub_directorio_rutas= obtener_directorio(ruta)
    ruta_directorio_elegido = obtener_ruta_directorio_elegido(sub_directorio_nombres,sub_directorio_rutas)
    nombre_receta=input("Ingrese el nombre de la receta: ") + ".txt"
    contenido_receta=input("Ingrese la receta: ")
    crear_receta_archivo(ruta_directorio_elegido,nombre_receta,contenido_receta)
    salir_de_menu(letra)
    return

def crear_categoria():
    letra ='1'
    categoria_nueva= input("Ingrese el nombre de la nueva categoria: ")
    crear_categoria_nueva(ruta,categoria_nueva)
    return

def eliminar_receta():
    letra ='1'
    sub_directorio_nombres, sub_directorio_rutas= obtener_directorio(ruta)
    ruta_categoria_elegida = obtener_ruta_directorio_elegido(sub_directorio_nombres,sub_directorio_rutas)

    archivos_nombres,archivos_directorio= obtener_archivos_directorio(ruta_categoria_elegida)
    ruta_archivo = obtener_ruta_directorio_elegido( archivos_nombres,archivos_directorio)
    eliminar_receta_elegida(ruta_archivo)
    salir_de_menu(letra)
    return

def eliminar_categoria():
    letra ='1'
    sub_directorio_nombres, sub_directorio_rutas= obtener_directorio(ruta)
    ruta_categoria_elegida = obtener_ruta_directorio_elegido(sub_directorio_nombres,sub_directorio_rutas)
    eliminar_categoria_elegida(ruta_categoria_elegida)
    salir_de_menu(letra)
    return



iniciar_programa_recetas()
