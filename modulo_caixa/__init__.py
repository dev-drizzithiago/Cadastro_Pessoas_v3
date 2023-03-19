from tkinter import *
from tkinter import messagebox
import mysql
from mysql.connector import errorcode


class conexao_DB:
    def __init__(self, usuario, password):
        try:
            conexao_bando = mysql.connector.connect(host='db4free.net', user=usuario,
                                                    password=password, database='drizzithiago_sql')
            messagebox.showinfo('AVISO!', 'Banco de dados conectado!')
        except mysql.connector.Error as falha:
            messagebox.showerror('AVISO!', 'Ocorreu um erro {}'.format(falha))


def CaixaMercadinhoPinheiro():
    class Caixa_mercadinho:
        def __init__(self):
            self.janela_principal = Tk()

            self.frame_1 = Frame(self.janela_principal, height=100, width=200)
            self.frame_1.pack(side='left')

            self.radio_valor = IntVar()
            self.radio_valor.set(0)

            self.label_1 = Label(self.frame_1, text='Selecione uma opção!')
            self.label_1.pack(side='left')

            self.botao_RD_entrar = Radiobutton(self.frame_1, text='Entrar', variable=self.radio_valor, value=1)
            self.botao_RD_entrar.pack(anchor='w')

            self.botao_RD_sair = Radiobutton(self.frame_1, text='Configurações', variable=self.radio_valor, value=2)
            self.botao_RD_sair.pack(anchor='w')

            self.botao_DR_sair = Button(self.frame_1, text='Sair', height=1, width=2,
                                        command=self.janela_principal.quit)
            self.botao_DR_sair.pack(side='left')

            self.botao_RD_enter = Button(self.frame_1, text='OK', height=2, width=4, command=self.radio_entrar)
            self.botao_RD_enter.pack(side='left')

            mainloop()

        def radio_entrar(self):
            valor_radio = self.radio_valor.get()
            if valor_radio == 1:
                self.janela_registradora = Tk()
                self.label_user = Label(self.janela_registradora, text='Usuário')
                self.label_user.pack(side='left')
                self.label_pass = Label(self.janela_registradora, text='Password')
                self.entrada_user = Entry(self.janela_registradora, bd=30)
                self.entrada_user.pack(side='right')
                self.botao_enter = Button(self.janela_registradora, text='Enter', command=self.login_db)

            def login_db():


            elif valor_radio == 2:
                messagebox.askquestion('Teste', 'Sim')

    exceltando_caixa = Caixa_mercadinho()
