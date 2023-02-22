# -*- coding: utf-8 -*-

# Desafio - 8

lista_numeros = []

entrada = input("Insira uma sequência de números: ")

for numero in entrada:
    lista_numeros.append(numero)

saida = ""

for numero in lista_numeros:
    if numero == "1":
        saida += "um "
    elif numero == "2":
        saida += "dois "
    elif numero == "3":
        saida += "tres "
    elif numero == "4":
        saida += "quatro "
    elif numero == "5":
        saida += "cinco "
    elif numero == "6":
        saida += "seis "
    elif numero == "7":
        saida += "sete "
    elif numero == "8":
        saida += "oito "
    elif numero == "9":
        saida += "nove "
    elif numero == "0":
        saida += "zero "

print(saida)


















