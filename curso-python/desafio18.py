# -*- coding: utf-8 -*-

# Desafio - 18

numero = int(input("Introduza um número entre 1 e 8: "))

while numero < 1 or numero > 8:
    numero = int(input("Introduza um número entre 1 e 8: "))

for i in range(numero):
    for j in range(numero-i-1):
        print(end=" ")
    for k in range(2*i+1):
        print(end="*")
    print()