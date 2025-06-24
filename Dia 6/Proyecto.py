from pathlib import Path, PureWindowsPath

ruta = Path("B:\Cursos-Programacion\Curso Python\Dia 6\Recetas")

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


def obtener_sub_directorio(ruta):
    sub_directorios = [item.name for item in ruta.iterdir() if item.is_dir()]
    return list(enumerate(sub_directorios)) 


def obtener_menu_sub_directorio(sub_directorios):
    return "\n".join([f"{categoriaNro}: {categoria}" for categoriaNro, categoria in sub_directorios])


def obtener_ruta_sub_directorio_elegido(sub_directorios):
    opciones= obtener_menu_sub_directorio(sub_directorios)
    categoria =int(input(f"Por favor elija una categoría:\n{opciones}\n> "))
    categoria_elegida= sub_directorios[categoria][1]
    ruta_directorio_elegido =  [item for item in ruta.iterdir() if item.is_dir() and item.name == categoria_elegida ]
    return str(ruta_directorio_elegido[0].resolve())

# def obtener_ruta_archivo_elegido(archivos):
#     opciones= obtener_menu_sub_directorio(archivos)
#     categoria =int(input(f"Por favor elija una categoría:\n{opciones}\n> "))
#     categoria_elegida= sub_directorios[categoria][1]
#     ruta_directorio_elegido =  [item for item in ruta.iterdir() if item.is_dir() and item.name == categoria_elegida ]
#     return str(ruta_directorio_elegido[0].resolve())

def obtener_archivos_directorio(ruta):
    p = Path(ruta)  # ← Convertir string a Path
    archivos = [item.stem for item in p.iterdir() if item.is_file() and item.suffix == ".txt"]
    return list(enumerate(archivos))

def leer_receta():
    letra =''
    sub_directorio= obtener_sub_directorio(ruta)
    ruta_categoria_elegida = obtener_ruta_sub_directorio_elegido(sub_directorio)
    archivos= obtener_archivos_directorio(ruta_categoria_elegida)
    opciones_archivo = obtener_menu_sub_directorio(archivos)
    print(opciones_archivo)
    while letra != "a":
        letra = input("Para salir precione la letra a")    
    
    return

def crear_receta():
    return

def crear_categoria():
    return

def eliminar_receta():
    return

def eliminar_categoria():
    return



iniciar_programa_recetas()
