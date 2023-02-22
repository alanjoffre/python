# -*- coding: utf-8 -*-

# Classes e Objetos

class Avatar:

    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia
        self.dinheiro = 100

    def mostra_status(self):
        print('=' * 20)
        print('Nome: ', self.nome)
        print('Energia: ', self.energia)
        print('Dinheiro: ', self.dinheiro)  
        print('=' * 20)  
    
    def move_direita(self):
        self.energia -= 5
        print('Move direita...')
    
    def move_esquerda(self):
        self.energia -= 5
        print('Move esquerda...')
    
    def alimenta(self):
        '''alimenta a personagem aumentando a sua energia'''
        self.energia += 5
        self.dinheiro -=10
        print('Alimentando...')
    
        