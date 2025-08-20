#con esto comento en una sola linea
"""
con esto comento multilinea


"""
#variables
# <variable> = <valor> python tiene tipado dinamico, no se define el tipo de variable
name = 'Juan' # puede ir con comillas simples o dobles.
age = 5
print(name)
print(type(name))
print(age)
print(type(age))
PI = 3.1416
print(PI)
print(type(PI))

# en python no exist en las constantes, pero se puede simular escribiendo el nombre en mayusculas, pero ojo que pueden mutar
PI = 2.5
print(PI)

# los numeros grandes se pueden escribir con guiones bajos
numero_grande = 1_000_000
print(numero_grande)

num_inicial = 10
resultado = num_inicial + 5
print(resultado)
print(type(resultado))

#operadores logicos and or not (en JS serian && || !)
 # ingreso por teclado
first_name = input('Ingres su nombre :')
print('Hola', first_name)

#input captura lo que se ingresa por teclado y lo almacena en la variable de tipo str
# si necesito que se cambie agrego el tipo de variable, ej agrego int, o float u operadores relacionales

first_name = input('ingrese su nombre: ') #str
age = int(input('ingrese su edad: ')) #int
height= float(input('ingrese su altura: '))#float
estado_civil = input('ingrese su estado: c/s)') == 'c'#boolean

print (first_name, age, height, estado_civil)
print(type(first_name), type(age), type(height), type(estado_civil))
# en JS seria
# console.log(first_name, age, height, estado_civil)
# y el ingreso es con prompt y tambien entrega string, para pasar a numeros se usaba parseInt() o parseFloat()