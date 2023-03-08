from reportlab.pdfgen import canvas
from time import sleep
from datetime import datetime
horario = datetime.now()
hora_atual = horario.strftime('%d-%m-%Y - %H-%M')


def gerando_PDF(msg_txt):
    fonte_padrao = "Helvetica-Oblique"
    nome_arquivo_pdf = str('C:/Relatorios/DADOS_CLIENTE_MERCADINHO')
    arquivo_PDF = canvas.Canvas(f'{nome_arquivo_pdf} - {hora_atual}.pdf')
    x = 720
    for valor in msg_txt:
        for chaves, valores in valor.items():
            x -= 20
            arquivo_PDF.drawString(20, x, f'{chaves} - {valores} \n '
                                          f'{"-" * 100}')
    arquivo_PDF.setTitle(nome_arquivo_pdf)  # TITULO PARA O ARQUIVO PDF
    arquivo_PDF.setFont(fonte_padrao, 14)  # FONTE PARA O TITULO
    arquivo_PDF.drawString(250, 850, "CLIENTES MERCADINHO PINHEIRO")
    arquivo_PDF.setFont(fonte_padrao, 14)
    # arquivo_PDF.drawString(245, 724, "ID_CLIENTE, NOME, CPF, DATA NASCIMENTO, TELEFONE, E-MAIL")
    arquivo_PDF.save()
    print(f'{nome_arquivo_pdf}.pdf criado com sucesso!')
    sleep(1)
