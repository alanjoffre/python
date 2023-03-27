# -*- coding: utf-8 -*-

# Desafio - 17

print("Quantas horas trabalhou na segunda-feira:")
segunda = int(input())
print("Quantas horas trabalhou na terça-feira:")
terca = int(input())
print("Quantas horas trabalhou na quarta-feira:")
quarta = int(input())
print("Quantas horas trabalhou na quinta-feira:")
quinta = int(input())
print("Quantas horas trabalhou na sexta-feira:")
sexta = int(input())
print("Quantas horas trabalhou no sábado:")
sabado = int(input())
print("Quantas horas trabalhou no domingo:")
domingo = int(input())

horas_trabalhadas = [segunda, terca, quarta, quinta, sexta, sabado, domingo]
maior_horas = max(horas_trabalhadas)

if maior_horas == segunda:
    print("Você trabalhou mais horas na segunda-feira.")
elif maior_horas == terca:
    print("Você trabalhou mais horas na terça-feira.")
elif maior_horas == quarta:
    print("Você trabalhou mais horas na quarta-feira.")
elif maior_horas == quinta:
    print("Você trabalhou mais horas na quinta-feira.")
elif maior_horas == sexta:
    print("Você trabalhou mais horas na sexta-feira.")
elif maior_horas == sabado:
    print("Você trabalhou mais horas no sábado.")
elif maior_horas == domingo:
    print("Você trabalhou mais horas no domingo.")


