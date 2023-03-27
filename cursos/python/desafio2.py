# -*- coding: utf-8 -*-

# Desafio 2
# Pedir o ano de nsacimento do utilizado e calcular a sua idade.

#ano = input('Digite o ano de nascimento: ')
#idade = 2021 - int(ano)
#print(f'Você nasceu em {ano} e possui {idade} anos.')

from datetime import date
current_date = date.today()
data_nascimento = int(input("Digite o ano de nascimento: "))
data_actual = current_date.year
idade = data_actual-data_nascimento
print(f'Você nasceu em {data_nascimento} e possui {idade} anos.')















