from tkinter import *
from tkinter import messagebox


class Caixa_mercadinho:
    def __init__(self):
        self.janela_principal = Tk()

        self.frame_1 = Frame(self.janela_principal, height=100, width=200)
        self.frame_1.pack(side='left')
        self.frame_2 = Frame(self.janela_principal, height=100, width=200)
        self.frame_2.pack(side='left')

        self.radio_valor = IntVar()
        self.radio_valor.set(0)

        self.label_1 = Label(self.frame_1, text='Selecione uma opção!')
        self.label_1.pack(side='left')

        self.botao_RD_entrar = Radiobutton(self.frame_1, text='Entrar', variable=self.radio_valor, value=1)
        self.botao_RD_entrar.pack(anchor='w')

        self.botao_RD_sair = Radiobutton(self.frame_1, text='Sair', variable=self.radio_valor, value=2)
        self.botao_RD_sair.pack(anchor='w')

        self.botao_DR_sair = Button(self.frame_1, text='Sair', height=1, width=2, command=self.janela_principal.quit)
        self.botao_DR_sair.pack(side='right')

        self.botao_RD_enter = Button(self.frame_1, text='OK', height=2, width=4, command=self.radio_entrar)
        self.botao_RD_enter.pack(side='right')

        mainloop()

    def radio_entrar(self):
        valor_radio = self.radio_valor.get()
        if valor_radio == 1:
            self.janela_registradora = Tk()
            self.frame_1_REG = Frame(self.janela_registradora, height=100, width=200)
            self.frame_1_REG.pack(side='left')
        elif valor_radio == 2:
            messagebox.showinfo('Aviso!!', f'O valor foi {valor_radio}')


exec_caixa = Caixa_mercadinho()