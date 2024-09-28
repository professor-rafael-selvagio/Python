# Definindo a classe Cachorro
class Cachorro:
    # Método construtor que inicializa nome e idade
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

    # Método que faz o cachorro latir
    def latir(self):
        print(f"{self.nome} está latindo!")

    # Método que retorna as informações do cachorro
    def info(self):
        return f"O cachorro {self.nome} tem {self.idade} anos."
