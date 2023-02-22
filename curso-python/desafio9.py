# -*- coding: utf-8 -*-

# Desafio - 9

def maior_numero(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

print('=' * 30)
print('Calculo - Maior número')
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))

print('O maior número é: ', maior_numero(num1, num2))
print('=' * 30)









