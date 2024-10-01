from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from services.faker_service import FakerService
from services.aluno_service import AlunoService

faker_bp = Blueprint('faker', __name__)
faker_service = FakerService()  # Inicializa o FakerService
aluno_service = AlunoService()

# Armazena a senha gerada
senha_protegida = generate_password_hash('SenaiPython')

@faker_bp.route('/gerar_dados_fake', methods=['POST'])
def gerar_dados_fake():
    dados = request.get_json()
    senha = dados.get('senha')

    # Verifica se a senha está correta
    if not senha or not check_password_hash(senha_protegida, senha):
        return jsonify({'erro': 'Senha incorreta!'}), 403

    # Gera dados falsos e retorna
    dados_fake = faker_service.gerar_dados_falsos()  # Gera os dados falsos
    aluno_service.salvar_aluno(dados_fake)
    return jsonify({'mensagem': 'Dados falsos gerados com sucesso!'}), 201
