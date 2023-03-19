from tkinter import messagebox
import mysql
from mysql.connector import errorcode


def banco_dados(usuario, password):
    try:
        conexao_banco = mysql.connector.connect(host='db4free.net', user=usuario,
                                                password=password, database='drizzithiago_sql')
        messagebox.showinfo('AVISO!', 'Banco de dados conectado!')
        return conexao_banco
    except mysql.connector.Error as falha:
        messagebox.showerror('AVISO!', 'Ocorreu um erro!! ==> {}'.format(falha))



