# Importa o modulo tk
import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
# Define o titulo da janela
janela.title("Meu Aplicativo Tkinter")
# Define o tamanho da janela
janela.geometry("400x300")  

# Cria um rótulo
rotulo = tk.Label(janela, text="Olá, Tkinter!")
# Adiciona o rótulo à janela
rotulo.pack(pady=10)  

# Cria um botão, define o texto do botão e define a ação do botão (quit = sair)
botao = tk.Button(janela, text="Clique aqui", command=janela.quit)
# Adiciona o botão à janela
botao.pack(pady=10)  

# Inicia o loop principal
janela.mainloop()
