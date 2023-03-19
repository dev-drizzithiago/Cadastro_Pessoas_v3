from tkinter import *
from tkinter import messagebox
from modulo_banco_dados import *
import mysql
from mysql.connector import errorcode


def CaixaMercadinhoPinheiro(usuario, password):
    class Caixa_mercadinho:
        try:
            conexao_banco = mysql.connector.connect(host='db4free.net', user=usuario,
                                                    password=password, database='drizzithiago_sql')
            messagebox.showinfo('AVISO!', 'Banco de dados conectado!')
            cursor_DB = conexao_banco.cursor()
        except mysql.connector.Error as falha:
            messagebox.showerror('AVISO!', 'Ocorreu um erro!! ==> {}'.format(falha))

        def __init__(self):
            self.janela_login_DB = Tk()

            self.frame_reg_1 = Frame(self.janela_login_DB)
            self.frame_reg_1.pack(side='left')

            self.frame_reg_2 = Frame(self.janela_login_DB)
            self.frame_reg_2.pack(side='left')

            self.label_user = Label(self.frame_reg_1, text='Usuário')
            self.label_user.pack(side='top')

            self.label_pass = Label(self.frame_reg_2, text='Password')
            self.label_pass.pack(side='top')

            self.entrada_user = Entry(self.frame_reg_1, bd=15)
            self.entrada_user.pack(side='left')

            self.entrada_pass = Entry(self.frame_reg_2, bd=15)
            self.entrada_pass.pack(side='left')

            self.botao_enter = Button(self.janela_login_DB, text='Enter', height=2, width=4, command=self.login_db)
            self.botao_enter.pack(side='left')

            mainloop()

        def login_db(self):
            user_DB = str(self.entrada_user.get())
            pass_DB = str(self.entrada_pass.get())
            cursor = banco_dados(user_DB, pass_DB)
            self.janela_login_DB.destroy()

            self.janela_view_DB = Tk()
            self.visualizacao_DB = Text(self.janela_view_DB)
            self.visualizacao_DB.insert(INSERT, f'{cursor} \n ')
            self.visualizacao_DB.insert(END, 'bye!')
            self.visualizacao_DB.pack()

    iniciando = Caixa_mercadinho()
