senha_correta = "12345"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite sua senha: ")
    tentativas += 1
    
    if senha == senha_correta:
        print("Login bem-sucedido!")
        break  # Interrompe o loop se o login for bem-sucedido
else:
    print("Conta bloqueada. Número máximo de tentativas excedido.")
