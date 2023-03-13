import mysql.connector
from mysql.connector import errorcode
from analise_dados import *
from datetime import datetime, date
from os import makedirs, listdir


# OBJETO PARA MELHORAR A APARENCIA DO PROGRAMA
class Aparencia:
    @staticmethod
    def logo_principal(texto):
        print('-' * 100)
        print(f'{texto}'.center(100))

    @staticmethod
    def linha():
        print('-' * 100)

    # FUNÇÃO PARA VERIFICAR SE A ENTRADA É UM NÚMERO INTEIRO
    @staticmethod
    def leiaInt(valor_int):
        while True:
            try:
                num_int = int(input(valor_int))
                return num_int
            except ValueError:
                print('Você entrou com um valor invalido, tente novamente.')

    # FUNÇÃO PARA ANALISAR SE A ENTRADA É UM NÚMERO REAL(FLOAT)
    @staticmethod
    def leiaFloat(valor_float):
        while True:
            try:
                num_float = float(input(valor_float))
                return num_float
            except ValueError:
                print('Você entrou com um valor invalido, tente novamente.')

    # FUNÇÃO PARA QUE O USUÁRIO RESPONDA "SIM" OU "NÃO" QUANDO SE UMA DUVIDA
    @staticmethod
    def continuar_SN(texto):
        print(f'{texto}')
        resp = 'Opção INVALIDA!'
        sleep(1)
        while True:
            try:
                valor_opc = str(input('Aceita prosseguir? [S/N]: '))[0].upper()
                if len(valor_opc) == 0:
                    Aparencia.linha()
                    print(resp)
                else:
                    return valor_opc
            except:
                Aparencia.linha()
                print(resp)

    # FUNÇÃO DESTINADA EM 'DAR' UMA PAUSA, ANTES DE CONTINUAR
    @staticmethod
    def apt_enter():
        return input('Aperte o ENTER para continuar')

    @staticmethod
    def guardando(diretorio, valor_lista):
        abrindo_relatorio = open(diretorio, 'a')
        abrindo_relatorio.write(f'{valor_lista} \n')


