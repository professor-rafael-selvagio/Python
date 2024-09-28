import os

pasta = os.getcwd()
print(pasta) # Saída: caminho do atual diretório


arquivos_e_pastas = os.listdir(pasta)
for item in arquivos_e_pastas:
    #print(f"Arquivo ou Pasta -> {item}")


    # Verificar se o item é um arquivo ou pasta
    if os.path.isfile(pasta + "/" + item):
        print(f"Arquivo -> {item}")
    elif os.path.isdir(pasta + "/" + item):
        print(f"Pasta   -> {item}")