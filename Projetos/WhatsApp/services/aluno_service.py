from data.persistencia_csv import PersistenciaCSV
# Importar outras persistências conforme necessário

class AlunoService:
    def __init__(self, tipo_persistencia='csv'):
        if tipo_persistencia == 'csv':
            self.persistencia = PersistenciaCSV()
        # Adicione outros tipos de persistência, como PDF, XML, MySQL, etc.

    def salvar_aluno(self, aluno):
        if isinstance(aluno, list):  # Verifica se é uma lista de alunos
            for a in aluno:
                self.persistencia.salvar_aluno(a)  # Salva cada aluno na lista
        else:
            self.persistencia.salvar_aluno(aluno)  # Salva o único aluno

    def buscar_alunos(self):
        return self.persistencia.buscar_alunos()
