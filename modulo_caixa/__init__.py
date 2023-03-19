from tkinter import *
from tkinter import messagebox
from modulo_banco_dados import *
import mysql
from mysql.connector import errorcode


def CaixaMercadinhoPinheiro():
    class Caixa_mercadinho:
        user_DB = None
        pass_DB = None
        try:
            conexao_banco = mysql.connector.connect(host='db4free.net', user=user_DB,
                                                    password=pass_DB, database='drizzithiago_sql')
            messagebox.showinfo('AVISO!', 'Banco de dados conectado!')
            cursor_DB = conexao_banco.cursor()
        except mysql.connector.Error as falha:
            messagebox.showerror('AVISO!', 'Ocorreu um erro!! ==> {}'.format(falha))

        def __init__(self):

            self.conexao_banco = None
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
            self.user_DB = str(self.entrada_user.get())
            self.pass_DB = str(self.entrada_pass.get())
            self.janela_login_DB.destroy()

            comando_view_produtos = "SELECT * FROM produtos_mercadinho "
            self.cursor_DB.execute(comando_view_produtos)

            self.janela_view_DB = Tk()
            self.visualizacao_DB = Text(self.janela_view_DB)
            self.visualizacao_DB.insert(INSERT, f'{self.cursor_DB} \n ')
            self.visualizacao_DB.insert(END, 'bye!')
            self.visualizacao_DB.pack()

    iniciando = Caixa_mercadinho()
