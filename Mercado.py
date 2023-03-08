import mysql.connector
from mysql.connector import errorcode
from analise_dados import *
from datetime import datetime, date
from os import mkdir, listdir


# OBJETO PARA MELHORAR A APARENCIA DO PROGRAMA
class aparencia:
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
                    aparencia.linha()
                    print(resp)
                else:
                    return valor_opc
            except:
                aparencia.linha()
                print(resp)

    # FUNÇÃO DESTINADA EM 'DAR' UMA PAUSA, ANTES DE CONTINUAR
    @staticmethod
    def apt_enter():
        return input('Aperte o ENTER para continuar')

    # @staticmethod
    # def guardando(diretorio, valor_lista):
    #    abrindo_relatorio = open(diretorio, 'a')
    #    abrindo_relatorio.write(f'{valor_lista} \n')


APARENCIA = aparencia()


# OBJETO DE RELATORIOS
class relatorios_mercadinho:
    # CRIA ARQUIVO DE LOG GERAL, ONDE CONTEM OS ERROS | CASO ARQUIVOS DE LOG NÃO ESTEJA CRIADO, USA-SE AS INFORMAÇÕES ABAIXO PARA CRIA-LOS
    # O ARQUIVO É ÚNICO, NÃO GERANDO UM POR DIA, COMO AS FUNÇOES DE CLIENTE E PRODUTOS GERAM.
    @staticmethod
    def criando_arquivos_txt_geral():
        relatorio_geral__ = 'G:/Meu Drive/Estudos/Pasta_teste_PYTHON/Geral_mercadinho_.log'
        return relatorio_geral__

    # CASO ARQUIVOS DE LOG NÃO ESTEJA CRIADO, USA-SE AS INFORMAÇÕES ABAIXO PARA CRIA-LOS
    # PARA CRIAR UM ARQUIVO POR DIA, USA-SE A FUNCÃO 'data_mercadinho'
    @staticmethod
    def criando_arquivo_txt_cliente():
        relatorio_cliente = 'G:/Meu Drive/Estudos/Pasta_teste_PYTHON/Relatorio_Cliente - ' + RELATORIOS.data_mercadinho() + '.log'
        return relatorio_cliente

    # CASO ARQUIVOS DE LOG NÃO ESTEJA CRIADO, USA-SE AS INFORMAÇÕES ABAIXO PARA CRIA-LOS
    # PARA CRIAR UM ARQUIVO POR DIA, USA-SE A FUNCÃO 'data_mercadinho'
    @staticmethod
    def criando_arquivo_txt_produto():
        relatorio_produto = 'G:/Meu Drive/Estudos/Pasta_teste_PYTHON/Relatorio_Produto - ' + RELATORIOS.data_mercadinho() + '.log'
        return relatorio_produto

    # ADICIONA OS ERROS NOS LOGS QUE NÃO TIVEREM ERROS.
    # AS INFORMAÇÕES SÃO ADICIONADAS COM OS HORARIOS É DATA.
    @staticmethod
    def relatorio_geral_SEM_ERROS(msg_sem_erro):
        registrando_relatorio = open(RELATORIOS.criando_arquivos_txt_geral(), 'a')
        registrando_relatorio.write(f'PROCESSO REALIZADO SEM ERROS - {RELATORIOS.time_mercadinho()}'
                                    f' | MSG: {msg_sem_erro}\n')
        registrando_relatorio.close()

    # ADICIONA OS ERROS NO LOG QUE POSSUEM ERROS.
    # AS INFORMAÇÕES SÃO ADICIONADAS COM OS HORARIOS É DATA.
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

    # RESPONSAVEL POR GERAR A DATA E HORA DOS ARQUIVOS DE LOG
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
            listdir('C:/Relatorios/')
        except FileNotFoundError:
            mkdir('C:/Relatorios/')

    #  VERIFICAR SE OS ARQUIVOS DE TEXTO ESTÃO CRIADOS, SERVE APENAS PARA 'LOGS'
    @staticmethod
    def verificacao_relatorios_txt():
        if not RELATORIOS.verf_relatorio(RELATORIOS.criando_arquivos_txt_geral()):
            RELATORIOS.criando_arquivo(RELATORIOS.criando_arquivos_txt_geral())

        if not RELATORIOS.verf_relatorio(RELATORIOS.criando_arquivo_txt_produto()):
            RELATORIOS.criando_arquivo(RELATORIOS.criando_arquivo_txt_produto())

        if not RELATORIOS.verf_relatorio(RELATORIOS.criando_arquivo_txt_cliente()):
            RELATORIOS.criando_arquivo(RELATORIOS.criando_arquivo_txt_cliente())


