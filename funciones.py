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