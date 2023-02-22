# -*- coding: utf-8 -*-

# Desafio - 12

print("Digite um algarismo em numeração romana:")

romano = input()

if romano == "I":
    print("O algarismo em numeração arabe é 1")
elif romano == "V":
    print("O algarismo em numeração arabe é 5")
elif romano == "X":
    print("O algarismo em numeração arabe é 10")
elif romano == "L":
    print("O algarismo em numeração arabe é 50")
elif romano == "C":
    print("O algarismo em numeração arabe é 100")
elif romano == "D":
    print("O algarismo em numeração arabe é 500")
elif romano == "M":
    print("O algarismo em numeração arabe é 1000")
else:
    print("Simbolo inválido")