print("Hello, World!")
# ejemplo sacado de la ia
#generador de contraseñas seguras
import random
import string

print(' 🔐Generador de contraseñas seguras')
#pedir al usuario de que longitud sera la contraseña
Longitud = int(input('Ingrese la longitud de la contraseña(minimo 8 caracteres): '))
if Longitud < 8:
    print('La longitud debe ser al menos 8 caracteres. Se establecerá en 8 por defecto.')
    Longitud = 8

#otra forma seria con un ciclo while
#while Longitud < 8:
#    Longitud = 8

letras = string.ascii_letters # trae mayusculas y minusculas
print(letras)
numeros = string.digits # trae los numeros
print(numeros)
simbolos = string.punctuation # trae los simbolos
print(simbolos)

incluir_simbolos = input('Incluir simbolos? s/n: ').lower()
if incluir_simbolos == 's':
    caracteres = letras + numeros + simbolos
else:
    caracteres = letras + numeros

# elegir caracteres al azar
password = ''.join(random.choice(caracteres) for _ in range(Longitud))
print('Tu nueva contraseña segura es: 🔐', password)