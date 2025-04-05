import tkinter as tk

# Função para inserir números e operadores no display
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(botao))

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para limpar o display
def limpar():
    entrada.delete(0, tk.END)

def apagar():
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual[:-1])  # remove o último caractere

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Bonita")
janela.config(bg="#1e1e1e")

# Tela de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Todo os botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("←", 5, 1), ("(", 5, 2), (")", 5, 3)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        comando = calcular
    elif texto == "C":
        comando = limpar
    elif texto == "←":
        comando = apagar
    else:
        comando = lambda t=texto: clicar(t)
    
    tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 16), command=comando, bg="#2d2d2d", fg="white").grid(row=linha, column=coluna, padx=5, pady=5)

# Ajustar coluna "C" para ocupar mais espaço
janela.grid_columnconfigure(0, weight=1)

# Iniciar a interface
janela.mainloop()