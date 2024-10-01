from faker import Faker
import random
import xml.etree.ElementTree as ET
import os
from services.cep_service import CepService

cep_service = CepService()  # Inicializa o CepService

class FakerService:
    def __init__(self, num_contatos=5):
        self.fake = Faker()
        self.num_contatos = num_contatos
        self.ceps = self.carregar_ceps_do_xml()  # Carregar os CEPS do XML ao inicializar a classe

    def gerar_dados_falsos(self):
        data = []
        for _ in range(self.num_contatos):  # Gerar contatos
            nome = self.fake.name()
            whatsapp = self.gerar_telefone_brasileiro()
            idade = self.fake.random_int(min=18, max=70)

            cep = self.escolher_cep_randomicamente()  # Escolhe um CEP aleatório do XML
            dados_cep, status_code = cep_service.buscar_cep(cep)

            aluno = {
                'nome': nome,
                'whatsapp': whatsapp,
                'idade': idade,
                'cep': cep,  # Salva apenas o CEP original
                'logradouro': dados_cep.get('logradouro'),  # Salva o logradouro
                'bairro': dados_cep.get('bairro'),          # Salva o bairro
                'localidade': dados_cep.get('localidade'),  # Salva a localidade
                'uf': dados_cep.get('uf'),                  # Salva a UF
                'ddd': dados_cep.get('ddd'),                # Salva o DDD
                'status': 'fake'
            }

            data.append(aluno)

        return data  # Retorna a lista de alunos gerados

    def carregar_bairro(self, cep):
        # Implementar lógica para obter o bairro com base no CEP
        return "Bairro Exemplo"

    def carregar_localidade(self, cep):
        # Implementar lógica para obter a localidade com base no CEP
        return "Localidade Exemplo"

    def carregar_uf(self, cep):
        # Implementar lógica para obter a UF com base no CEP
        return "SP"  # Exemplo: São Paulo

    def gerar_telefone_brasileiro(self):
        ddd = self.fake.random_int(min=16, max=16)  # Gera um DDD fictício
        numero = f"{random.randint(9000, 9999)}{random.randint(1000, 9999)}"
        return f"55{ddd}9{numero}"  # Formata o número no padrão brasileiro

    def escolher_cep_randomicamente(self):
        return random.choice(self.ceps) if self.ceps else None

    def carregar_ceps_do_xml(self):
        arquivo = 'Projetos/WhatsApp/data/ceps_sao_carlos.xml'
        ceps = []

        if os.path.exists(arquivo):
            tree = ET.parse(arquivo)
            root = tree.getroot()

            for cep_element in root.findall('Cep'):
                ceps.append(cep_element.text)

        return ceps
