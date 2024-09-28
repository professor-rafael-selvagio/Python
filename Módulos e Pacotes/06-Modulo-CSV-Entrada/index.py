import csv, os

with open(f'{os.getcwd()}/06-Modulo-CSV-Entrada/dados_entrada.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:
        print(linha)
