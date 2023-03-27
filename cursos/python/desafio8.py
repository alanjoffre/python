# -*- coding: utf-8 -*-

# Desafio - 8

num = {
    '1':'um ',
    '2':'dois ',
    '3':'tres ',
    '4':'quatro ',
    '5':'cinco ',
    '6':'seis ',
    '7':'sete ',
    '8':'oito ',
    '9':'nove ',
    '0':'zero '
}

output = ''
numero = input('Por favor, introduza um número: ')

for digito in numero:
    output = output + num.get(digito, '!') + ''

print(output)
