# OBJETO DE RELATORIOS
class Relatorios_Mercadinho:

    # CRIA ARQUIVO DE LOG GERAL, ONDE CONTEM OS ERROS | CASO ARQUIVOS DE LOG NÃO ESTEJA CRIADO, USA-SE AS INFORMAÇÕES ABAIXO PARA CRIA-LOS
    # O ARQUIVO É ÚNICO, NÃO GERANDO UM POR DIA, COMO AS FUNÇÕES DE CLIENTE E PRODUTOS GERAM.
    @staticmethod
    def pasta_relatorios():
        local_pasta_relatorio = 'G:/Meu Drive/Estudos/Python/Pasta_teste_PYTHON/Relatorios/'
        return local_pasta_relatorio

    @staticmethod
    def criando_arquivos_txt_geral():
        relatorio_geral__ = RELATORIOS.pasta_relatorios() + 'Geral_mercadinho_.log'
        return relatorio_geral__

    # CASO ARQUIVOS DE LOG NÃO ESTEJA CRIADO, USA-SE AS INFORMAÇÕES ABAIXO PARA CRIA-LOS
    # PARA CRIAR UM ARQUIVO POR DIA, USA-SE A FUNCÃO 'data_mercadinho'
    @staticmethod
    def criando_arquivo_txt_cliente():
        relatorio_cliente = RELATORIOS.pasta_relatorios() + 'Relatorio_Cliente - ' + RELATORIOS.data_mercadinho() + '.log'
        return relatorio_cliente

    # CASO ARQUIVOS DE LOG NÃO ESTEJA CRIADO, USA-SE AS INFORMAÇÕES ABAIXO PARA CRIA-LOS
    # PARA CRIAR UM ARQUIVO POR DIA, USA-SE A FUNCÃO 'data_mercadinho'
    @staticmethod
    def criando_arquivo_txt_produto():
        relatorio_produto = RELATORIOS.pasta_relatorios() + 'Relatorio_Produto - ' + RELATORIOS.data_mercadinho() + '.log'
        return relatorio_produto

    # ADICIONA OS ERROS NOS LOGS QUE NÃO TIVEREM ERROS.
    # AS INFORMAÇÕES SÃO ADICIONADAS COM OS HORÁRIOS É DATA.
    @staticmethod
    def relatorio_geral_SEM_ERROS(msg_sem_erro):
        registrando_relatorio = open(RELATORIOS.criando_arquivos_txt_geral(), 'a')
        registrando_relatorio.write(f'PROCESSO REALIZADO SEM ERROS - {RELATORIOS.time_mercadinho()}'
                                    f' | MSG: {msg_sem_erro}\n')
        registrando_relatorio.close()

    # ADICIONA OS ERROS NO LOG QUE POSSUEM ERROS.
    # AS INFORMAÇÕES SÃO ADICIONADAS COM OS HORÁRIOS E DATA.
    @staticmethod
    def relatorio_geral_COM_ERROS(msg_com_erro):
        registrando_relatorio = open(RELATORIOS.criando_arquivos_txt_geral(), 'a')
        registrando_relatorio.write(f'OCORREU UM ERRO NO PROCESSO - {RELATORIOS.time_mercadinho()}'
                                    f' | MSG: {msg_com_erro}\n')
        registrando_relatorio.close()

    # FUNÇÃO DESTINADA PARA TESTES
    @staticmethod
    def horario():
        valor_1 = datetime.now()
        hora_certa = valor_1.strftime('%d-%m-%Y - %H-%M-%S')
        return hora_certa

    # DATA PARA ADICIONAR NOS ARQUIVOS DE RELATORIOS DE ERRO E ACERTOS. É GERADO TODOS OS DIAS.
    @staticmethod
    def data_mercadinho():
        data = str(date.today())
        return data

    # RESPONSÁVEL POR GERAR A DATA E HORA DOS ARQUIVOS DE LOG
    @staticmethod
    def time_mercadinho():
        data_relatorio = datetime.now()
        data_atual = data_relatorio.strftime('[%d-%m-%Y] | [%H:%M] | ==> ')
        return data_atual

    #  CASO OS ARQUIVOS DE RELATORIO NÃO ESTEJAM CRIADOS.
    @staticmethod
    def criando_arquivo(msg):
        novo_arq = open(msg, 'w')
        novo_arq.close()

    # VERIFICAR SE POSSUI OS ARQUIVOS DE RELATORIOS. É CHAMADO PELO 'verificacao_relatorios_txt'
    @staticmethod
    def verf_relatorio(msg):
        try:
            abrir_relat = open(msg, 'r')
            abrir_relat.close()
            return True
        except FileNotFoundError:
            return False

    # FUNÇÃO DESTINADA EM CRIAR A PASTA DE RELATORIOS.
    @staticmethod
    def pasta_relatorio():
        try:
            listdir('G:/Meu Drive/Estudos/Python/Pasta_teste_PYTHON/Relatorios')
        except FileNotFoundError:
            makedirs('G:/Meu Drive/Estudos/Python/Pasta_teste_PYTHON/Relatorios')

    #  VERIFICAR SE OS ARQUIVOS DE TEXTO ESTÃO CRIADOS, SERVE APENAS PARA 'LOGS'
    @staticmethod
    def verificacao_relatorios_txt():
        if not RELATORIOS.verf_relatorio(RELATORIOS.criando_arquivos_txt_geral()):
            RELATORIOS.criando_arquivo(RELATORIOS.criando_arquivos_txt_geral())

        if not RELATORIOS.verf_relatorio(RELATORIOS.criando_arquivo_txt_produto()):
            RELATORIOS.criando_arquivo(RELATORIOS.criando_arquivo_txt_produto())

        if not RELATORIOS.verf_relatorio(RELATORIOS.criando_arquivo_txt_cliente()):
            RELATORIOS.criando_arquivo(RELATORIOS.criando_arquivo_txt_cliente())


RELATORIOS = Relatorios_Mercadinho()
RELATORIOS.pasta_relatorio()
RELATORIOS.verificacao_relatorios_txt()


