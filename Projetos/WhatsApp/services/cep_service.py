import requests

class CepService:
    def buscar_cep(self, cep):
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if resposta.status_code == 200:
            conteudo = resposta.json()
            # Extrai apenas os dados desejados
            dados_relevantes = {
                'cep': conteudo.get('cep'),
                'logradouro': conteudo.get('logradouro'),
                'bairro': conteudo.get('bairro'),
                'localidade': conteudo.get('localidade'),
                'uf': conteudo.get('uf'),
                'ddd': conteudo.get('ddd'),
            }
            return dados_relevantes, resposta.status_code
        else:
            return {'erro': 'Erro ao buscar o CEP.'}, resposta.status_code
