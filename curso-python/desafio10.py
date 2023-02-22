# -*- coding: utf-8 -*-

# Desafio - 10

print('=' * 50)

try:
  def calcularDesconto(preco, desconto):
    preco_final = preco - (preco * (desconto / 100))
    return preco_final


  preco = float(input('Introduzir o preço do produto:'))
  desconto = float(input('Introduzir a porcentagem de desconto:'))

  preco_final = calcularDesconto(preco, desconto)

  print('Preço do produto: R$ {:.2f}'.format(preco))
  print('Desconto: {}%'.format(desconto))
  print('Preço com desconto: R$ {:.2f}'.format(preco_final))

except ValueError:
    print('O preço não é um valor válido!')

print('FIM')
print('=' * 50)