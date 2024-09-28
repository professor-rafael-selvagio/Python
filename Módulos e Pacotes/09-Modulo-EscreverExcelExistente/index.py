import pandas as pd
import os

# Caminho do arquivo Excel
caminho_do_arquivo = os.getcwd() + '/09-Modulo-EscreverExcelExistente/VendasDeBolos.xlsx'

# Lendo o arquivo Excel (primeira aba)
arquivo = pd.read_excel(caminho_do_arquivo)

# Definindo o caminho para o arquivo Excel existente onde os dados serão adicionados
caminho_arquivo_existente = os.getcwd() + '/09-Modulo-EscreverExcelExistente/NovaPlanilha.xlsx'

# Lendo a planilha existente
try:
    planilha_existente = pd.read_excel(caminho_arquivo_existente, sheet_name='Dados Originais')
except FileNotFoundError:
    # Se o arquivo não existir, cria um DataFrame vazio
    planilha_existente = pd.DataFrame()

# Adicionando o conteúdo do arquivo original à planilha existente
planilha_existente = pd.concat([planilha_existente, arquivo], ignore_index=True)

# Escrevendo o conteúdo atualizado de volta para a planilha existente
planilha_existente.to_excel(caminho_arquivo_existente, index=False, sheet_name='Dados Originais')

print(f'Conteúdo da planilha foi atualizado em {caminho_arquivo_existente}')
