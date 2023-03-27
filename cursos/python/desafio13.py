# -*- coding: utf-8 -*-

# Desafio - 13

print("Pergunta 1: Qual é a capital do Brasil?\n")
print("A) Rio de Janeiro\nB) São Paulo\nC) Brasília\nD) Belo Horizonte\n")
resposta = input("Digite a letra da resposta:  ")

if resposta == "C":
    print("Resposta correta!\n")
    soma = 1
else:
    print("Resposta incorreta!\n")
    soma = 0

print("Pergunta 2: Quem é o atual presidente do Brasil?\n")
print("A) Jair Bolsonaro\nB) Fernando Collor\nC) Luiz Inácio Lula da Silva\nD) Dilma Rousseff\n")
resposta2 = input("Digite a letra da resposta:  ")

if resposta2 == "A":
    print("Resposta correta!\n")
    soma = soma + 1
else:
    print("Resposta incorreta!\n")

print("Pergunta 3: Qual é o maior país do mundo?\n")
print("A) Estados Unidos\nB) França\nC) Rússia\nD) China\n")
resposta3 = input("Digite a letra da resposta:  ")

if resposta3 == "D":
    print("Resposta correta!\n")
    soma = soma + 1
else:
    print("Resposta incorreta!\n")

print("Pergunta 4: Qual é a moeda do Canadá?\n")
print("A) Euro\nB) Dólar Canadense\nC) Libra Esterlina\nD) Peso Argentino\n")
resposta4 = input("Digite a letra da resposta:  ")

if resposta4 == "B":
    print("Resposta correta!\n")
    soma = soma + 1
else:
    print("Resposta incorreta!\n")

print("Pergunta 5: Qual é a capital de Portugal?\n")
print("A) Lisboa\nB) Porto\nC) Faro\nD) Coimbra\n")
resposta5 = input("Digite a letra da resposta:  ")

if resposta5 == "A":
    print("Resposta correta!\n")
    soma = soma + 1
else:
    print("Resposta incorreta!\n")

print("Você acertou", soma, "respostas!")