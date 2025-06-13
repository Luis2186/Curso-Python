mi_texto = "esta es una prueba"
# (texto, indexInicio, indexFin) 
resultado = mi_texto.index("e",0, 10)
print(mi_texto)

import re
prueba = "Ci: 43211322 Empresa: Neveland Rut: 123456789455"
partes = re.split(r"\s+(?=\w+\s*:)", prueba)
print(partes)
