#Las tuplas a diferencia de los listas son inmutables, es decir no pueden ser modificadas una vez creadas.
#Las listas se escriben con [] y las tuplas con () y los metodos que se usan para las listas son diferentes a los de las tuplas.
settings = ('localhost', 8080, True)
print(type(settings))  # <class 'tuple'>
print(settings[1])
print(settings[-1])
# print(settings[4]) # error indi e fuera de rango

# tambien puedo crear una tupla si el uso de los parentesis, python infiere que es una tupla
numbers = 1, 2, 3, 4, 5
print(type(numbers))  # <class 'tuple'>

#tambien podemos crear una tupla de un solo valor, pero lo que no debe faltar son las comas
valor_unico = 40,
print(type(valor_unico))  # <class 'tuple'>

#Las tuplas son INMUTABLES,  no se pueden modificar, ni su contenido, ni agregar o borrar.