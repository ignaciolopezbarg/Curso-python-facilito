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
# DESEMPAQUETADO DE TUPLAS
courses = ('Python', 'Java', 'JavaScript', 'HTML', 'CSS')
# a cada elemento de la tupla se lo asigno a una variable
var1 = courses[0]
var2 = courses[1]
var3 = courses[2]
var4 = courses[3]
var5 = courses[4]

var1,var2,var3,var4,var5 = courses
print(var1)  # Python
print(courses[2]) # JS
print(courses)

# si quiero modificar, y por ej obviar el var 2 y 5, reemplazo por un guion bajo:
var1, _, var3, _, var5 = courses
print(courses) # ('Python', 'Java', 'JavaScript', 'HTML', 'CSS') la  tupla queda inmutable, pero
print(var1,var3,var5)# Python JavaScript CSS
print(_)  # Java y HTML, pero no se usan

#tambien se puede agrupar de la siguiente forma: con *
var1, _, *sub_courses, last_course = courses
print(var1, *sub_courses, last_course)  # Python JS HTML CSS 

# FUNCION ZIP:
# agrupa elemento de diferentes iterables (listas, tuplas) usando la funcion zip() que toma los mismos indices para agrupar
users = ['juan', 'pedro', 'maria'] # lista de usuarios
ids = [1, 2, 3] # lista de ids
print(list(zip(users, ids))) # [('juan', 1), ('pedro', 2), ('maria', 3)]

# ahora agrupemos tres iterables:
courses = ['Python', 'Java', 'JavaScript']
notas = (10,8,5)
#usamos list y el zip

respuesta = list(zip(users, courses, notas))
print(respuesta)
print(type(respuesta))  # <class 'list'>, porque zip devuelve un objeto iterable, y al usar list() lo convertimos en una lista. Si lo queremos convertir en una tupla, podemos usar la funcion tuple()
respuesta_tupla = tuple(zip(users, courses, notas)) #<class 'tuple'>
print(respuesta_tupla)  # (('juan', 'Python', 10), ('pedro', 'Java', 8), ('maria', 'JavaScript', 5)) me devolvio una tupla, esta entre parentesis, anterior la lista estaba encerrada entre corchetes
print(type(respuesta_tupla))  # <class 'tuple'>

# zip() agrupo las distintas colecciones de iterables con indices coincidentes

respuesta_nueva_tupla = tuple(zip(users,ids, courses, notas))
respuesta_nueva_lista = list(zip(users,ids, courses, notas))

print(respuesta_nueva_tupla)  
print(respuesta_nueva_lista)

#FUNCIONES DE TUPLAS:

num = (1,2,3,3,5,5,8,15)
#len() me da la longitud de la tupla
print(len(num)) # 8

#count()
print(num.count(3)) # 2, me dice cuantas veces se repite el valor 3 en la tupla
print(num.count(5)) # 2
print(num.count(65)) # 0

#sorted()
print(sorted(num)) # [1, 2, 3, 3, 5, 5, 8, 15]
# si le doy el parametro reverse = True, lo ordena descendente
print(sorted(num, reverse=True)) # [15, 8, 5, 5, 3, 3, 2, 1]

#sum()
print(sum(num)) # 37 suma todos los numeros

print(min(num)) # 1
print(max(num)) # 15

#in
print(88 in sum) # false
print(5 in num) # true

#index me da el indice de un elemento (el primero)
print(num.index(15))# 7
print(num.index(3))# 2
print(num.index(88)) # ValueError: 88 is not in tuple