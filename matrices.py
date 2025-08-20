# Las matrices en python son lista con sublistas anidadas, y puedo tener n dimensiones.Una matriz de 3x3 sera una matriz de dos dimensiones
matrix = [
    [1,2,3], # elemento 0 de la lista
    [4,5,6], # elemento 1 de la lista
    [7,8,9]  # elemento 2 de la lista
]
print(matrix)
# si quiero el primer fila o indice 0
print(matrix[0]) # [1,2,3]
# si quiero el primer elemento de la fila 0 o de indice 0
print(matrix[0][0]) # 1
# si quiero el ultimo elemento, las filas empiezan con 0 y las columnas igual
print(matrix[2][2]) # 9