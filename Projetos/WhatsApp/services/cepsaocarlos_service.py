import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os

def obter_ceps_sao_carlos():
    url = 'https://buscacep.com.br/estado/sao-paulo/sao-carlos'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        ceps = []

        # Encontre a tabela que contém os CEPs
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')[1:]  # Ignora o cabeçalho da tabela

            for row in rows:
                columns = row.find_all('td')
                if columns and len(columns) > 0:
                    cep = columns[3].text.strip()  # O primeiro TD contém o CEP
                    ceps.append(cep)

        return ceps
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return []

def gerar_xml_ceps(ceps, arquivo='Projetodata/ceps_sao_carlos.xml'):
    # Certifique-se de que o diretório "data" existe
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)

    root = ET.Element('Ceps')  # Elemento raiz

    for cep in ceps:
        cep_element = ET.SubElement(root, 'Cep')
        cep_element.text = cep

    # Cria o arquivo XML
    tree = ET.ElementTree(root)
    tree.write(arquivo, encoding='utf-8', xml_declaration=True)
    print(f"Arquivo XML gerado: {arquivo}")

# Uso das funções
ceps_sao_carlos = obter_ceps_sao_carlos()
if ceps_sao_carlos:
    gerar_xml_ceps(ceps_sao_carlos)
