# -*- coding: utf-8 -*-

# Desafio - 16

nome = str(input("Digite o seu nome completo: "))

nome_separado = nome.split()

print("O seu primeiro nome é:", nome_separado[0])

print("As suas iniciais são:", end=" ")

for nomes in nome_separado[1:]:
  print(nomes[0], end=" ")

