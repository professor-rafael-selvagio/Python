# gerar_inserts.py
import gerador_dados as gd
from conexao import obter_proximo_id  # Importa a função para obter IDs
from datetime import datetime

#gd.gerar_deletes()

# Obter os próximos IDs disponíveis
proximos_ids = obter_proximo_id()

# Formatar o nome do arquivo com data e hora
agora = datetime.now()
nome_arquivo = f"DataFaker/sql/arquivo_{agora.strftime('%Y%m%d_%H%M%S')}.sql"

# Abrir o arquivo em modo de escrita
with open(nome_arquivo, 'w') as f:
    # Gerar inserts para a tabela Jogos
    jogos_inserts = gd.gerar_inserts_jogos(10, proximos_ids)
    for insert in jogos_inserts:
        f.write(insert + '\n')

    # Gerar inserts para a tabela Usuarios
    usuarios_inserts = gd.gerar_inserts_usuarios(30, proximos_ids)
    for insert in usuarios_inserts:
        f.write(insert + '\n')

    # Gerar inserts para a tabela Transmissoes
    transmissoes_inserts = gd.gerar_inserts_transmissoes(100, proximos_ids)
    for insert in transmissoes_inserts:
        f.write(insert + '\n')

    # Gerar inserts para a tabela Comentarios
    comentarios_inserts = gd.gerar_inserts_comentarios(1000, proximos_ids)
    for insert in comentarios_inserts:
        f.write(insert + '\n')

print("Arquivo SQL gerado com sucesso!")
