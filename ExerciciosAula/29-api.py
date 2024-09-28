import requests
from click import clear
clear()

cep = input('Digite o CEP:')

req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
dic = req.json()




print(dic['logradouro'])