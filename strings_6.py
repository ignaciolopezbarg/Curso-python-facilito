#strings son colecciones igual que las listas y las tuplas y son INMUTABLES. 
message = 'Hola mundo!'
print(len(message)) #11
print(type(message)) # str
print('!' in message) # True
print('w' in message) # False
new_message ='h' + message[1:]
print(new_message) # ola mundo!
new_message2 = message[-1::-1] # !odnum aloH
print(new_message2) # !odnum aloH
print(message[0:5]) # Hola
# message[2]='z'
print(message) # TypeError: 'str' object does not support item assignment, porque las cadenas son inmutables

#Metodosjoin y split
#split genera una lista a partir de un string
message2 = 'Hola, mundo!'
print (message2.split()) # ['Hola,', 'mundo!']
# se puede agregar como parametro separadores, el que elijamos
print(message2.split(',    ')) # ['Hola', ' mundo!']
#el str original queda igual, split los transforma en una lista, comillas, separadas por comas

#join funciona al reves, desde una lista genera strings
name = 'edu'
last_name = 'lopez'
age = 30
full_name = ' '.join([name, last_name, str(age)]) # age hay que convertirlo a str, join no permite mezclar ditintos tipos de variables 
print(full_name)
print(type(full_name)) # str

full_name2 = name + ' ' + last_name + ' ' + 'tiene' + ' ' + str(age) + ' años'
print(full_name2)

# Otra forma de concatenar strings es con el metodo FORMAT
# se usan llaves como espacios con las variables que tengo. Tengamos por ejemplo un string que guardo en una variable que llamamos base
name1 = 'edu'
last_name1 = 'lopez'
age1 = 55
base = 'El nombre completo es {} {} y tiene {} años'
full_name3 = base.format(name1, last_name1, age1)
print(full_name3) # El nombre completo es edu lopez y tiene 55 años

# hagamos esto mas dinamico
name2 = input(' Ingrese su nombre: ')
last_name2 = input ('Ingrese su apellido: ')
age2 = input ('Ingrese su edad: ')
active = input('Ingrese si esta activo (si/no): ')
base = 'El nombre completo es {name2} {last_name2} y tiene {age2} años y {active} trabaja'
full_name4 = base.format(
   name2 = name2,
   active = active,
   last_name2 = last_name2,
   age2 = age2)
print(full_name4)

# Esto ultimo se podria hacer con el operador +, sin tanto formato:
print('El nombre completo es ' + name2 + ' ' + last_name2 + ' y tiene ' + age2 + ' años y ' + active + ' trabaja mucho')

# Lo mas moderno es usar directamente los f-strings
print(f'El nombre completo es {name2} y su apellido es {last_name2} y su edad es de {age2} años y {active} trabaja actualemente')

#Funcion print
print('Hola', 'mundo', sep='-', end='!') # Hola-mundo!
#podemos imprimir directamente o imprimir variables, por defecto siempre deja un espacion entre ellas, peo podemos con sep agregar lo que deseemos.
# Tambien podemos usar el parametro end, que es lo que se imprime al final de la linea, por defecto es un salto de linea, pero podemos cambiarlo por lo que queramos.
user = 'Eduardo'
edad = 25
print(user, 'tiene',edad ,'años', sep= '   ', end ='???')

#Funcion in
nuevo_string = 'Welcome to the jungle'
print('u' in nuevo_string) # True
print('junglita' in nuevo_string) # False

#Funciones startswith y endswith
print(nuevo_string.startswith('w')) # False
print(nuevo_string.endswith('p')) # False
print(nuevo_string.endswith('e')) # True

#Funciones upper y lower
print(nuevo_string.upper()) # WELCOME TO THE JUNGLE
print(nuevo_string.lower()) # welcome to the jungle

#Funcion strip (recorta espacios al incio y al final)
string_sin_recotar = '   Bienvenidos al Tren   '
print(string_sin_recotar.strip()) # Bienvenidos al Tren

#Funcion count
print((nuevo_string.count('e'))) #4

#Funcion replace
print(nuevo_string.replace('welcome', 'bienvenido')) # bienvenido to the jungle Van dos parametros, que se reemplaza ,con que

#Funcion find
print(nuevo_string.find('x')) # -1 Da por resultado 1 si la encuentra o -1 no esta la letra

#Funcion index
print(nuevo_string.index('t')) # 8 Si no encuentra la letra da error

# Funcion capitalize
strincito = 'hola a todos'
print(strincito.capitalize()) # Hola a todos Convierte la primera letra en mayuscula