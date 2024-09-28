import csv

dados = [
    {'Nome': 'João', 'Idade': 25, 'Cidade': 'São Paulo'},
    {'Nome': 'José', 'Idade': 39, 'Cidade': 'São Carlos'},
    {'Nome': 'Helena', 'Idade': 19, 'Cidade': 'Rio de Janeiro'},
]


with open('05-Modulo-CSV/dados_saida.csv', 'w', newline='') as arquivo_csv:
    campos = ['Nome', 'Idade', 'Cidade']
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)

    escritor_csv.writeheader()
    for dado in dados:
        escritor_csv.writerow(dado)
