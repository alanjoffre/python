# -*- coding: utf-8 -*-

# Strings (métodos)

nome = 'Joana Santos'
print(len(nome)) # retorna o número de caracteres na variável

print(nome.upper())     # método upper - retorna todas as letras em maiúsculas
print(nome.lower())     # método lower - retorna todas as letras em minúsculas
print(nome.find('a'))   # método find  - retorna a posição da primeira letra a
print(nome.find('tos')) # método find  - retorna a posição das letras tos
print(nome.find('kj'))  # método find  - retorna -1 quando não encontra

# verificar se o email é válido
nome = 'joana@gmail.com'
print(nome.find('@'))  # válido por encontrar o @
nome = 'joana_gmail.com'
print(nome.find('@'))  # não é válido, pois retornou -1

nome = 'joana_gmail.com'
contem = 'joana' in nome
print(contem)

nome = 'joana_gmail.com'
contem = 'Joana' in nome
print(contem)

