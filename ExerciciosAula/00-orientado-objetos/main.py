from click import clear
clear()

# Importando a classe Cachorro do arquivo cachorro.py
from cachorro import Cachorro

# Criando uma instância da classe Cachorro
meu_cachorro1 = Cachorro("Rex", 5)
meu_cachorro2 = Cachorro("Dog", 7)

# Chamando o método latir
meu_cachorro1.latir()  # Saída: Rex está latindo!
meu_cachorro2.latir()  # Saída: Dog está latindo!

# Chamando o método info e imprimindo as informações
print(meu_cachorro1.info())  # Saída: O cachorro Rex tem 5 anos.
print(meu_cachorro2.info())  # Saída: O cachorro Rex tem 5 anos.
