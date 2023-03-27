# -*- coding: utf-8 -*-

from tkinter import *

# Criando uma variavel para identificar a janela
root = Tk()
class calculadora_idade():
    def __init__(self):
        self.root = root
        self.janela()
        self.desenho()
        # criando o Loop
        root.mainloop()
    def janela(self):
        self.root.title("Calculadora da idade")
        self.root.configure(background= '#B0C4DE')
        self.root.geometry("400x150")
        self.root.resizable(True, True)
    def desenho(self):
        self.datanascimento = IntVar()
        self.lb_datanascimento = Label(text='Ano de Nascimento',
                                       font=('Verdana', '8', 'bold'),
                                       bg='#D3D3D3', fg='#000000')
        self.lb_datanascimento.place(relx=0.2, rely=0.05, relwidth=0.35,
                                     relheight=0.1)
        self.input_datanascimento = Entry(textvariable=self.datanascimento)
        self.input_datanascimento.place(relx=0.6, rely=0.05, relwidth=0.2,
                                        relheight=0.1)

        self.anocalcular = IntVar()
        self.lb_anocalcular = Label(text='Ano a Calcular ',
                                       font=('Verdana', '8', 'bold'),
                                    bg='#D3D3D3', fg='#000000')
        self.lb_anocalcular.place(relx=0.2, rely=0.2,
                                  relwidth=0.35, relheight=0.1)
        self.input_anocalcular = Entry(textvariable=self.anocalcular)
        self.input_anocalcular.place(relx=0.6, rely=0.2,
                                     relwidth=0.2, relheight=0.1)

        self.bt_calcular = Button( text='Calcular',
                                bg='#808080', fg='#F8F8FF',
                                   font=("verdana", 10, "bold"),
                                   command = self.butaoclick1)
        self.bt_calcular.place(relx=0.35, rely=0.5, relwidth=0.3,
                               relheight=0.14)


        # Resultado
        self.idadeactual = StringVar()
        self.idadeactual1 = Label(textvariable=self.idadeactual)

        self.resultado1 = Label(textvariable=self.idadeactual)
        self.resultado1.place(relx=0.1, rely=0.7, relwidth=0.8)

    def butaoclick1(self):
        data_nascimento = self.datanascimento.get()
        anocalcularf = self.anocalcular.get()
        idade = anocalcularf - data_nascimento
        if idade == 0:
            final = 'Nasceu no mesmo ano a calcular!'
        elif idade >= 0:
            final = 'A idade em '+ str(anocalcularf) +\
                    ' dos nascidos em '+ str(data_nascimento) +\
                    ' será de '+ str(idade) + ' anos.'
        else:
            final ='O Ano de Nascimento é superior ao Ano a Calcular!'
        return self.idadeactual.set(final)

calculadora_idade()










