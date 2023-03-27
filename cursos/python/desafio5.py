# -*- coding: utf-8 -*-

# Desafio - 5

import random

numero_secreto = random.randint(1, 6)

print("Adivinhe o número entre 1 e 6:")

for tentativas in range(3):
    numero_usuario = int(input())
    if numero_usuario == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Errou! Tente novamente!")

if numero_usuario != numero_secreto:
    print("Boa sorte na próxima!")


















