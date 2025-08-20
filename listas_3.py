# la forma de indicar una lista es 
# <lista> = <[elemento1, elemento2, elemento3]>
# en JS serian los arreglos o arrays
mi_lista = [1, 2, 3, 4, 5]
my_list = ['string', 25, 3.14, True, [1, 2, 3] ]

print(my_list)
print(type(my_list))

# los indices en las lista son iguales a JS, comienzan en cero y van de uno en uno

print(value := my_list[1]) # en una sola linea
# en JS seria
# let value = my_list[1];
# console.log(value);
# en python se puede usar el operador walrus, que permite asignar y retornar el valor en una sola expresion

valor = my_list[2]
print(valor)

# si quiero el ultimo valor de la lista, usamos len para obtener la loingitud o la cantidad de elementos de la lista
longitud = len(my_list)
print(longitud)

#ultimo indice:
valor_ultimo = my_list[longitud - 1]
print(valor_ultimo)

# tambien puedo usar indices negativos, -1 es el ultimo, -2 el penultimo y asi sucesivamente, leyendo de derecha a izquierda
valor_ultimo_con_negativos = my_list[-1]
print(valor_ultimo_con_negativos)

# puedo actualizar los valores en las listas, asignado nuevos valores en la posicion que quiero modificar
my_list[1] = 'nuevo valor'
my_list[4] = [7, 8, 9]
my_list[-2] = 25
print(my_list)

#SUBLISTAS, aca usamos el concepto de slicing
courses = ['Python', 'JS', 'Java', 'C++', 'HTML']
# creamos una sublista
# el slicing lo hacemos con dos puntos con un start and end 
new_courses = courses[0:2]
print(new_courses)
""" en JS seria
let new_courses = courses.slice(0, 2);
console.log(new_courses);"""

#tambien puedo hacerlo en forma manual
courses[0] = 'CSS'
courses[-1] = 'React'
new_courses_1 = [
    courses[0],
    courses[-1] 
]
print(new_courses_1)

new_courses_2 = [ courses[0], courses[1]]
print(new_courses_2)

#si quiero una sublista con los ultimos tres elementos
new_num = [1,2,3,4,5]
new_num_2 = new_num[-1:-2]
print(new_num_2) #[]
# esto no funciona, el slice viene seteado de izquierda a derecha con +1, por eso me da [], para que funcione debo agregar un tercer parametro cambiando el paso, o sea -1

new_num_2 = new_num[-1:-3:-1]
print(new_num_2)# [5, 4]

new_num_3 = new_num[0:1]
print(new_num_3) # 1

# tambien si omito el numero final, python supone que se tomara todo
new_num_4 = new_num[0:]
print(new_num_4) # [1, 2, 3, 4, 5] y se genero por ejemplo una copia de la lista original

# o mas facil si no le indico nada toma todo, idem si no indico el inicio, supone el 0 y le indico el final, o valores intermedios
new_num_5 = new_num [:]
print(new_num_5) # [1, 2, 3, 4, 5]

#si quiero una lista con solo los valores indices pares
new_num_6 = new_num[::2]
print(new_num_6) # [1, 3, 5]
# si quiero una lista solo con los valores impares:
new_num_7 = new_num[1::2]
print(new_num_7) # [2, 4]

#METODOS DE LAS LISTAS
# las listas en python se pueden modificar, aumentandolas o disminuyendolas en su longitud
#Metodo append() agrega al final un nuevo valor
new_num.append(6)
print(new_num) # [1, 2, 3, 4, 5, 6]

#Otro metodo es insert() que recibe dos parametros el indice donde agrego y el valor
new_num.insert(3,0)
print(new_num) # [1, 2, 3, 0, 4, 5, 6]

new_num.insert(-1,7)
print(new_num) # [1, 2, 3, 0, 4, 5, 7, 6] el insert coloca antes del indice indicado

#Metodo extend() agrego a una lista otros valores
new_num_agregar = [20, 21, 22]
new_num.extend(new_num_agregar)
print(new_num) # [1, 2, 3, 0, 4, 5, 7, 6, 20, 21, 22]

# Metodo para saber si un elemento esta en la lista, dara un valor booleano si esta o no EL metodo es "in"
print(100 in new_num)# False
print(20 in new_num) # True

#Metodo para conocer el indice de un elemento: index()
print(new_num.index(6)) # 7
# si el elemento no esta en la lista, dara un error
# print(new_num.index(1000)) # ValueError: 1000 is not in list

# Vimos dos metodos para buscar elementos en la lista: in e index. Uno da un booleano y el otro el valor, pero ver que con el index, si da error, corta todo el script, por eso lo comento para seguir

#Remocion de elementos:
# Metodo remove() y le pasamos lo que eliminamos
new_num.remove(1)
new_num.remove(2) #remove solo admite un argumento
print(new_num)

#Metodo pop() remueve el ultimo elemento
new_num.pop()
print(new_num)

first_element = new_num.pop(0) # si le paso un indice, remueve el elemento en esa posicion
print(first_element) # 3
print(new_num) # [0, 4, 5, 7, 6, 20, 21, 22]

#Si quiero puedo limpiar completamente la lista con clear() y me dara un arreglo vacio, lista vacia
new_num.clear()
print(new_num) # []

#Ordenar una lista con sort() en forma ascendente
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros) # [1, 2, 5, 5, 6, 9]

numeros.sort(reverse=True) # si le paso el reverse true lo ordena en forma descendente
print(numeros) # [9, 6, 5, 5, 2, 1]

""" Resumen de los metodos vistos hasta aca
append() Agrega un elemento al final de la lista
insert() Agrega un elemento en una posicion especifica
extend() Agrega varios elementos al final de la lista
remove() Elimina la primera ocurrencia de un elemento
pop() Elimina y devuelve un elemento en una posicion especifica (o el ultimo si no se indica)
clear() Elimina todos los elementos de la lista
sort() Ordena los elementos de la lista
"""
#Metodos copy y reverse
#Con el slicing ya podiamos copiar una lista
nueva_lista = numeros[:]
print(nueva_lista) # [1, 2, 5, 5, 6, 9]

nueva_lista2 = numeros.copy() # retorna lo mismo
print(nueva_lista2) # [1, 2, 5, 5, 6, 9]

nueva_reversa = numeros.reverse()
print(nueva_reversa) # None, porque no retorna nada, pero la lista original se invierte
print(numeros) # [9, 6, 5, 5, 2, 1] ahora la lista original se invirtio

#tambien para darla vuelta podemos usar el slicing
reversed_list = numeros[::-1]
print(reversed_list) # [1, 2, 5, 5, 6, 9] y la original no se modifica, volvimos a la original