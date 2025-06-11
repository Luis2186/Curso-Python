comision= 13

nombre= input("¿Cuál es tu nombre? ")
ventaMEs = float(input("¿Cuánto vendiste este mes? "))

comision = ventaMEs * 0.13
comisionRedondeada = round(comision, 2)

print(f"Ok {nombre}, tu comisión por ventas es de $ {comision}")