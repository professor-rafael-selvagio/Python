import pandas, os as sistema_operacional

# Caminho do arquivo Excel
caminho_do_arquivo = sistema_operacional.getcwd() + '/07-Modulo-LerExcel/VendasDeBolos.xlsx'

# Lendo o arquivo Excel (primeira aba)
arquivo = pandas.read_excel(caminho_do_arquivo)

# Mostrando as primeiras 5 linhas
#print(pandas.head())

# Somar o total da coluna Valor Total
soma_total = arquivo['Valor Total'].sum()

# Total de pedidos: Contar o número total de pedidos na planilha
total_pedidos = arquivo['ID do Pedido'].nunique()
print(f"Total de pedidos: {total_pedidos}")

# Total de vendas: Somar o valor total de todos os pedidos
total_vendas = arquivo['Valor Total'].sum()
print(f"Total de vendas: R${total_vendas:.2f}")

# Média do valor total por pedido: Calcular a média do valor dos pedidos
media_valor_pedido = arquivo['Valor Total'].mean()
print(f"Média do valor total por pedido: R${media_valor_pedido:.2f}")

# Quantidade total de bolos vendidos: Somar a coluna 'Quantidade' para ver quantos bolos foram vendidos
total_bolos_vendidos = arquivo['Quantidade'].sum()
print(f"Quantidade total de bolos vendidos: {total_bolos_vendidos}")

# Pedido mais caro e mais barato: Encontrar o pedido com o maior e menor valor
pedido_mais_caro = arquivo['Valor Total'].max()
pedido_mais_barato = arquivo['Valor Total'].min()
print(f"Pedido mais caro: R${pedido_mais_caro:.2f}")
print(f"Pedido mais barato: R${pedido_mais_barato:.2f}")

# Total por sabor: Somar o valor total das vendas para cada sabor de bolo
total_por_sabor = arquivo.groupby('Sabor do Bolo')['Valor Total'].sum()
print("Total por sabor de bolo:")
print(total_por_sabor)