import tkinter as tk
import re  # adicionei isso para usar expressões regulares
import math

# Variável de controle do tema
modo_escuro = True

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

def alternar_tema():
    global modo_escuro

    # Alterna o valor da flag
    modo_escuro = not modo_escuro

    # Define os temas
    bg_cor = "#1e1e1e" if modo_escuro else "#f0f0f0"
    fg_cor = "white" if modo_escuro else "black"
    botao_bg = "#2d2d2d" if modo_escuro else "#dcdcdc"

    # Atualiza fundo da janela
    janela.config(bg=bg_cor)
    frame_topo.config(bg=bg_cor)
    frame_historico.config(bg=bg_cor)
    frame_botoes.config(bg=bg_cor)

    # Atualiza entrada
    entrada.config(bg="white" if not modo_escuro else "white", fg="black", insertbackground="black")

    # Atualiza histórico
    historico.config(bg=bg_cor, fg=fg_cor)

    # Atualiza botões
    for widget in frame_botoes.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(bg=botao_bg, fg=fg_cor)

    # Atualiza botão de tema
    botao_tema.config(bg=botao_bg, fg=fg_cor)

def raiz_quadrada():
    try:
        expressao = entrada.get()
        valor = eval(expressao)
        resultado = math.sqrt(valor)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))

        # Adiciona ao histórico
        historico.insert(tk.END, f"√({expressao}) = {resultado}")
        historico.yview(tk.END)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Responsiva")
janela.geometry("400x500")
janela.config(bg="#1e1e1e")

# Frames
frame_topo = tk.Frame(janela, bg="#1e1e1e")
frame_topo.pack(fill="x", padx=10, pady=(10, 5))

frame_historico = tk.Frame(janela, bg="#1e1e1e")
frame_historico.pack(fill="x", padx=10, pady=(0, 10))

frame_botoes = tk.Frame(janela, bg="#1e1e1e")
frame_botoes.pack(expand=True, fill="both", padx=10, pady=10)

# Tela de entrada
entrada = tk.Entry(frame_topo, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
entrada.pack(fill="x")

# Histórico
historico = tk.Listbox(frame_historico, height=5, font=("Arial", 14), bg="#1e1e1e", fg="white", bd=0)
historico.pack(fill="x")

# Botão para alternar tema
botao_tema = tk.Button(frame_historico, text="Modo Claro/Escuro", font=("Arial", 12),
                       command=alternar_tema, bg="#2d2d2d", fg="white")
botao_tema.pack(pady=5)

# Grade de botões
botoes = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
    ("C", 4, 0), ("←", 4, 1), ("(", 4, 2), (")", 4, 3),
    ("%", 5, 0), ("HistC", 5, 1), ("√", 5, 3)

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
    elif texto == "√":
        comando = raiz_quadrada
    else:
        comando = lambda t=texto: clicar(t)

    btn = tk.Button(frame_botoes, text=texto, font=("Arial", 16), command=comando,
                    bg="#2d2d2d", fg="white", relief=tk.RAISED)
    btn.grid(row=linha, column=coluna, sticky="nsew", padx=3, pady=3)

# Tornar colunas e linhas expansíveis
for i in range(6):
    frame_botoes.rowconfigure(i, weight=1)
for j in range(4):
    frame_botoes.columnconfigure(j, weight=1)

# Iniciar a interface
janela.mainloop()