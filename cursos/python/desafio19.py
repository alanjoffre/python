# -*- coding: utf-8 -*-

# Desafio - 19

# Programa para calcular a área das figuras geométricas

opção = 0

while opção != 6: 
  print("MENU")
  print("1 - Área Quadrado")
  print("2 - Area do Retângulo")
  print("3 - Área do Triângulo")
  print("4 - Area do Trapézio")
  print("5 - Área do Circulo")
  print("6 - Sair")

  opção = int(input("Digite a opção desejada: "))

  if opção == 1:
    lado = int(input("Digite o lado do quadrado: "))
    área = lado * lado
    print("A área do quadrado é de " + str(área) + " cm²")
  
  elif opção == 2:
    base = int(input("Digite a base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    área = base * altura
    print("A área do retângulo é de " + str(área) + " cm²")

  elif opção == 3:
    base = int(input("Digite a base do triângulo: "))
    altura = int(input("Digite a altura do triângulo: "))
    área = (base * altura) / 2
    print("A área do triângulo é de " + str(área) + " cm²")

  elif opção == 4:
    base_maior = int(input("Digite a base maior do trapézio: "))
    base_menor = int(input("Digite a base menor do trapézio: "))
    altura = int(input("Digite a altura do trapézio: "))
    área = ((base_maior + base_menor) * altura) / 2
    print("A área do trapézio é de " + str(área) + " cm²")
  
  elif opção == 5:
    raio = int(input("Digite o raio do círculo: "))
    área = 3.14 * (raio ** 2)
    print("A área do círculo é de " + str(área) + " cm²")

print("Programa encerrado!")