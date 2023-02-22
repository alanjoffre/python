# -*- coding: utf-8 -*-

# Desafio - 15

#início do programa
#introduzir os dados
print("Introduza 5 números separados por espaço: ")
a, b, c, d, e = map(int, input().split())

#calcular a média
media = (a+b+c+d+e)/5

#calcular a amplitude
amplitude = max(a,b,c,d,e) - min(a,b,c,d,e)

#mostrar a média e a amplitude
print("Média:", media)
print("Amplitude:", amplitude)
#fim do programa