RELATORIOS = relatorios_mercadinho()
RELATORIOS.pasta_relatorio()
RELATORIOS.verificacao_relatorios_txt()


class mercadinho:
    aparencia.logo_principal('BEM VINDO AO MERCADINHO PINHEIRO')

    # SCRIPT PARA ABRIR UM PROGRAMA EM ESPECIFICO
    while True:
        try:
            aparencia.logo_principal('ABRINDO O BANDO DE DADOS, ENTRE COM SUAS INFORMAÇÕES')
            aparencia.logo_principal('DIGITE O USUÁRIO E A SENHA PARA SE CONECTAR AO BANCO DE DADOS')
            usuario = str(input('Usuário: '))
            password = str(input('Password: '))
            print('ABRINDO O BANCO DE DADOS, AGUARDE...!!')
            sleep(1)
            db_conexao = mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password=password,
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
                aparencia.linha()
                aparencia.apt_enter()

    # FUNÇÃO PARA CLASSIFICAR OS PRODUTOS EM CATEGORIAS
    # É POSSUI ACRESCENTAR MAIS CATEGORIAS
    @staticmethod
    def funcao_categoria():
        print('''
                [1] PADARIA
                [2] HORTIFRÚTI
                [3] CONGELADOS
                [4] FRIOS
                [5] AÇOUGUE
                [6] ALIMENTOS
                [7] BEBIDAS
                [8] HIGIENE PESSOAL
                [9] PRODUTOS DE LIMPEZA
                [10] PAPELARIA
                [11] LATICÍNIOS
                ''')
        opcao_f_categoria = aparencia.leiaInt('Categoria: ')
        if opcao_f_categoria == 1:
            return ['PADARIA', 1]
        elif opcao_f_categoria == 2:
            return ['HORTIFRÚTI', 2]
        elif opcao_f_categoria == 3:
            return ['CONGELADOS', 3]
        elif opcao_f_categoria == 4:
            return ['FRIOS', 4]
        elif opcao_f_categoria == 5:
            return ['AÇOUGUE', 5]
        elif opcao_f_categoria == 6:
            return ['ALIMENTOS', 6]
        elif opcao_f_categoria == 7:
            return ['BEBIDAS', 7]
        elif opcao_f_categoria == 8:
            return ['HIGIENE PESSOAL', 8]
        elif opcao_f_categoria == 9:
            return ['PRODUTOS DE LIMPEZA', 9]
        elif opcao_f_categoria == 10:
            return ['PAPELARIA', 10]
        elif opcao_f_categoria == 11:
            return ['LATICÍNIOS', 11]
        else:
            opc_categoria = aparencia.continuar_SN('Essa categoria não existe, deseja adicionar outra?')
            if opc_categoria == 'S':
                print('<desenvolvimento!>\n')
                print('Escolha uma categoria valida')
                sleep(1)

    def cadastrar(self):
        global id_categoria, categoria
        while True:
            aparencia.logo_principal('JANELA DE CADASTRO...')
            print('''
            [1] CADASTRAR UM NOVO CLIENTES
            [2] CADASTRAR UM NOVO PRODUTOS
            [0] VOLTAR AO MENU PRINCIPAL
            ''')
            opc_cadastro = aparencia.leiaInt('Escolha uma opção: ')

            # CADASTRO CLIENTES
            if opc_cadastro == 1:
                cont = 0
                aparencia.logo_principal('CADASTRANDO CLIENTES...')
                while True:
                    while True:
                        nome_cliente = str(input('Nome do cliente: ')).upper()
                        if len(nome_cliente) == 0:
                            print('Esse campo não pode ficar vazio!')
                            cont += 1
                        else:
                            break
                    cpf_cliente = aparencia.leiaInt('Entre com o CPF(Sem pontos): ')
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
                    aparencia.linha()
                    print('Você adicionou as seguintes informações \n')
                    print(f'Nome do Cliente: {nome_cliente} \n'
                          f'CPF do cliente: {cpf_cliente} \n'
                          f'Data de Nascimento: {data_nasc} \n'
                          f'Telefone: {telefone} \n'
                          f'E-mail do Cliente: {email} \n')
                    resp = aparencia.continuar_SN('Deseja adicionar essas informações no bando de dados?')
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
                            aparencia.guardando(RELATORIOS.criando_arquivo_txt_cliente(),
                                                cadastro_produto_relatorio)
                            aparencia.apt_enter()
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)
                            break
                    resp = aparencia.continuar_SN('Adicionar outro cliente?')
                    if resp == 'N':
                        cadastro_produto_relatorio = [nome_cliente, cpf_cliente, data_nasc, telefone, email]
                        aparencia.guardando(RELATORIOS.criando_arquivo_txt_produto(),
                                            cadastro_produto_relatorio)
                        RELATORIOS.relatorio_geral_SEM_ERROS('Você optou por CANCELAR A AÇÃO!')
                        break

            # CADASTRO PRODUTOS
            elif opc_cadastro == 2:
                while True:
                    aparencia.linha()
                    nome_produto = str(input('Nome do produto: ')).upper()
                    if len(nome_produto) == 0:
                        print('Esse campo não pode ficar vazio, digite o nome do produto.')
                    else:
                        break
                aparencia.linha()
                # categoria_GERAL = self.funcao_categoria()
                for id_catg, txt_catg in self.funcao_categoria():
                    id_categoria = int(id_catg)
                    categoria = str(txt_catg)
                fabricante = str(input(f'Fabricante do produto: {nome_produto}: ')).upper()
                if len(fabricante) == 0:
                    fabricante = '<desconhecido>'
                aparencia.linha()
                valor_produto = aparencia.leiaFloat('Valor do produto R$: ')
                print(f'Valores adicionados: \n  '
                      f' ==> {nome_produto} \n  '
                      f' ==> ID: {id_categoria} {categoria} \n '
                      f' ==> {fabricante} \n  '
                      f' ==> {valor_produto} \n'
                      f'{aparencia.linha()} \n')
                aparencia.linha()
                aparencia.apt_enter()
                resp = aparencia.continuar_SN('Adicionar esse produto?')
                aparencia.linha()
                if resp == 'S':
                    try:
                        conectar_tabela_produto = self.db_conexao.cursor()
                        comando_sql_add_produto = "INSERT INTO produtos_mercadinho " \
                                                  "(nome_produto, fabri_produto, valor_produto, id_categoria)" \
                                                  "VALUES(%s, %s, %s, %s)"
                        valor_sql_add_produto = (nome_produto, fabricante, valor_produto)
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
                        aparencia.guardando(RELATORIOS.criando_arquivo_txt_produto(),
                                            cadastro_produto_relatorio)
                elif resp == 'N':
                    cadastro_produto_relatorio = [nome_produto, fabricante, valor_produto]
                    aparencia.guardando(RELATORIOS.criando_arquivo_txt_produto(), cadastro_produto_relatorio)
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
                opc_erro = aparencia.continuar_SN('Voce escolheu uma opção INCORRETA')
                if opc_erro == 'S':
                    print('Escolha uma opção correta!!')
                    sleep(1)
                else:
                    print('Voltando ao menu principal!')
                    sleep(1)

    # VISUALIZANDO AS INFORMAÇÕES NO BANCO DE DADOS
    def visualizar_cadastros(self):
        global comando_SQL_cliente, dict_cliente, visualizacao
        conectando_banco_DB = self.db_conexao.cursor()

        def view_dados_cliente(dados_cliente):
            try:
                for ID_CLIENTE, NOME, CPF, NASC, TELEFONE, EMAIL in dados_cliente:
                    print(f'ID: ==> {ID_CLIENTE} \n' f'NOME: ==> {NOME} \n' f'CPF: ==> {CPF} \n'
                          f'NASC: ==> {NASC} \n' f'TELEFONE ==> {TELEFONE} \n' f'EMAIL: ==> {EMAIL}')
                    aparencia.linha()
                RELATORIOS.relatorio_geral_SEM_ERROS('Busca realizada com sucesso!')
                print()
                aparencia.apt_enter()
            except:
                print('NÃO FOI POSSÍVEL LISTAS OS DADOS DOS CLIENTE')

        def view_dados_produtos(dados_produtos):
            try:
                for ID_PRODUTO, NOME_PRODUTO, FABRICANTE_PRODUTO, VALOR_PRODUTO in dados_produtos:
                    print(f' ==> REGISTRO DO PRODUTO: {ID_PRODUTO} \n'
                          f' ==> NOME DO PRODUTO: {NOME_PRODUTO} \n'
                          f' ==> FABRICANTE: {FABRICANTE_PRODUTO} \n'
                          f' ==> R$:{VALOR_PRODUTO} ')
                    aparencia.linha()
                    RELATORIOS.relatorio_geral_SEM_ERROS('Busca realizada com sucesso na tabela "produtos_mercadinho"')
                aparencia.apt_enter()
            except:
                print('NÃO FOI POSSÍVEL LISTAS OS DADOS DOS CLIENTE')

        while True:
            aparencia.logo_principal('---CONSULTA DE CADASTROS DO MERCADINHO---')
            print('''
        ==> [1] VERIFICAR CADASTROS DE CLIENTES
        ==> [2] VERIFICAR CADASTROS DE PRODUTOS
        ==> [0] VOLTAR AO MENU PRINCIPAL
            ''')
            opc_consultar = aparencia.leiaInt('Escolha uma opção: ')
            aparencia.linha()

            # CONSULTANDO TABELA CLIENTE_MERCADINHO
            if opc_consultar == 1:
                print('''
                [1] BUSCAR POR TODA TABELA
                [2] BUSCAR POR INFORMAÇÕES ESPECIFICAS
                [0] VOLTAR AO MENU PRINCIPAL
                ''')
                resp_opcao = aparencia.leiaInt('Escolha uma opção: ')
                aparencia.linha()

                # BUSCAR POR TODOS OS DADOS DO CLIENTE.
                if resp_opcao == 1:
                    lista_relatorio_cliente = list()
                    print('carregando...!!\n')
                    while True:
                        try:
                            comando_SQL_cliente = "SELECT * FROM cliente_mercadinho"
                            conectando_banco_DB.execute(comando_SQL_cliente)
                            view_dados_cliente(conectando_banco_DB)
                            visualizacao = True
                        except mysql.connector.Error as erro:
                            print(f'Não foi possível localizar as informações')
                            print('Verifique se a conexão com o bando de dados esta normal.\n '
                                  f'==> {erro}')
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)
                            visualizacao = False
                            aparencia.apt_enter()
                            break
                        aparencia.linha()
                        if visualizacao:
                            resp_opcao = aparencia.continuar_SN('Deseja realizar um relatório da busca?')
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
                                break
                        elif resp_opcao == 'N':
                            print('Voltando um menu!')
                            break
                        else:
                            print('Voce digitou uma opção invalida!')

                # BUSCANDO POR INFORMAÇÕES ESPECIFICAS
                elif resp_opcao == 2:
                    while True:
                        print('''
                        [1] BUSCA POR NOME
                        [2] BUSCA POR CPF
                        [3] BUSCA POR TELEFONE
                        [4] BUSCA POR EMAIL
                        [0] Voltar
                        ''')
                        resp_busca = aparencia.leiaInt('Escolha um opção: ')

                        # BUSCA REALIZADA POR NOME
                        if resp_busca == 1:
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
                            print('Voltando ao menu!')
                            sleep(1)
                            break

            # VERIFICANDO TABELA PRODUTOS_MERCADINHO
            elif opc_consultar == 2:
                print('''
                [1] BUSCAR POR TODA TABELA
                [2] BUSCAR POR INFORMAÇÕES ESPECIFICAS
                [0] VOLTAR AO MENU PRINCIPAL
                ''')
                opcao_produto = aparencia.leiaInt('Escolha uma opção: ')

                # BUSCA REALIZADO EM TODA TABELA
                if opcao_produto == 1:
                    print('carregando...!!\n')
                    consultar_produtos = self.db_conexao.cursor()
                    try:
                        comando_SQL_produtos = "SELECT * FROM produtos_mercadinho"
                        consultar_produtos.execute(comando_SQL_produtos)
                        for ID_PRODUTO, NOME_PRODUTO, FABRI_PRODUTO, VALOR_PRODUTO in consultar_produtos:
                            print(f'Registro: {ID_PRODUTO} \n'
                                  f'Nome do produto: {NOME_PRODUTO} \n'
                                  f'Fabricante: {FABRI_PRODUTO} \n'
                                  f'Valor do produto R$:{VALOR_PRODUTO}')
                            aparencia.linha()
                            RELATORIOS.relatorio_geral_SEM_ERROS(f'As informações foram listadas com SUCESSO! \n'
                                                                 f'ID: {ID_PRODUTO} \n'
                                                                 f'{NOME_PRODUTO} \n'
                                                                 f'{FABRI_PRODUTO} \n'
                                                                 f'{VALOR_PRODUTO} \n')
                    except mysql.connector.Error as erro:
                        print('Não foi possível verificar as informações.\n'
                              'Verifique seu bando de dados!'
                              f' ==> {erro}')
                        RELATORIOS.relatorio_geral_COM_ERROS(erro)
                    aparencia.apt_enter()

                # REALIZAR UMA BUSCA ESPECIFICA
                elif opcao_produto == 2:
                    print('''
                    [1] BUSCA PELO ID DO PRODUTO
                    [2] BUSCA PELO NOME DO PRODUTO
                    [3] BUSCA PELO FABRICANTE DOS PRODUTOS
                    [4] BUSCA PELO VALOR
                    ''')
                    resp_busca_espc = aparencia.leiaInt('Escolha uma opção: ')

                    # BUSCAR REALIZADA PELO ID DO PRODUTO
                    if resp_busca_espc == 1:
                        try:
                            busca_produto_ID = str(input('DIGITE O NUMERO DE ID DO PRODUTO: '))
                            comando_sql_id_produto = "SELECT * FROM produtos_mercadinho " \
                                                     "'WHERE registro_produto = '" + busca_produto_ID + "'"
                            conectando_banco_DB.execute(comando_sql_id_produto)
                            view_dados_produtos(conectando_banco_DB)
                        except mysql.connector.Error as erro:
                            print(f'NÃO FOI POSSÍVEL BUSCAR OS DADOS!! ==> {erro}')
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)

                    # BUSCAR REALIZADA PELO NOME DO PRODUTO
                    elif resp_busca_espc == 2:
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
                        try:
                            busca_produto_valor = str(input('QUAL VALOR DA BUSCA R$: '))
                            comando_sql_valor = "SELECT * FROM produtos_mercadinho " \
                                                "WHERE valor_produto = " + busca_produto_valor
                            conectando_banco_DB.execute(comando_sql_valor)
                            view_dados_produtos(conectando_banco_DB)
                        except mysql.connector.Error as erro:
                            print(f'NÃO FOI POSSÍVEL BUSCAR OS DADOS!! ==> {erro}')
                            RELATORIOS.relatorio_geral_COM_ERROS(erro)
                    else:
                        print('Opção invalida!')
            elif opc_consultar == 0:
                print('Voltando ao menu principal!!')
                sleep(1)
                break
            else:
                print('Você digitou uma opção invalida!!')
                sleep(0.5)


abrindo_mercadinho = mercadinho()


class menu_principal:
    global fechando_programa
    while True:
        print('''
    ==> [1] Realizar um cadastro (Clientes/Produtos)
    ==> [2] Consultando cadastros (Clientes/Produtos)
    ==> [0] Sair do programa
        ''')
        opc_menu_principal = APARENCIA.leiaInt('Escolha uma opção: ')
        if opc_menu_principal == 1:
            print('Direcionando para opção escolhida...')
            abrindo_mercadinho.cadastrar()
        elif opc_menu_principal == 2:
            print('Direcionando para opção escolhida...')
            abrindo_mercadinho.visualizar_cadastros()
        elif opc_menu_principal == 0:
            print('Saindo do BANDO DE DADOS!')
            print('Fechando o programa!')
            abrindo_mercadinho.db_conexao.close()
        else:
            print('Você escolheu uma opção invalida.')


MENU_PRINCIPAL = menu_principal()
