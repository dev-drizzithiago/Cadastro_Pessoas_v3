from tkinter import *
from tkinter import messagebox


class Caixa_mercadinho:
    def __init__(self):
        self.janela_principal = Tk()
        self.frame_1 = Frame(self.janela_principal, height=100, width=100)
        self.frame_1.pack(side='left')
        self.frame_2 = Frame(self.janela_principal, height=100, width=100)
        self.frame_2.pack(side='left')

        self.radio_valor = IntVar()
        self.radio_valor.set(0)

        self.label_1 = Label(self.frame_1, text='Selecione uma opção!')
        self.label_1.pack()

        self.botao_RD_entrar = Radiobutton(self.frame_1, text='Entrar', variable=self.radio_valor, value=1)
        self.botao_RD_entrar.pack()

        self.botao_RD_sair = Radiobutton(self.frame_1, text='Sair', variable=self.radio_valor, value=2)
        self.botao_RD_sair.pack()

        self.botao_RD_enter = Button(self.frame_1, text='OK', command=self.radio_entrar)
        self.botao_RD_enter.pack(side='left')
        self.botao_DR_sair = Button(self.frame_1, text='Sair', command=self.janela_principal.quit)






        mainloop()

    def radio_entrar(self):
        entrar_caixa = str(self.radio_valor.get())
        messagebox.showinfo(f'Aviso!', f'Você escolheu a opção: "{entrar_caixa}"')


exec_caixa = Caixa_mercadinho()
