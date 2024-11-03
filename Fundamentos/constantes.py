
# Exemplo de "Constantes" em Python

# Em Python, não existe uma palavra-chave específica para declarar constantes.
# Por convenção, variáveis que devem ser tratadas como constantes são escritas em letras maiúsculas.
# Essas variáveis podem ser modificadas, então cabe ao programador manter a convenção e evitar alterar esses valores.

# Exemplo de constantes:
PI = 3.14159
GRAVIDADE = 9.81

print("Constante PI:", PI)
print("Constante GRAVIDADE:", GRAVIDADE)

# Demonstrando que constantes podem ser alteradas (embora não seja recomendado)
PI = 3.1416  # Alterando o valor de PI
GRAVIDADE = 9.81  # Alterando o valor de GRAVIDADE

print("Constante PI (alterada):", PI)
print("Constante GRAVIDADE (alterada):", GRAVIDADE)
print("Observação: Em Python, o valor das 'constantes' pode ser alterado, pois o comportamento de imutabilidade não é forçado.")