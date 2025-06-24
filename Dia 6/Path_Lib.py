from pathlib import Path, PureWindowsPath


carpeta= Path("C:/Users/lilp_/Downloads/prueba.txt")

ruta_windows= PureWindowsPath(carpeta)

if not carpeta.exists():
    print("Este archivo no existe")
else: 
    
    print(carpeta.read_text())
    print(carpeta.name) #nombre del archivo
    print(carpeta.suffix) #sufijo ".txt"
    print(carpeta.stem) #nombre sin extension

    print("Este archivo existe")


base= Path.home()
guia = Path(base,"Europa","España",Path('Barcelona', "Sagrada_Familia"))
guia2= guia.with_name("La_Pedrera.txt")

en_europa= guia.relative_to(Path("Europa"))
en_espania= guia.relative_to(Path("España"))

print(guia)
print(guia2)

