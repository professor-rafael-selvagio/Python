from flask import Blueprint, request, jsonify
from services.aluno_service import AlunoService
from services.cep_service import CepService

aluno_bp = Blueprint('alunos', __name__)
aluno_service = AlunoService()  # Inicializa com persistência CSV por padrão
cep_service = CepService()  # Inicializa o CepService

@aluno_bp.route('/cadastro_aluno', methods=['POST'])
def cadastrar_aluno():
    dados = request.get_json()
    nome = dados.get('nome')
    whatsapp = dados.get('whatsapp')
    idade = dados.get('idade')
    cep = dados.get('cep')

    if not nome or not whatsapp:
        return jsonify({'erro': 'Nome e número do WhatsApp são obrigatórios!'}), 400

    # Consome o cep_service para buscar dados do CEP
    dados_cep, status_code = cep_service.buscar_cep(cep)

    if status_code != 200:
        return jsonify({'erro': 'Erro ao buscar informações do CEP.'}), status_code

    # Adiciona as informações do CEP ao dicionário do aluno
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
        'status': 'real'
        
    }

    aluno_service.salvar_aluno(aluno)

    return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'}), 201
