# -*- coding: utf-8 -*-

# Desafio - 4

pswd = input('Digite sua senha: (6-15 caracteres) ')

if len(pswd) < 6:
    print('Sua senha possui menos que 6 caracteres. Digite uma nova senha válida, entre 6 a 15 caracteres')
elif len(pswd) <= 15:
    print('Login validado com sucesso.')
else:
    print('Login inválido. Digite uma nova senha válida, entre 6 a 15 caracteres')          

















