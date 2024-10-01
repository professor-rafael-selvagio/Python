from flask import Blueprint, request, jsonify
import webbrowser
from urllib.parse import quote
from time import sleep
import pyautogui
import os
import pandas as pd

whatsapp_bp = Blueprint('whatsapp', __name__)

@whatsapp_bp.route('/enviar_mensagens', methods=['POST'])
def enviar_mensagens():
    dados = request.get_json()
    codigo = dados.get('codigo')

    # Validação do código
    if codigo != "454":  # Substitua "454" pelo código correto
        return jsonify({'erro': 'Código inválido!'}), 400

    # Ler planilha CSV e guardar informações sobre nome, telefone e mensagem
    alunos = []
    
    # Define o caminho para o arquivo CSV
    caminho_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'alunos.csv')
    
    try:
        df = pd.read_csv(caminho_csv)  # Lê o arquivo CSV
        for index, linha in df.iterrows():  # Itera sobre as linhas do DataFrame
            nome = linha['nome']  # Nome do aluno
            telefone = linha['whatsapp']  # Telefone do aluno
            status = linha['status']  # Status do aluno

            # Enviar mensagem apenas para alunos com status "real"
            if status.lower() == 'real':
                msg = "Essa mensagem está sendo enviada através do Backend do Programa desenvolvido usando Python e Flask. Obrigado!"
                mensagem = f'Olá {nome}. A origem da mensagem a seguir foi um arquivo CSV: {msg}'

                # Criar links personalizados do WhatsApp e enviar mensagens
                try:
                    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
                    webbrowser.open(link_mensagem_whatsapp)
                    sleep(10)
                    pyautogui.press('enter')

                    # Adiciona o aluno à lista
                    alunos.append({'nome': nome, 'whatsapp': telefone})
                except Exception as e:
                    print(f'Não foi possível enviar mensagem para {nome}. Erro: {e}')
    except Exception as e:
        return jsonify({'erro': f'Erro ao ler o arquivo CSV: {str(e)}'}), 500

    return jsonify({'mensagem': 'Mensagens enviadas com sucesso!', 'alunos': alunos}), 200
