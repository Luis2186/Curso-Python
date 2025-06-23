cliente= { 'nombre': 'Federico',
          'edad': 45,
          'ocupacion':'instructor'}

pelicula = {'titulo':'Matrix',
            'ficha_tecnica': {
                'protagonista':'Keanu Reeves',
                'director':'Lana y Lilly Wachowski'
            }}


elementos =[cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion': ocupacion}:
                print('Es cliente')
                print(nombre,edad,ocupacion)
        case {'titulo':titulo,
              'ficha_tecnica': {
                'protagonista':protagonista,
                'director':director
              }}:
                    print(titulo,protagonista,director)
        case _: 
                  print("No se que es esto")