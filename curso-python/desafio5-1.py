# -*- coding: utf-8 -*-

# Desafio - 5 - 1

import random

num_aleatorio = random.randint(1,6)
num_tentativas = 0

# print(num_aleatorio)

while num_tentativas < 3:
    num_tentativas += 1
    num_utilizador = int(input('Tente adivinhar o número: '))
    if num_utilizador == num_aleatorio:
        print('Parabéns acertou!')
        break
else: 
    print('Boa sorte para a próxima')






















