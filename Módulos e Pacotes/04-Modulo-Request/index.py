import requests

resposta = requests.get("https://www.google.com.br")
conteudo = resposta.text

print(conteudo) # Saída: conteúdo da página solicitada









'''
resposta = requests.get("https://viacep.com.br/ws/13574320/json/")
conteudo = resposta.text
  
print(conteudo) # Saída: conteúdo da página solicitada
print(f"Status da Requisição -> {resposta.status_code}") # Deve retornar 200 se a requisição for bem-sucedida
'''