class mercadinho:
    self = None
    Aparencia.logo_principal('BEM VINDO AO MERCADINHO PINHEIRO')

    # SCRIPT PARA ABRIR UM PROGRAMA EM ESPECIFICO
    while True:
        try:
            Aparencia.logo_principal('ABRINDO O BANDO DE DADOS, ENTRE COM SUAS INFORMAÇÕES')
            Aparencia.logo_principal('DIGITE O USUÁRIO E A SENHA PARA SE CONECTAR AO BANCO DE DADOS')
            usuario = str(input('Usuário: '))
            password = str(input('Password: '))
            print('ABRINDO O BANCO DE DADOS, AGUARDE...!!')
            sleep(1)
            db_conexao = mysql.connector.connect(host='localhost', user='root', password='PE@Penso@',
                                                 database='mercadinho_pinheiro')
            print('Bando de dados conectado!!')
            RELATORIOS.relatorio_geral_SEM_ERROS('Banco de dados conectado!!')
            sleep(0.5)
            break
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                RELATORIOS.relatorio_geral_COM_ERROS(f'{error} - Banco de dados inexistente ')
                print('Banco de dados inexistente')
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                RELATORIOS.relatorio_geral_COM_ERROS(error)
                print('LOGIN OU SENHA INVÁLIDOS! Tente de novo!')
                sleep(0.5)
            else:
                RELATORIOS.relatorio_geral_COM_ERROS(error)
                print(f' ==>  {error}')
                print('Não foi possível conectar o banco de dados! Para continuar, VERIFIQUE SEU BANCO DE DADOS!')
                Aparencia.linha()
                Aparencia.apt_enter()

    # FUNÇÃO PARA CLASSIFICAR OS PRODUTOS EM CATEGORIAS, BUSCANDO AS INFORMAÇÕES NO BANCO DE DADOS

    def funcao_categoria(self):
        categorias = list()
        conectando_DB = self.db_conexao.cursor()
        comando_catg = "SELECT * FROM categorias_mercadinhos"
        conectando_DB.execute(comando_catg)
        for id_catg, nome_catg in conectando_DB:
            categorias.append(id_catg)
            categorias.append(nome_catg)
        return categorias

    def cadastrar(self):
        global id_categoria, categoria
        while True:
            Aparencia.logo_principal('JANELA DE CADASTRO...')
            print('''
            [1] CADASTRAR UM NOVO CLIENTES
            [2] CADASTRAR UM NOVO PRODUTOS
            [0] VOLTAR AO MENU PRINCIPAL
            ''')
            opc_cadastro = Aparencia.leiaInt('Escolha uma opção: ')

            # CADASTRO CLIENTES
            if opc_cadastro == 1:
                cont = 0
                Aparencia.logo_principal('CADASTRANDO CLIENTES...')
                while True:
                    while True:
                        nome_cliente = str(input('Nome do cliente: ')).upper()
                        if len(nome_cliente) == 0:
                            print('Esse campo não pode ficar vazio!')
                            cont += 1
                        else:
                            break
                    cpf_cliente = Aparencia.leiaInt('Entre com o CPF(Sem pontos): ')
                    data_nasc = str(input('Data de nascimento (ddmmaaaa): '))
                    if len(data_nasc) == 0:
                        data_nasc = '1900-01-01'
                    else:
                        data_nasc = data_nasc[4:8] + '-' + data_nasc[2:4] + '-' + data_nasc[0:2]
                    telefone = str(input('Telefone com DDD(opcional): '))
                    if len(telefone) == 0:
                        telefone = '(xx)xxxxx-xxxx'
                    email = str(input('Email do cliente (opcional): '))
                    if cont == 5:
                        print('Você não pode deixar esse campo vazio')
                        sleep(1)
                        print('Voltando ao menu...')
                        sleep(1)
                        break
                    Aparencia.linha()
                    print('Você adicionou as seguintes informações \n')
                    print(f'Nome do Cliente: {nome_cliente} \n'
                          f'CPF do cliente: {cpf_cliente} \n'
                          f'Data de Nascimento: {data_nasc} \n'
                          f'Telefone: {telefone} \n'
                          f'E-mail do Cliente: {email} \n')
                    resp = Aparencia.continuar_SN('Deseja adicionar essas informações no bando de dados?')
                    if resp == 'S':
                        try:
                            conexao_cliente = self.db_conexao.cursor()
                            comando_SQL_cliente: str = "INSERT INTO cliente_mercadinho (" \
                                                       "nome_cliente, cpf_cliente, data_nasc," \
                                                       "tel_cliente, email_cliente) " \
                                                       "VALUES (%s, %s, %s, %s, %s)"
                            valores_SQL_cliente = (nome_cliente, cpf_cliente, data_nasc, telefone, email)
                            conexao_cliente.execute(comando_SQL_cliente, valores_SQL_cliente)
                            print('Dados adicionados com sucesso!')
                            RELATORIOS.relatorio_geral_SEM_ERROS('Dados adicionados com sucesso! \n'
                                                                 f'{nome_cliente} \n'
                                                                 f'{cpf_cliente} \n'
                                                                 f'{data_nasc} \n'
                                                                 f'{telefone} \n'
                                                                 f'{email} \n')
                            sleep(1)
                        except mysql.connector.Error as erro:
                            print('Não foi possível adicionar os dados cadastrados'
                                  f'VERIFIQUE SEU BANDO DE DADOS\n ==> {erro}')
                            cadastro_produto_relatorio = [nome_cliente, cpf_cliente, data_nasc, telefone, email]
                            Aparencia.guardando(RELATORIOS.criando_arquivo_txt_cliente(),
                                                cadastro_produto_relatorio)
                            Aparencia.apt_enter()
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)
                            break
                    resp = Aparencia.continuar_SN('Adicionar outro cliente?')
                    if resp == 'N':
                        cadastro_produto_relatorio = [nome_cliente, cpf_cliente, data_nasc, telefone, email]
                        Aparencia.guardando(RELATORIOS.criando_arquivo_txt_produto(),
                                            cadastro_produto_relatorio)
                        RELATORIOS.relatorio_geral_SEM_ERROS('Você optou por CANCELAR A AÇÃO!')
                        break

            # CADASTRO PRODUTOS
            elif opc_cadastro == 2:
                while True:
                    Aparencia.linha()
                    nome_produto = str(input('Nome do produto: ')).upper()
                    if len(nome_produto) == 0:
                        print('Esse campo não pode ficar vazio, digite o nome do produto.')
                    else:
                        break
                add_catg = self.funcao_categoria()
                print(add_catg)
                Aparencia.apt_enter()
                for id_catg, nome_catg in add_catg:
                    id_categoria = id_catg
                    categoria = nome_catg
                fabricante = str(input(f'Fabricante do produto: {nome_produto}: ')).upper()
                if len(fabricante) == 0:
                    fabricante = '<desconhecido>'
                Aparencia.linha()
                valor_produto = Aparencia.leiaFloat('Valor do produto R$: ')
                print(f'Valores adicionados: \n  '
                      f' ==> Nome do produto: {nome_produto} \n  '
                      f' ==> Fabricante: {fabricante} \n  '
                      f' ==> Valor R$: {valor_produto} \n'
                      f' ==> ID: {id_categoria} | Categoria: {categoria} \n '
                      f'{Aparencia.linha()} \n')
                Aparencia.linha()
                Aparencia.apt_enter()
                resp = Aparencia.continuar_SN('Adicionar esse produto?')
                Aparencia.linha()
                if resp == 'S':
                    try:
                        conectar_tabela_produto = self.db_conexao.cursor()
                        comando_sql_add_produto = "INSERT INTO produtos_mercadinho " \
                                                  "(nome_produto, fabri_produto, valor_produto, id_categoria)" \
                                                  "VALUES(%s, %s, %s, %s)"
                        valor_sql_add_produto = (nome_produto, fabricante, valor_produto, id_categoria)
                        conectar_tabela_produto.execute(comando_sql_add_produto, valor_sql_add_produto)
                        RELATORIOS.relatorio_geral_SEM_ERROS(f'Dados adicionados com sucesso! \n'
                                                             f'{nome_produto} \n'
                                                             f'{fabricante} \n'
                                                             f'{valor_produto} \n'
                                                             f'{id_categoria}')
                    except mysql.connector.Error as erro:
                        print('Não foi possível adicionar os dados cadastrados'
                              f'VERIFIQUE SEU BANDO DE DADOS\n ==> {erro}')
                        RELATORIOS.relatorio_geral_COM_ERROS(erro)
                        cadastro_produto_relatorio = [nome_produto, fabricante, valor_produto]
                        Aparencia.guardando(RELATORIOS.criando_arquivo_txt_produto(),
                                            cadastro_produto_relatorio)
                elif resp == 'N':
                    cadastro_produto_relatorio = [nome_produto, fabricante, valor_produto]
                    Aparencia.guardando(RELATORIOS.criando_arquivo_txt_produto(), cadastro_produto_relatorio)
                    RELATORIOS.relatorio_geral_SEM_ERROS('Você optou por CANCELAR A AÇÃO!')
                    break
                else:
                    print('Produto não foi adicionado.. Voltando ao  menu anterior')
                    break

            # SAIR
            elif opc_cadastro == 0:
                print('Voltando ao menu principal...!')
                sleep(1)
                break
            else:
                opc_erro = Aparencia.continuar_SN('Voce escolheu uma opção INCORRETA')
                if opc_erro == 'S':
                    print('Escolha uma opção correta!!')
                    sleep(1)
                else:
                    print('Voltando ao menu principal!')
                    sleep(1)

    # VISUALIZANDO AS INFORMAÇÕES NO BANCO DE DADOS
    def visualizar_cadastros(self):
        global comando_SQL_cliente, dict_cliente
        conectando_banco_DB = self.db_conexao.cursor()

        def view_dados_cliente(dados_cliente):
            verif = list()
            for ID_CLIENTE, NOME, CPF, NASC, TELEFONE, EMAIL in dados_cliente:
                verif.append(ID_CLIENTE)
                print(f'ID: ==> {ID_CLIENTE} \n'
                      f'NOME: ==> {NOME} \n'
                      f'CPF: ==> {CPF} \n'
                      f'NASC: ==> {NASC} \n'
                      f'TELEFONE ==> {TELEFONE} \n'
                      f'EMAIL: ==> {EMAIL}')
                print('')
                Aparencia.linha()
            if len(verif) > 0:
                RELATORIOS.relatorio_geral_SEM_ERROS('Busca realizada com sucesso!')
            else:
                print('Não foi encontrado nenhum cadastro')
                RELATORIOS.relatorio_geral_SEM_ERROS('Busca realizada com sucesso! Mas não foi nenhum cadastro')

        def view_dados_produtos(dados_produtos):
            for ID_PRODUTO, NOME_PRODUTO, FABRICANTE_PRODUTO, VALOR_PRODUTO, ID_CATG in dados_produtos:

                print(f' ==> REGISTRO DO PRODUTO: {ID_PRODUTO} \n'
                      f' ==> NOME DO PRODUTO: {NOME_PRODUTO} \n'
                      f' ==> FABRICANTE: {FABRICANTE_PRODUTO} \n'
                      f' ==> VALOR R$:{VALOR_PRODUTO} '
                      f' ==> ID CATEGORIA: {ID_CATG}')
                print('')
                RELATORIOS.relatorio_geral_SEM_ERROS(f'As informações foram listadas com SUCESSO!')
            Aparencia.linha()
            Aparencia.apt_enter()

        while True:
            Aparencia.logo_principal('---CONSULTA DE CADASTROS DO MERCADINHO---')
            print('''
        ==> [1] VERIFICAR CADASTROS DE CLIENTES
        ==> [2] VERIFICAR CADASTROS DE PRODUTOS
        ==> [0] VOLTAR AO MENU PRINCIPAL
            ''')
            opc_consultar = Aparencia.leiaInt('Escolha uma opção: ')
            sleep(0.5)
            Aparencia.linha()

            # CONSULTANDO TABELA CLIENTE_MERCADINHO
            if opc_consultar == 1:
                print('''
                [1] BUSCAR POR TODA TABELA
                [2] BUSCAR POR INFORMAÇÕES ESPECIFICAS
                [0] VOLTAR AO MENU PRINCIPAL
                ''')
                resp_opcao = Aparencia.leiaInt('Escolha uma opção: ')
                Aparencia.linha()

                # BUSCAR POR TODOS OS DADOS DO CLIENTE.
                if resp_opcao == 1:
                    sleep(0.5)
                    lista_relatorio_cliente = list()
                    print('carregando...!!\n')
                    sleep(0.5)
                    while True:
                        try:
                            comando_SQL_cliente = "SELECT * FROM cliente_mercadinho"
                            conectando_banco_DB.execute(comando_SQL_cliente)
                            view_dados_cliente(conectando_banco_DB)
                        except mysql.connector.Error as erro:
                            print(f'Não foi possível localizar as informações')
                            print('Verifique se a conexão com o bando de dados esta normal.\n '
                                  f'==> {erro}')
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)
                            Aparencia.apt_enter()
                            break
                        resp_opcao = Aparencia.continuar_SN('Deseja realizar um relatório da busca?')
                        if resp_opcao == 'S':
                            conectando_banco_DB.execute(comando_SQL_cliente)
                            for id_cliente, nome_cliente, cpf_cliente, nasc_cliente, tel_cliente, mail_cliente in \
                                    conectando_banco_DB:
                                dict_cliente = {f'ID_CLIENTE: ': id_cliente,
                                                'NOME_CLIENTE: ': nome_cliente,
                                                'CPF_CLIENTE: ': cpf_cliente,
                                                'DATA_NASC: ': nasc_cliente,
                                                'TEL_CLIENTE: ': tel_cliente,
                                                'MAIL_CLIENTE: ': mail_cliente}
                                lista_relatorio_cliente.append(dict_cliente)
                            gerando_PDF(lista_relatorio_cliente)
                            Aparencia.apt_enter()
                            break
                        elif resp_opcao == 'N':
                            print('Voltando um menu!')
                            sleep(0.5)
                            break

                # BUSCANDO POR INFORMAÇÕES ESPECIFICAS
                elif resp_opcao == 2:
                    sleep(0.5)
                    while True:
                        print('''
                        [1] BUSCA POR NOME
                        [2] BUSCA POR CPF
                        [3] BUSCA POR TELEFONE
                        [4] BUSCA POR EMAIL
                        [0] Voltar
                        ''')
                        resp_busca = Aparencia.leiaInt('Escolha um opção: ')

                        # BUSCA REALIZADA POR NOME
                        if resp_busca == 1:
                            sleep(0.5)
                            nome_busca = str(input('Digite o nome do cliente: '))
                            try:
                                convertendo_STR = str("SELECT * FROM cliente_mercadinho "
                                                      "WHERE nome_cliente LIKE " + "'" + nome_busca + "%'")
                                comando_busca_nome = convertendo_STR
                                conectando_banco_DB.execute(comando_busca_nome)
                                view_dados_cliente(conectando_banco_DB)
                            except mysql.connector.Error as erro:
                                print(f' ==> {erro}')
                                RELATORIOS.relatorio_geral_COM_ERROS(erro)

                        # BUSCA REALIZADA POR CPF
                        elif resp_busca == 2:
                            sleep(0.5)
                            try:
                                busca_cpf = str(input("Digite o CPF (Sem acento): "))
                                convertendo_comando_STR = str("SELECT * FROM cliente_mercadinho "
                                                              "WHERE cpf_cliente = " + "'" + busca_cpf + "'")
                                comando_busco_cpf = convertendo_comando_STR
                                conectando_banco_DB.execute(comando_busco_cpf)
                                view_dados_cliente(conectando_banco_DB)
                            except mysql.connector.Error as erro:
                                print(f'Ocorreu um erro!\n'
                                      f'{erro}')
                                RELATORIOS.relatorio_geral_COM_ERROS(erro)

                        # BUSCA REALIZADA POR TELEFONE
                        elif resp_busca == 3:
                            sleep(0.5)
                            try:
                                busca_telefone = str(input('Digite o telefone(com DDD): '))
                                convertendo_comando_STR = str("SELECT * FROM cliente_mercadinho "
                                                              "WHERE tel_cliente = " + "'" + busca_telefone + "'")
                                comando_busca_tele = convertendo_comando_STR
                                conectando_banco_DB.execute(comando_busca_tele)
                                view_dados_cliente(conectando_banco_DB)
                            except mysql.connector.Error as erro:
                                print(f' ==> {erro}')
                                RELATORIOS.relatorio_geral_COM_ERROS(erro)

                        # BUSCA REALIZADA POR E-MAIL
                        elif resp_busca == 4:
                            sleep(0.5)
                            try:
                                buscar_email = str(input('Digite um e-mail: '))
                                convertendo_comando_STR = str("SELECT * FROM cliente_mercadinho "
                                                              "WHERE email_cliente = " + "'" + buscar_email + "'")
                                comando_busca_email = convertendo_comando_STR
                                conectando_banco_DB.execute(comando_busca_email)
                                view_dados_cliente(conectando_banco_DB)
                            except mysql.connector.Error as erro:
                                print(f' ==> {erro}')
                                RELATORIOS.relatorio_geral_COM_ERROS(erro)

                        # VOLTAR AO MENU ANTERIOR
                        if resp_busca == 0:
                            sleep(0.5)
                            print('Voltando ao menu!')
                            sleep(0.5)
                            break

            # VERIFICANDO TABELA PRODUTOS_MERCADINHO
            elif opc_consultar == 2:
                while True:
                    sleep(0.5)
                    print('''
                    [1] BUSCAR POR TODA TABELA
                    [2] BUSCAR POR INFORMAÇÕES ESPECIFICAS
                    [0] VOLTAR AO MENU PRINCIPAL
                    ''')
                    opcao_produto = Aparencia.leiaInt('Escolha uma opção: ')
                    sleep(1)

                    # BUSCA REALIZADO EM TODA TABELA
                    if opcao_produto == 1:
                        sleep(0.5)
                        print('Carregando o bando de dados...!!\n')
                        try:
                            comando_SQL_produtos = "SELECT * FROM produtos_mercadinho"
                            conectando_banco_DB.execute(comando_SQL_produtos)
                            view_dados_produtos(conectando_banco_DB)
                            Aparencia.linha()
                            resp_busca = Aparencia.continuar_SN('Deseja realizar mais um busca?')
                            if resp_busca == 'S':
                                print('Carregando o bando de dados...')
                            else:
                                break
                        except mysql.connector.Error as erro:
                            print('Não foi possível verificar as informações.\n'
                                  'Verifique seu bando de dados!'
                                  f' ==> {erro}')
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)

                    # REALIZAR UMA BUSCA ESPECIFICA
                    elif opcao_produto == 2:
                        sleep(0.5)
                        while True:
                            print('''
                            [1] BUSCA PELO ID DO PRODUTO
                            [2] BUSCA PELO NOME DO PRODUTO
                            [3] BUSCA PELO FABRICANTE DOS PRODUTOS
                            [4] BUSCA PELO VALOR
                            [5] BUSCA POR CATEGORIA
                            ''')
                            resp_busca_espc = Aparencia.leiaInt('Escolha uma opção: ')

                            # BUSCAR REALIZADA PELO ID DO PRODUTO
                            if resp_busca_espc == 1:
                                sleep(0.5)
                                try:
                                    busca_produto_ID = str(input('DIGITE O NUMERO DE ID DO PRODUTO: '))
                                    comando_sql_id_produto = "SELECT * FROM produtos_mercadinho " \
                                                             "WHERE reg_produto = " + busca_produto_ID
                                    conectando_banco_DB.execute(comando_sql_id_produto)
                                    view_dados_produtos(conectando_banco_DB)
                                except mysql.connector.Error as erro:
                                    print(f'NÃO FOI POSSÍVEL BUSCAR OS DADOS!! ==> {erro}')
                                    RELATORIOS.relatorio_geral_COM_ERROS(erro)

                            # BUSCAR REALIZADA PELO NOME DO PRODUTO
                            elif resp_busca_espc == 2:
                                sleep(0.5)
                                try:
                                    busca_produto_nome = str(input('DIGITE O NOME DO PRODUTO: '))
                                    comando_sql_nome_produto = "SELECT * FROM produtos_mercadinho " \
                                                               "WHERE nome_produto LIKE " + "'" + busca_produto_nome + "%'"
                                    conectando_banco_DB.execute(comando_sql_nome_produto)
                                    view_dados_produtos(conectando_banco_DB)
                                except mysql.connector.Error as erro:
                                    print(f'NÃO FOI POSSÍVEL BUSCAR OS DADOS!! ==> {erro}')
                                    RELATORIOS.relatorio_geral_COM_ERROS(erro)

                            # BUSCAR REALIZADA PELO FABRICANTE DO PRODUTO
                            elif resp_busca_espc == 3:
                                sleep(0.5)
                                try:
                                    busca_produto_fabricante = str(input('DIGITE O FABRICANTE DO PRODUTO: '))
                                    comando_sql_fabricante = "SELECT * FROM produtos_mercadinho " \
                                                             "WHERE fabricante LIKE " + "'" + busca_produto_fabricante + "%'"
                                    conectando_banco_DB.execute(comando_sql_fabricante)
                                    view_dados_produtos(conectando_banco_DB)
                                except mysql.connector.Error as erro:
                                    print(f'NÃO FOI POSSÍVEL BUSCAR OS DADOS!! ==> {erro}')
                                    RELATORIOS.relatorio_geral_COM_ERROS(erro)

                            # BUSCAR REALIZADA POR VALORES R$ DO PRODUTO
                            elif resp_busca_espc == 4:
                                sleep(0.5)
                                try:
                                    busca_produto_valor = str(input('QUAL VALOR DA BUSCA R$: '))
                                    comando_sql_valor = "SELECT * FROM produtos_mercadinho " \
                                                        "WHERE valor_produto = " + busca_produto_valor
                                    conectando_banco_DB.execute(comando_sql_valor)
                                    view_dados_produtos(conectando_banco_DB)
                                except mysql.connector.Error as erro:
                                    print(f'NÃO FOI POSSÍVEL BUSCAR OS DADOS!! ==> {erro}')
                                    RELATORIOS.relatorio_geral_COM_ERROS(erro)

                            # BUSCAR REALIZADA PELA CATEGORIA DO PRODUTO
                            elif resp_busca_espc == 5:
                                sleep(0.5)
                                busca_produto_categoria = self.funcao_categoria()
                                print(busca_produto_categoria)
                            else:
                                print('Opção invalida!')
                    elif opc_consultar == 0:
                        sleep(0.5)
                        print('Voltando para o menu de busca de produtos!!')
                        sleep(0.5)
                        break
                    else:
                        print('Você digitou uma opção invalida!!')
                        sleep(0.5)


MERCADINHO = mercadinho()


class menu_principal:
    global fechando_programa
    while True:
        print('''
    ==> [1] Realizar um cadastro (Clientes/Produtos)
    ==> [2] Consultando cadastros (Clientes/Produtos)
    ==> [0] Sair do programa
        ''')
        opc_menu_principal = Aparencia.leiaInt('Escolha uma opção: ')
        if opc_menu_principal == 1:
            print('Direcionando para opção escolhida...')
            sleep(0.5)
            MERCADINHO.cadastrar()
        elif opc_menu_principal == 2:
            print('Direcionando para opção escolhida...')
            sleep(0.5)
            MERCADINHO.visualizar_cadastros()
        elif opc_menu_principal == 0:
            print('Saindo do BANDO DE DADOS!')
            print('Fechando o programa!')
            sleep(0.5)
            mercadinho.db_conexao.close()
        else:
            print('Você escolheu uma opção invalida.')
            sleep(0.5)


MENU_PRINCIPAL = menu_principal()
