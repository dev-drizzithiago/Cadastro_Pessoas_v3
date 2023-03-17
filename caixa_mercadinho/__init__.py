from tkinter import *


class Caixa_mercadinho:
    def __init__(self):
        self.janela_principal = Tk()
        self.frame_1 = Frame(self.janela_principal)
        self.frame_2 = Frame(self.janela_principal)

        self.radio_valor = IntVar
        self.radio_valor.set(0)

        self.label_1 = Label(self.frame_1, text='Selecione uma opção!')
        self.botao_RD_enter = Radiobutton(self.frame_1, text='Entrar', variable=self.radio_valor, value=1)
        self.botao_RD_sair = Radiobutton(self.frame_1, text='Sair', variable=self.radio_valor, value=1)

        self.label_1.pack()
        self.botao_RD_enter.pack()
        self.botao_RD_sair.pack()

mainloop()
