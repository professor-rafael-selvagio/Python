import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())  # Avalia a expressão matemática
        entrada.delete(0, tk.END)  # Limpa a entrada
        entrada.insert(0, str(resultado))  # Exibe o resultado
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("800x600")

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 30), width=64)
# Coloca a entrada na primeira linha
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  

# Lista de botões
botoes = [
    ('1', 1), ('2', 2), ('3', 3), ('+', '+'),
    ('4', 4), ('5', 5), ('6', 6), ('-', '-'),
    ('7', 7), ('8', 8), ('9', 9), ('*', '*'),
    ('C', 'C'), ('0', 0), ('=', '='), ('/', '/')
]

# Adiciona os botões na grade
linha = 1
coluna = 0
for (texto, valor) in botoes:
    if texto == 'C':
        btn = tk.Button(janela, text=texto, command=lambda: entrada.delete(0, tk.END), font=("Arial", 28), width=4)
    elif texto == '=':
        btn = tk.Button(janela, text=texto, command=calcular, font=("Arial", 28), width=4)
    else:
        btn = tk.Button(janela, text=texto, command=lambda t=texto: entrada.insert(tk.END, t), font=("Arial", 28), width=4)
    
    # Adiciona o botão à grade
    btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")  # Posiciona o botão

    # Atualiza a coluna e linha para o próximo botão
    coluna += 1
    if coluna > 3:  # Se exceder 4 colunas, muda para a próxima linha
        coluna = 0
        linha += 1

# Configura o redimensionamento da grade
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
    
for i in range(5):  # 5 linhas para garantir espaço para o campo de entrada
    janela.grid_rowconfigure(i, weight=1)

# Inicia o loop principal
janela.mainloop()
