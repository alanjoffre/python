# -*- coding: utf-8 -*-

# Tuplas
# São utilizadas, quando temos certeza que os dados não serão alterados.

num1 = [1,2,3] #Lista

num2 = (1,2,3) #Tupla

num1[0] = 5
#num2[0] = 5 # Vai gerar erro, object does not support item assignment

print(num1)
print(num2)