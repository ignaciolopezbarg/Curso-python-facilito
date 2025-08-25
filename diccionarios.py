# Diccionarios
#Aparece el concepto de clave(llave)-valor, y las claves o llaves son INMUTABLES, pudiendo ser strings(lo mas comun), tuplas, float, int, booleanos, y hasta funciones.
users = {
    'name': 'Ignacio',
    'age': 68,
    'active' : True,
    'courses': ['HTML','CSS', 'JS'], # lista de cursos
    'settings': (123, True) # tupla de configuracion

}
print(users)
# Si quiero saber si una clave existe utilizo IN
print('name' in users) # True
print('lastname' in users) # False

#si quiero acceder a un valor de una clave
print(users['name']) # Ignacio
print(users['courses']) # ['HTML', 'CSS', 'JS']

print(type(users)) # <class 'dict'>

#Metodos de acceso en los diccionarios, para obtener claves, valores o el par llave - valor
# Son
# - keys(): devuelve una lista con las claves del diccionario
# - values(): devuelve una lista con los valores del diccionario
# - items(): devuelve una lista de tuplas con los pares (clave, valor)

print(users.keys()) # dict_keys(['name', 'age', 'active', 'courses', 'settings'])
print(list(users.keys())) # ['name', 'age', 'active', 'courses', 'settings']
print(tuple(users.keys())) # ('name', 'age', 'active', 'courses', 'settings')

print(users.values()) # dict_values(['Ignacio', 68, True, ['HTML', 'CSS', 'JS'], (123, True)])
print(list(users.values())) # ['Ignacio', 68, True, ['HTML', 'CSS', 'JS'], (123, True)]
print(tuple(users.values())) # ('Ignacio', 68, True, ['HTML', 'CSS', 'JS'], (123, True))

print(users.items()) # dict_items([('name', 'Ignacio'), ('age', 68), ('active', True), ('courses', ['HTML', 'CSS', 'JS']), ('settings', (123, True))])
print(list(users.items())) # [('name', 'Ignacio'), ('age', 68), ('active', True), ('courses', ['HTML', 'CSS', 'JS']), ('settings', (123, True))]
print(tuple(users.items())) # (('name', 'Ignacio'), ('age', 68), ('active', True), ('courses', ['HTML', 'CSS', 'JS']), ('settings', (123, True)))

# cuando uso items() me interesa obtener tanto la clave como el valor. 

# El equivalente en JS seria keys(), values() y entries()

#dict_values es una vista dinámica → refleja los cambios.
#list y tuple son copias independientes → no cambian si el diccionario cambia.

#ACTUALIZACION DE LOS DICCIONARIOS
users['name'] = 'Pepe'
users['age'] = 30
users['active'] = False
users['courses'].append('Python')
users['settings'] = (456, False)

print(users)

#Si quiero la longitud del diccionario(o sea su cantidad de claves):
print(len(users)) # 5
# si quiero eliminar un par clave-valor uso del
del(users['name'])
print(users)

"""
Mutabilidad del diccionario
El diccionario sí se puede modificar:
Podés agregar claves nuevas.
Podés cambiar el valor de una clave existente.
Podés borrar claves con del. 
"""
#Puedo agregar mas llaves de la siguiente forma:
users['lastname'] = 'Gomez'
users['email'] = 'pepe@gmail.com'
users['phone'] = '1234-5678'

print(users)

users['name'] = 'Nacho'
print(users)
print(len(users)) # 8

# Otra forma es usar el metodo UPDATE
users.update({
    'gender': 'Male',
    'adress': 'Calle 24 1979',
    'phone': '9879-9879' #modifico valor existente. Si quiero que sea int y no str, no puedo porque la clave ya fue definida como str
})
print(users)

# como seria con JS: 
"""
let users = {
    name: 'Nacho',
    age: 30,
    active: false,
    courses: ['HTML', 'CSS', 'JS'],
    settings: [123, true]
};

users.name = 'Pepe';
users.age = 30;
users.active = false;
users.courses.push('Python');
users.settings = [456, false];

console.log(users);
"""
#si quiero borrar el diccionario uso clear
users.clear()
print(users) # {}

# Si quiero volver a crear el diccionario
users = {
    'name': 'Nacho',
    'age': 30,
    'active': False,
    'courses': ['HTML', 'CSS', 'JS'],
    'settings': (123, True),
    'activity': 'None'
}

#None equivalente en JS es null, es algo que representa la ausencia de valor
print(users['activity']) # None

# Valores en python que se consideran Falsos
# - None
# - False
# - 0
# - Cualquier colección vacía: '', "", [], (), {}
# - 0.0 -0.0
# - objetos personalizados que implementen el método __bool__ y retornen False

# Valores en python que se consideran Verdaderos
# - True
# - Cualquier número distinto de 0: 1, 2, 3, -1, -2, -3, 0.1, 0.2, 0.3
# - Cualquier colección no vacía: 'hola', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'a', 2: 'b'}
# - Objetos ' ', " ", [], (), {}, estos tres ultimos con cuaquier valor adentro o par de valores adentro(dict)

