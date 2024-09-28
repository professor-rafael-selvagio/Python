import tkinter as tk

def iniciar():
    global rodando
    rodando = True
    atualizar()

def pausar():
    global rodando
    rodando = False

def resetar():
    global tempo
    tempo = 0
    label_tempo.config(text="00:00:00")

def atualizar():
    if rodando:
        global tempo
        tempo += 1
        horas = tempo // 3600
        minutos = (tempo % 3600) // 60
        segundos = tempo % 60
        label_tempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        janela.after(1000, atualizar)  # Atualiza a cada 1 segundo

tempo = 0
rodando = False

janela = tk.Tk()
janela.title("Cronômetro")

label_tempo = tk.Label(janela, text="00:00:00", font=("Arial", 48))
label_tempo.pack(pady=20)

botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar)
botao_iniciar.pack(side=tk.LEFT, padx=10)

botao_pausar = tk.Button(janela, text="Pausar", command=pausar)
botao_pausar.pack(side=tk.LEFT, padx=10)

botao_resetar = tk.Button(janela, text="Resetar", command=resetar)
botao_resetar.pack(side=tk.LEFT, padx=10)

janela.mainloop()
