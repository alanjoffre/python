# -*- coding: utf-8 -*-

# Listas Bidimensionais

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# Forma correta 1
for l in range(3):
    for c in range(3):
        print(matriz[l] [c])
print('='*5)

# Forma correta 2
for linha in matriz:
    for num in linha:
        print(num)
print('='*5)

# Para entendimento
print(matriz)
print('='*5)

print(matriz[0])
print('='*5)

print(matriz[1][0])
print('='*5)

print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[2][0])
print(matriz[2][1])
print(matriz[2][2])
print('='*5)












