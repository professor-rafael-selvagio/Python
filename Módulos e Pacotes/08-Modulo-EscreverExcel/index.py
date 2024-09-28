import pandas, os as sistema_operacional

# Caminho do arquivo Excel
caminho_do_arquivo = sistema_operacional.getcwd() + '/08-Modulo-EscreverExcel/VendasDeBolos.xlsx'

# Lendo o arquivo Excel (primeira aba)
arquivo = pandas.read_excel(caminho_do_arquivo)

# Definindo o caminho para o novo arquivo Excel
caminho_novo_arquivo = sistema_operacional.getcwd() + '/08-Modulo-EscreverExcel/NovaPlanilha.xlsx'

# Escrevendo o conteúdo na nova planilha
arquivo.to_excel(caminho_novo_arquivo, index=False, sheet_name='Dados Originais')

print(f'Conteúdo da planilha foi salvo em {caminho_novo_arquivo}')