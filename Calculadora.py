import tkinter as tk
import re  # adicionei isso para usar expressões regulares


# Função para inserir números e operadores no display
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(botao))

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))

        # Adiciona ao histórico
        historico.insert(tk.END, f"{expressao} = {resultado}")
        # Rola automaticamente para o final
        historico.yview(tk.END)

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

def limpar_historico():
    historico.delete(0, tk.END)

def porcentagem():
    expressao = entrada.get()

    try:
        # Encontra a última operação (ex: "200 + 50")
        operadores = re.split(r'([\+\-\*/])', expressao)
        
        if len(operadores) >= 3:
            anterior = eval(''.join(operadores[:-2]))  # ex: 200
            operador = operadores[-2]                  # ex: +
            atual = float(operadores[-1])              # ex: 50

            resultado = anterior + (anterior * atual / 100) if operador == '+' else \
                       anterior - (anterior * atual / 100) if operador == '-' else \
                       anterior * (atual / 100) if operador == '*' else \
                       anterior / (atual / 100)

            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        else:
            # Se tiver só um número, converte direto para porcentagem
            resultado = float(expressao) / 100
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))

    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg="#1e1e1e")

# Tela de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Área de histórico (lista de resultados)
historico = tk.Listbox(janela, height=5, font=("Arial", 14), bg="#1e1e1e", fg="white", bd=0)
historico.grid(row=1, column=0, columnspan=4, sticky="we", padx=10, pady=(0,10))

#Todo os botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), # Lista com os botões da calculadora, suas posições na grade e funções associadas.

    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("←", 5, 1), ("(", 5, 2), (")", 5, 3),
    ("%", 6, 0), ("HistC", 6, 1)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        comando = calcular
    elif texto == "C":
        comando = limpar
    elif texto == "←":
        comando = apagar
    elif texto == "%":
        comando = porcentagem
    elif texto == "HistC":
        comando = limpar_historico
    else:
        comando = lambda t=texto: clicar(t)
    
    tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 16), command=comando, bg="#2d2d2d", fg="white").grid(row=linha, column=coluna, padx=5, pady=5)

# Ajustar coluna "C" para ocupar mais espaço
janela.grid_columnconfigure(0, weight=1)

# Iniciar a interface
janela.mainloop()