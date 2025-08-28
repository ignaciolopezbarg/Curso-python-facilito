# El esquema del condicional es el siguiente:
# if<valor booleano>:
#     print('se cumple la condicion')
# Dejar 4 espacios de identacion, y ese es el bloque del condicional

if True:
    print('imprimi sin miedo')
print('sigo pero fuera del condicional')

# si repito pero con false la condicion no se cumple
if False:
    print('no se imprime nada')
    print('tampoco esto')
print('sigo pero fuera del condicional, solo imprime esto')

number_1 = 5
number_2 = 10
if number_1 == 5 and number_2 == 10 and number_1 > number_2:
    print('vemos que pasa')
    print('esto no se imprime')
print('sigo pero fuera del condicional')

#valores que python considera nulos: 0, 0.0, "", '', None, (), [], {}, False
value = 'codigo'
if(value):
    print(f' >>> el valor es: {value}') # >>> el valor es: codigo
    print('el valor es ' + value)

value_1 = ' '
if value_1:
    print(f' >>> el valor es distinto a  vacio')
else:
    print('el valor es  vacio') # condicion cuando no se cumple

number_1 = 100
number_2 = 1000
print(type(number_1))
print(type(number_2))
if number_1 < number_2:
    print('el numero 1 es menor que el numero 2')
elif number_1 == number_2:
    print('el numero 1 es igual que el numero 2')
else:
    print('el numero 1 es mayor que el numero 2')

color = 'verdes'
if color == 'rojo':
    print('parada obligatoria')
elif color == 'amarillo':
    print('precaucion')
elif color == 'verde':
    print('puede avanzar')
elif color != 'rojo' or color != 'amarillo' or color != 'verde':
    print('color no reconocido') 

#Match, el similar en JS es switch
# color = input('ingrese un color:')
# match color:
#     case 'rojo':
#         print('parada obligatoria')
#         # en JS agregamos aca el break, y pasamos al otro case
#     case 'amarillo':
#         print('precaucion')
#     case 'verde':
#         print('puede avanzar')
#     case _:                   # cualquier otra cosa, es como el default en JS
#         print('color no reconocido')

#Ciclo for-each
#Iteramos sobre un str o list o tuples o diccionarios, acccediendo a cada elemento
#Estructura for <variable> in <coleccion>:
     #..codigo..
colors = ['rojo', 'verde', 'amarillo']
for color in colors:
    print('el color es: ' + color)  

numbers = [1,2,5,20,30]
for number in numbers:
    print(f'El numero es: {number}') 
# en JS tendrimaos forEach:
# numbers.forEach(function(number){
# console.log(`El numero es : ${number}`)
# }) 

mensaje = 'Hola mundo'
for letra in mensaje:
    print(f'las letras son: {letra}')
# en JS seria:
# mensaje.forEach(function(letra){
# console.log('Las letras son :' + letra)})

#Iteracion sobre un diccionario:
user = {
    'name': 'pepe',
    'age': 45,
    'password': 'pass123'

}
for key in user:
    # print(f'key: {key}')
    print(f'valor: {user[key]}')
    print(user.items())
    print(list(user.items()))
    print(tuple(user.items()))

for item in user.items():
    print(f'item: {item}')

for value in user.values():
    print(f'value: {value}')

# Funcion range
for i in range(5):
    print(f'Iteracion: {i}')
# en JS seria:
# for(let i = 0; i < 5; i++){
#     console.log(`Iteracion: ${i}`);
# }

for number in range(2,9):
    print(f'el numero es : {number}')

#Ciclo While
i = 0
while i < 5:
    print(f'Iteracion: {i}')
    i += 1

counter = 0
while counter < 8:
    print('El valor es counter :', counter)
    counter += 2
# otra forma es seguir usando el ciclo for-each:
for number in range(0,8):
    print('el valor es valor:', number)

counter = 0
number = int(input('ingrese un numero: ')) # quiero saber cuantos digitos tiene el numero:
while number > 0:
    number = number //10# division entera
    counter += 1
print('el numero tiene:',counter, 'digitos')

#si no quiero usar la division entera (//) y usar la division real (/) tengo que agregar el int
# number = int(number/10) y se fuerza a entero

#Ejercicio de adivinar el mumero, generamos un numero aleatorio con randint, y le pedimos al usuario que ingrese un mumero de dos digitos
from random import randint
number_aleatorio = randint(0,20)
print(number_aleatorio)
contador = 0
number = None
while number != number_aleatorio:
    number = int(input('Adivine el numero de dos digitos del 0 al 20 :'))
    if number <0 or number > 20:
        print(' 🚥El numero ingresado no es valido')
        continue #salta a la siguiente iteracion sin comparar 
    else:
        contador += 1
    if number < number_aleatorio:
        print(' <<< el numero ingresado es menor')
    elif number > number_aleatorio:
        print(' >>> el numero ingresado es mayor')
    else:
        print(f' 😀Felicidades, adivinaste el numero {number_aleatorio} en {contador} intentos')  

# en JS seria:
"""
const numeroAleatorio = Math.floor(Math.random() * 21); // número entre 0 y 20
let numero = null;
let contador = 0;

while (numero !== numeroAleatorio) {
  numero = parseInt(prompt("🎲 Adivine el número del 0 al 20:"));

  if (isNaN(numero) || numero < 0 || numero > 20) {
    console.log("❌ El número ingresado no es válido, pruebe otra vez");
    continue; // salta a la siguiente vuelta sin contar
  }

  contador++;

  if (numero < numeroAleatorio) {
    console.log("El número ingresado es menor");
  } else if (numero > numeroAleatorio) {
    console.log("El número ingresado es mayor");
  } else {
    console.log(`🎉 Felicidades, adivinaste el número ${numeroAleatorio} en ${contador} intentos`);
  }
}

"""
# CONTINUE Y BREAK
#CONTINUE : el ciclo, ya sea for-each o while, salta a la siguiente iteracion y no ejecuta el resto del codigo. En el ejemplo anterior cuando el numero estaba fuera de rango, no seguia el codigo, sino que saltaba a la siguiente iteraciion
#BREAK : el ciclo se detiene por completo y sale.


for number in range(1,21):
    if number ==12:
        continue
    if(number % 2 != 0):
        continue # salta a la siguiente iteracion
    if number == 16:
        break # sale del ciclo
    print(f' ⭐ El numero par es: {number}')

#solo se imprimiran los numeros pares y se saltara el 12. Ademas se corta el ciclo en 16 (ojo que si le pongo un valor impar, nunca lo lee, porque el continue anterior salta a la siguiente iteracion y avanzan solo los pares)
