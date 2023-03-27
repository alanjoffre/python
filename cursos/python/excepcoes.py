# -*- coding: utf-8 -*-

# Excepções

try:
    idade = int(input('Idade: '))
    salario = 1600
    risco = salario / idade # 1600 / 0
    print('Idade:',idade, '| Salário: R$',salario,',00',' | Risco:{:.2f} '.format(risco),'%')
except ValueError:
    print('A idade introduzida não é válida!')
except ZeroDivisionError:
    print('A idade não pode ser ZERO!')
print('FIM')