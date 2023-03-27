# -*- coding: utf-8 -*-

# Strings Formatadas

nome = 'Joana'
apelido = 'Santos'
idade = 17
# idade = '17' não seria do tipo int e sim str
# A Joana (Santos) tem 17 anos.
frase1 = 'A ' + nome + ' (' + apelido + ') ' + 'tem ' + str(idade) + ' anos.' # converter int idade em str idade
frase2 = f'A {nome} ({apelido}) tem {idade} anos' #string formatada f
print(frase1)
print(frase2)


