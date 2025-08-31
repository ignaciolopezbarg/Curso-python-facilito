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
print(dividir(58,0))