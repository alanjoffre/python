# -*- coding: utf-8 -*-

# Desafio - 14

numero = int(input("Introduza um número entre 1 e 100: "))
if numero < 1 or numero > 100:
    print("Erro: número fora do intervalo.")
else:
    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        print("O número introduzido é primo.")
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print("O número introduzido não é primo.")
    else:
        print("O número introduzido é primo.")

