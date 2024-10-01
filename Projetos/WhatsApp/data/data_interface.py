from abc import ABC, abstractmethod

class DataInterface(ABC):
    
    @abstractmethod
    def salvar_aluno(self, aluno):
        pass

    @abstractmethod
    def buscar_alunos(self):
        pass
