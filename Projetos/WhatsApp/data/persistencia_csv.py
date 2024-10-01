import pandas as pd
import os
from .data_interface import DataInterface

class PersistenciaCSV(DataInterface):
    def __init__(self, arquivo='alunos.csv'):
        # Obtém o diretório onde este arquivo está localizado
        dir_atual = os.path.dirname(os.path.abspath(__file__))
        # Cria o caminho completo para o arquivo CSV
        self.arquivo = os.path.join(dir_atual, arquivo)

    def salvar_aluno(self, aluno):
        # Converte o aluno em um DataFrame
        aluno_df = pd.DataFrame([aluno])
        
        if os.path.exists(self.arquivo):
            # Lê o arquivo existente
            planilha = pd.read_csv(self.arquivo)
            # Concatena o novo aluno
            planilha = pd.concat([planilha, aluno_df], ignore_index=True)
        else:
            # Se o arquivo não existir, cria um novo DataFrame
            planilha = aluno_df
        
        # Salva o DataFrame atualizado de volta no arquivo CSV
        planilha.to_csv(self.arquivo, index=False)

    def buscar_alunos(self):
        if os.path.exists(self.arquivo):
            return pd.read_csv(self.arquivo).to_dict(orient='records')
        return []
