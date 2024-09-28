import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Meu Aplicativo Tkinter")
janela.geometry("400x300")  # Define o tamanho da janela

# Cria um rótulo
rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.pack(pady=10)  # Adiciona o rótulo à janela

# Cria um botão
botao = tk.Button(janela, text="Clique aqui", command=janela.quit)
botao.pack(pady=10)  # Adiciona o botão à janela

# Inicia o loop principal
janela.mainloop()
