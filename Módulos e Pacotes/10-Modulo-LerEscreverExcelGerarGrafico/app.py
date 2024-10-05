import pandas as pd
import os
import matplotlib.pyplot as plt

# Define o caminho do arquivo
caminho = os.getcwd()
caminho_arquivo = caminho + '/10-Modulo-LerEscreverExcelGerarGrafico/VendasDeBolos.xlsx'
# Lê o arquivo Excel
arquivo = pd.read_excel(caminho_arquivo)
# Exibe as primeiras 79 linhas do DataFrame
#print(arquivo.head(79))

# Cálculos de soma e média
soma_total = arquivo['Valor Total'].sum()
#print(soma_total)

quantidade = arquivo['Quantidade'].sum()
#print(quantidade)

media_unitario = arquivo['Valor Unitário'].mean()  # cálculo da média
#print(f'Função SUM -> {media_unitario}')

# Usando a função describe
estatisticas = arquivo.describe()  # calcula estatísticas descritivas
#print(estatisticas)

pedido_caro = arquivo['Valor Total'].max()
pedido_barato = arquivo['Valor Total'].min()
#print(f'Pedido mais caro: R${pedido_caro:.2f}')
#print(f'Pedido mais barato: R${pedido_barato:.2f}')



'''
total_sabor é a variavel que vai o agrupamento por sabor
arquivo é a variavel que contem o excel
.groupby é uma funcao que recebe por parametro o que vai ser agrupado
'''
total_sabor = arquivo.groupby('Sabor do Bolo')['Valor Total'].sum()
#print(total_sabor)




total_tamanho = arquivo.groupby('Tamanho do Bolo')['Quantidade'].sum()
#print(total_tamanho)
total_sabor = arquivo.groupby('Tamanho do Bolo')['Valor Total'].sum()
#print(total_sabor)
total_sabor_tamanho = arquivo.groupby(['Tamanho do Bolo', 'Sabor do Bolo'])['Valor Total'].sum()
print(total_sabor_tamanho)



caminho_novo_arquivo = caminho + '/10-Modulo-LerEscreverExcelGerarGrafico/TotalTamanho.xlsx'
total_sabor_tamanho.to_excel(caminho_novo_arquivo)


total_sabor_tamanho.unstack().plot(kind='bar', figsize=(10, 6), title="Total por Tamanho e Sabor")

plt.xlabel('Tamanho do Bolo')  # Define o rótulo do eixo x como "Tamanho do Bolo"
plt.ylabel('Valor Total')  # Define o rótulo do eixo y como "Valor Total"
plt.legend(title='Sabor do Bolo')  # Adiciona uma legenda ao gráfico com o título "Sabor do Bolo"
plt.grid(axis='y')  # Adiciona uma grade ao eixo y para facilitar a leitura dos valores

plt.show()  # Exibe o gráfico na tela
