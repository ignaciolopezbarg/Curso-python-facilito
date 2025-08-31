"""
Bloques de codigo que pueden ser reutilizados en diferentes partes del programa
La estructura de una funcion es la siguiente:
def nombre_funcion(parametros): utilizando snake_case, con o sin parametros
    # cuerpo de la funcion con identacion
    return valor
"""
name = input('ingrese su nombre: ')
def say_goodbye(name):
    print('Adios ' + name)
def say_hello(name):
    print('Hola', name)
say_hello(name)
say_goodbye(name)

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name

def multiplicar(num_1, num_2):
    resultado = num_1 * num_2
    return resultado - 5
print(multiplicar(3, 4))

def dividir(num_1, num_2):
    if num_2 == 0:
        return 'no se puede dividir por cero'
    #  lo que esta despues del return no se ejecuta, termina la funcion
    resultado = num_1 / num_2
    return resultado
print(dividir(58,8))

# Parametros que se asignan por default:
def saludar (name, saludo = ''):
    print(saludo, name)
saludar('Pepe')
saludar('Rio', 'Buenos dias')
# saludo lo paso por default, si no pongo nada, trae el default

def precio_final(precio, impuesto, descuento=0):
    precio_final = precio + (precio * impuesto) - descuento
    return precio_final
print('Precio Final: ',  precio_final(100, 0.21, 10))

# ARGS y KARGS: si quiero funciones con n cantidad de argumentos, mucha mas flexibles, podemos usar el *args y **kwargs

# args trabaja con una cantidad variable de argumentos en una sola posicion
def sumar(*numbers):
    return sum(numbers)
print(sumar(1,2,8,77,9,25)) # paso los argumentos que deseo en la tupla numbers

#otro ejemplo
def show_info(user, email, *scores):
    print('Usuario:', user)
    print('Email:', email)
    if scores:  # primero verifico que haya valores
        average = sum(scores) / len(scores)
        print('Promedio:', average)
    else:
        print('No hay scores')

# Llamado 
show_info(
    'Jose',
    'jose@example.com',
    85, 98, 100, 57, 74
)

show_info(
    'rio',
    'rio@example.com',
    10, 10, 10
)

# **kwargs ahora puedo pasar n argumentos pero usando nombres distintos, y en vez de tener una tupla como con los *args, aca tendremos un diccionario:
def show_info(**users):
    for key, value in users.items():
        print(f'{key}: {value}')  #los dict tienen items, keys y values
show_info(
     user_name= 'raul',
     email= 'raul@example.com',
     password= '12327',
     active= True,
     courses= ['Python', 'JavaScript']
 )
# Funcion con args y kwargs:
def funcion_con_args_y_kwargs(*info, **datos):
    # por norma, aunque funciona igual, se recomienda reemplazar info con args y datos por kwargs
    print(type(info))
    print(type(datos))
    print('>>> Informacion: ')
    for value in info:
        print(value)
    print('\n')
    print('>>> Datos: ')
    for key,value in datos.items():
        print(f'{key} , {value} ')
funcion_con_args_y_kwargs(
        'Pepe', 'Lopez', 30, 'Ingeniero',
        courses = ['Python', 'JavaScript'],
        active= True,
        is_admin = False,
        email= 'pepe@example.com',
        phone= None
    )

# Recordar, con *args, llamamos los argumentos por posicion y con **kwargs por nombres , donde los primeros los recibimos como una tupla, y los recorremos usando sus metodos y los kwargs como un diccionario, y los recorremos recordando que tiene clave(llave y valor, y el conjunto de ambos son los items)

# Tamibien debemos considerar que hay funciones con parametros obligatorios, parametros por default, parametros *args, paramentros **kwargs, y el orden correcto para definirlos es:
def ejemplo_funcion(obligatorio, por_default='valor por defecto', *args, **kwargs):
    print('Parametro obligatorio:', obligatorio)
    print('Parametros *args:', args)
    print('Parametro por defecto:', por_default)
    print('Parametros **kwargs:', kwargs)

def ejemplo_completo(name, last_name, *args, active = True, is_admin = False, **kwargs):
    print('Argumentos obligatorios')
    print('Nombre: ', name),
    print('Apellido: ', last_name),
    print('\n')
    print('Argumentos *args: ')
    for value in args:
        print(value)
    print('\n')
    print('Argumentos por default: ')
    print('Activo: ', active)  
    print('Es Admin: ', False)
    print('\n')
    print('Argumentos **kwargs: ')
    for key,value in kwargs.items():
        print(f'{key} : {value}')
    
ejemplo_completo(
        'Ana',
        'Gomez',
        (25, 'Ingeniera', 'Uruguaya'),
        active= True,
        is_admin= True,
        email= 'ana@example.com',
        phone= None,
        graduate_with_honors= True
    ) 