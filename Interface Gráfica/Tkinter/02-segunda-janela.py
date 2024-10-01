import tkinter as tk
from tkinter import messagebox

def mostrar_saudacao():
    # Obtém o nome inserido pelo usuário
    nome = entrada_nome.get()  
    if nome:
        # Exibe uma mensagem de saudação
        messagebox.showinfo("Saudação", f"Olá, {nome}!")  
    else:
        # Aviso caso o nome não seja inserido
        messagebox.showwarning("Atenção", "Por favor, insira seu nome!")  

# Cria a janela principal
janela = tk.Tk()
janela.title("Aplicativo de Saudação")
janela.geometry("400x300")  # Define o tamanho da janela

# Cria um rótulo
rotulo = tk.Label(janela, text="Insira seu nome:", font=("Arial", 14))
rotulo.pack(pady=10)  # Adiciona o rótulo à janela

# Cria um campo de entrada
entrada_nome = tk.Entry(janela, font=("Arial", 14))
entrada_nome.pack(pady=10)  # Adiciona o campo de entrada à janela

# Cria um botão
botao = tk.Button(janela, text="Saudar", command=mostrar_saudacao, font=("Arial", 14))
botao.pack(pady=20)  # Adiciona o botão à janela

# Inicia o loop principal
janela.mainloop()
