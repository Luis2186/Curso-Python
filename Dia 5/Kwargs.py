def prueba (num1,num2,*args,**kwargs):
    #print(type(kwargs))

    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(15,50,100,25,20,23,25,26, x=3,y=5,z=2) 