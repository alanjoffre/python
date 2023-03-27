# -*- coding: utf-8 -*-

# Desafio - 10-1

try:
  preco = int(input('Introduzir o preço do produto: '))
except ValueError:
  print('O preço não é válido!')

try:
  desconto = int(input('A percentagem de desconto: '))
except ValueError:
  print('A percentagem não é válida!')

try:
  valor_pagar = preco - preco * (desconto/100)
  print('Valor a pagar: ', valor_pagar)
except NameError:
  print('O programa não consegue calcular o desconto por falta de informação')
