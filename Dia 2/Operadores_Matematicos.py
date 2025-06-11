x=6
y=2
z=7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"El modulo/residuo de {z} dividido {y} es igual a {z%y}")
print(f"{x} elevado a {y} es igual a {x**y}")
print(f"La raiz cuadrada de {x} es igual a {x**(1/2)}")
print(f"El valor absoluto de {y} es igual a {abs(y)}")

print(f"El valor absoluto de {x} es igual a {abs(x)}")  
print(f"El valor absoluto de {z} es igual a {abs(z)}")

print(f"El valor absoluto de -{y} es igual a {abs(-y)}")
print(f"El valor absoluto de -{x} es igual a {abs(-x)}")
print(f"El valor absoluto de -{z} es igual a {abs(-z)}")
print(f"El valor absoluto de 0 es igual a {abs(0)}")
print(f"El valor absoluto de -0 es igual a {abs(-0)}")



cantidadDeDigitosDecimales= 2
redondeo = round(12.256865256, cantidadDeDigitosDecimales)
print(redondeo)