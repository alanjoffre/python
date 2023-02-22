# -*- coding: utf-8 -*-

# Dicionários

aluno = {
    'nome':'joana',
    'idade': 17,
    'inscrito': True    
}

aluno['ano'] = 10

print(aluno)
print(aluno['idade'])

print(aluno.get('nome'))
print(aluno.get('ano',9))#Caso não encontre, retorne 9