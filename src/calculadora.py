import tkinter as tk
import re
import math
import os
from PIL import Image, ImageTk

# Variável de controle do tema
modo_escuro = True # Começa no modo escuro por padrão

# Variáveis globais para as imagens Tkinter
imagem_sol_tk = None
imagem_lua_tk = None

# Variável global para a memória da calculadora
memoria_valor = 0.0

# Variável global para o modo atual da calculadora
modo_calculadora_atual = "Científica" # Começa no modo Científica por padrão

# --- FUNÇÕES DA CALCULADORA ---
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(botao))

def calcular():
    try:
        expressao = entrada.get()
        if not expressao or expressao.strip() in "+-*/%":
            entrada.insert(0, "Erro")
            return
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        historico.config(state=tk.NORMAL)
        historico.insert(tk.END, f"{expressao} = {resultado}\n")
        historico.config(state=tk.DISABLED)
        historico.see(tk.END)
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)

def apagar():
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual[:-1])

def limpar_historico():
    historico.config(state=tk.NORMAL)
    historico.delete(1.0, tk.END)
    historico.config(state=tk.DISABLED)

def porcentagem():
    expressao = entrada.get()
    try:
        if not expressao: entrada.insert(0, "Erro"); return
        operadores = re.split(r"([\+\-\*/])", expressao)
        if len(operadores) >= 3:
            anterior = eval("".join(operadores[:-2]))
            operador = operadores[-2]
            atual = float(operadores[-1])
            if operador == "+": resultado = anterior + (anterior * atual / 100)
            elif operador == "-": resultado = anterior - (anterior * atual / 100)
            elif operador == "*": resultado = anterior * (atual / 100)
            elif operador == "/": resultado = anterior / (atual / 100)
            else: raise ValueError("Operador inválido")
            entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
        else:
            resultado = float(expressao) / 100
            entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, tk.END); entrada.insert(0, "Erro %")

# --- FUNÇÕES CIENTÍFICAS ---
def elevar_ao_quadrado():
    try:
        valor_str = entrada.get()
        if not valor_str: entrada.insert(0, "Erro"); return
        valor = float(valor_str)
        resultado = math.pow(valor, 2)
        entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
        historico.config(state=tk.NORMAL)
        historico.insert(tk.END, f"{valor_str}² = {resultado}\n")
        historico.config(state=tk.DISABLED); historico.see(tk.END)
    except Exception:
        entrada.delete(0, tk.END); entrada.insert(0, "Erro x²")

def elevar_ao_cubo():
    try:
        valor_str = entrada.get()
        if not valor_str: entrada.insert(0, "Erro"); return
        valor = float(valor_str)
        resultado = math.pow(valor, 3)
        entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
        historico.config(state=tk.NORMAL)
        historico.insert(tk.END, f"{valor_str}³ = {resultado}\n")
        historico.config(state=tk.DISABLED); historico.see(tk.END)
    except Exception:
        entrada.delete(0, tk.END); entrada.insert(0, "Erro x³")

def logaritmo_base10():
    try:
        valor_str = entrada.get()
        if not valor_str: entrada.insert(0, "Erro"); return
        valor = float(valor_str)
        if valor <= 0: entrada.delete(0, tk.END); entrada.insert(0, "Erro log"); return
        resultado = math.log10(valor)
        entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
        historico.config(state=tk.NORMAL)
        historico.insert(tk.END, f"log({valor_str}) = {resultado}\n")
        historico.config(state=tk.DISABLED); historico.see(tk.END)
    except Exception:
        entrada.delete(0, tk.END); entrada.insert(0, "Erro log")

def logaritmo_natural():
    try:
        valor_str = entrada.get()
        if not valor_str: entrada.insert(0, "Erro"); return
        valor = float(valor_str)
        if valor <= 0: entrada.delete(0, tk.END); entrada.insert(0, "Erro ln"); return
        resultado = math.log(valor)
        entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
        historico.config(state=tk.NORMAL)
        historico.insert(tk.END, f"ln({valor_str}) = {resultado}\n")
        historico.config(state=tk.DISABLED); historico.see(tk.END)
    except Exception:
        entrada.delete(0, tk.END); entrada.insert(0, "Erro ln")

# --- FUNÇÕES DE MEMÓRIA ---
def memoria_clear(): # MC
    global memoria_valor
    memoria_valor = 0.0

def memoria_recall(): # MR
    global memoria_valor
    entrada.delete(0, tk.END)
    entrada.insert(0, str(memoria_valor))

def memoria_adicionar(): # M+
    global memoria_valor
    try:
        valor_display = float(entrada.get())
        memoria_valor += valor_display
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro M+")

def memoria_subtrair(): # M-
    global memoria_valor
    try:
        valor_display = float(entrada.get())
        memoria_valor -= valor_display
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro M-")

def alternar_tema():
    global modo_escuro, imagem_sol_tk, imagem_lua_tk, label_imagem_tema_no_historico, janela, frame_topo, frame_modos, frame_botao_tema_container, frame_historico_e_imagem, frame_botoes, entrada, historico, botao_tema, botao_modo_padrao, botao_modo_cientifica

    modo_escuro = not modo_escuro

    bg_cor = "#1e1e1e" if modo_escuro else "#f0f0f0"
    fg_cor = "white" if modo_escuro else "black"
    botao_bg = "#2d2d2d" if modo_escuro else "#e0e0e0"
    botao_fg = "white" if modo_escuro else "black"
    entrada_bg = "#333333" if modo_escuro else "white"
    text_hist_bg = "#252525" if modo_escuro else "#e8e8e8"
    hist_container_bg = text_hist_bg

    janela.config(bg=bg_cor)
    frame_topo.config(bg=bg_cor)
    frame_modos.config(bg=bg_cor)
    frame_botao_tema_container.config(bg=bg_cor)
    frame_historico_e_imagem.config(bg=hist_container_bg)
    frame_botoes.config(bg=bg_cor)

    entrada.config(bg=entrada_bg, fg=fg_cor, insertbackground=fg_cor, relief=tk.FLAT, bd=5)
    historico.config(bg=text_hist_bg, fg=fg_cor, relief=tk.FLAT, bd=0)
    
    # Estilizar botões de modo
    botao_modo_padrao.config(bg=botao_bg, fg=botao_fg, activebackground=fg_cor, activeforeground=botao_bg)
    botao_modo_cientifica.config(bg=botao_bg, fg=botao_fg, activebackground=fg_cor, activeforeground=botao_bg)
    atualizar_destaque_botao_modo() # Destaca o botão do modo ativo

    # Estilizar botões de operação (que estão em frame_botoes)
    for widget in frame_botoes.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(bg=botao_bg, fg=botao_fg, activebackground=fg_cor, activeforeground=botao_bg, relief=tk.RAISED, bd=2)
    
    if botao_tema: 
        botao_tema.config(bg=botao_bg, fg=botao_fg, activebackground=fg_cor, activeforeground=botao_bg, relief=tk.RAISED, bd=1)
    
    if label_imagem_tema_no_historico:
        current_image = None
        if modo_escuro:
            if imagem_lua_tk: current_image = imagem_lua_tk
        else:
            if imagem_sol_tk: current_image = imagem_sol_tk
        
        label_imagem_tema_no_historico.config(image=current_image, bg=hist_container_bg)
        if current_image: label_imagem_tema_no_historico.image = current_image
        else: label_imagem_tema_no_historico.image = None

def raiz_quadrada():
    try:
        expressao = entrada.get()
        if not expressao: entrada.insert(0, "Erro"); return
        valor = float(expressao)
        resultado = math.sqrt(valor)
        entrada.delete(0, tk.END); entrada.insert(0, str(resultado))
        historico.config(state=tk.NORMAL)
        historico.insert(tk.END, f"√({expressao}) = {resultado}\n")
        historico.config(state=tk.DISABLED); historico.see(tk.END)
    except Exception:
        entrada.delete(0, tk.END); entrada.insert(0, "Erro √")

def tecla_pressionada(event):
    tecla = event.char
    if tecla.isdigit() or tecla in ".+-*/()": clicar(tecla)
    elif event.keysym == "Return" or tecla == "=": calcular()
    elif event.keysym == "BackSpace": apagar()
    elif tecla.lower() == "c": limpar()

# --- FUNÇÃO PARA MUDAR MODO E ATUALIZAR BOTÕES ---
def configurar_botoes_para_modo(modo):
    global frame_botoes, modo_calculadora_atual
    modo_calculadora_atual = modo

    # Limpar botões existentes em frame_botoes
    for widget in frame_botoes.winfo_children():
        widget.destroy()

    botoes_config_modo = []
    num_linhas_modo = 0

    if modo == "Padrão":
        janela.title("DragonCalculadora Padrão")
        num_linhas_modo = 7
        botoes_config_modo = [
            ("MC", 0, 0, 1, 1, memoria_clear), ("MR", 0, 1, 1, 1, memoria_recall), ("M-", 0, 2, 1, 1, memoria_subtrair), ("M+", 0, 3, 1, 1, memoria_adicionar),
            ("C", 1, 0, 1, 1, limpar), ("HistC", 1, 1, 1, 1, limpar_historico), ("%", 1, 2, 1, 1, porcentagem), ("/", 1, 3, 1, 1, lambda: clicar("/")),
            ("7", 2, 0, 1, 1, lambda: clicar("7")), ("8", 2, 1, 1, 1, lambda: clicar("8")), ("9", 2, 2, 1, 1, lambda: clicar("9")), ("*", 2, 3, 1, 1, lambda: clicar("*")),
            ("4", 3, 0, 1, 1, lambda: clicar("4")), ("5", 3, 1, 1, 1, lambda: clicar("5")), ("6", 3, 2, 1, 1, lambda: clicar("6")), ("-", 3, 3, 1, 1, lambda: clicar("-")),
            ("1", 4, 0, 1, 1, lambda: clicar("1")), ("2", 4, 1, 1, 1, lambda: clicar("2")), ("3", 4, 2, 1, 1, lambda: clicar("3")), ("+", 4, 3, 1, 1, lambda: clicar("+")),
            ("0", 5, 0, 1, 2, lambda: clicar("0")), (".", 5, 2, 1, 1, lambda: clicar(".")), ("=", 5, 3, 1, 1, calcular),
            ("(", 6, 0, 1, 1, lambda: clicar("(")), (")", 6, 1, 1, 1, lambda: clicar(")")), ("√", 6, 2, 1, 1, raiz_quadrada), ("←", 6, 3, 1, 1, apagar)
        ]
    elif modo == "Científica":
        janela.title("DragonCalculadora Científica")
        num_linhas_modo = 8
        botoes_config_modo = [
            ("MC", 0, 0, 1, 1, memoria_clear), ("MR", 0, 1, 1, 1, memoria_recall), ("M-", 0, 2, 1, 1, memoria_subtrair), ("M+", 0, 3, 1, 1, memoria_adicionar),
            ("x²", 1, 0, 1, 1, elevar_ao_quadrado), ("x³", 1, 1, 1, 1, elevar_ao_cubo), ("log", 1, 2, 1, 1, logaritmo_base10), ("ln", 1, 3, 1, 1, logaritmo_natural),
            ("C", 2, 0, 1, 1, limpar), ("HistC", 2, 1, 1, 1, limpar_historico), ("%", 2, 2, 1, 1, porcentagem), ("/", 2, 3, 1, 1, lambda: clicar("/")),
            ("7", 3, 0, 1, 1, lambda: clicar("7")), ("8", 3, 1, 1, 1, lambda: clicar("8")), ("9", 3, 2, 1, 1, lambda: clicar("9")), ("*", 3, 3, 1, 1, lambda: clicar("*")),
            ("4", 4, 0, 1, 1, lambda: clicar("4")), ("5", 4, 1, 1, 1, lambda: clicar("5")), ("6", 4, 2, 1, 1, lambda: clicar("6")), ("-", 4, 3, 1, 1, lambda: clicar("-")),
            ("1", 5, 0, 1, 1, lambda: clicar("1")), ("2", 5, 1, 1, 1, lambda: clicar("2")), ("3", 5, 2, 1, 1, lambda: clicar("3")), ("+", 5, 3, 1, 1, lambda: clicar("+")),
            ("0", 6, 0, 1, 2, lambda: clicar("0")), (".", 6, 2, 1, 1, lambda: clicar(".")), ("=", 6, 3, 1, 1, calcular),
            ("(", 7, 0, 1, 1, lambda: clicar("(")), (")", 7, 1, 1, 1, lambda: clicar(")")), ("√", 7, 2, 1, 1, raiz_quadrada), ("←", 7, 3, 1, 1, apagar)
        ]

    for i in range(num_linhas_modo): frame_botoes.rowconfigure(i, weight=1)
    for j in range(4): frame_botoes.columnconfigure(j, weight=1)

    FONT_BOTOES_MEM_CIEN = ("Arial", 13, "normal")
    FONT_BOTOES_PADRAO = ("Arial", 15, "normal")
    FONT_BOTOES_OPERADORES = ("Arial", 15, "bold")

    for (texto, linha, coluna, rspan, cspan, comando) in botoes_config_modo:
        font_usada = FONT_BOTOES_PADRAO
        if (modo == "Científica" and (linha == 0 or linha == 1)) or (modo == "Padrão" and linha == 0) : # Botões de memória e científicos
             font_usada = FONT_BOTOES_MEM_CIEN
        elif texto in "=/*-+":
            font_usada = FONT_BOTOES_OPERADORES
            
        btn = tk.Button(frame_botoes, text=texto, font=font_usada, command=comando, padx=8, pady=4)
        btn.grid(row=linha, column=coluna, rowspan=rspan, columnspan=cspan, sticky="nsew", padx=1, pady=1)
    
    alternar_tema() # Reaplicar tema aos novos botões
    alternar_tema() # Chamar duas vezes para garantir o estado correto do modo_escuro
    atualizar_destaque_botao_modo()

def atualizar_destaque_botao_modo():
    global botao_modo_padrao, botao_modo_cientifica, modo_calculadora_atual, modo_escuro
    
    cor_ativa_fg = "#1e1e1e" if modo_escuro else "#f0f0f0" # Inverte com o fundo do botão
    cor_ativa_bg = "white" if modo_escuro else "black"
    cor_inativa_fg = "white" if modo_escuro else "black"
    cor_inativa_bg = "#2d2d2d" if modo_escuro else "#e0e0e0"

    if modo_calculadora_atual == "Padrão":
        botao_modo_padrao.config(relief=tk.SUNKEN, bg=cor_ativa_bg, fg=cor_ativa_fg)
        botao_modo_cientifica.config(relief=tk.RAISED, bg=cor_inativa_bg, fg=cor_inativa_fg)
    elif modo_calculadora_atual == "Científica":
        botao_modo_padrao.config(relief=tk.RAISED, bg=cor_inativa_bg, fg=cor_inativa_fg)
        botao_modo_cientifica.config(relief=tk.SUNKEN, bg=cor_ativa_bg, fg=cor_ativa_fg)

# --- CONFIGURAÇÃO DA JANELA E WIDGETS ---
janela = tk.Tk()
janela.geometry("380x780") # Altura aumentada para botões de modo
janela.minsize(370, 750)

# --- CARREGAMENTO DE IMAGENS ---
IMAGE_TARGET_SIZE = (48, 48)
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path_img_sol = os.path.join(script_dir, "..", "sol.png")
    path_img_lua = os.path.join(script_dir, "..", "lua.png")

    if os.path.exists(path_img_sol):
        img_sol_pil = Image.open(path_img_sol)
        img_sol_pil.thumbnail(IMAGE_TARGET_SIZE, Image.Resampling.LANCZOS)
        imagem_sol_tk = ImageTk.PhotoImage(img_sol_pil)
    else: print(f"AVISO: Imagem sol não encontrada em 	'{path_img_sol}'.")

    if os.path.exists(path_img_lua):
        img_lua_pil = Image.open(path_img_lua)
        img_lua_pil.thumbnail(IMAGE_TARGET_SIZE, Image.Resampling.LANCZOS)
        imagem_lua_tk = ImageTk.PhotoImage(img_lua_pil)
    else: print(f"AVISO: Imagem lua não encontrada em 	'{path_img_lua}'.")
except Exception as e:
    print(f"Ocorreu um erro ao carregar as imagens: {e}")

# --- LAYOUT DOS FRAMES PRINCIPAIS ---
PADX_FRAMES = 10

frame_topo = tk.Frame(janela)
frame_topo.pack(fill="x", padx=PADX_FRAMES, pady=(10,5))

# Frame para seleção de modo
frame_modos = tk.Frame(janela)
frame_modos.pack(fill="x", padx=PADX_FRAMES, pady=5)

frame_botao_tema_container = tk.Frame(janela)
frame_botao_tema_container.pack(fill="x", padx=PADX_FRAMES, pady=5)

frame_historico_e_imagem = tk.Frame(janela, height=120)
frame_historico_e_imagem.pack(fill="x", padx=PADX_FRAMES, pady=5)

frame_botoes = tk.Frame(janela) # Este frame será preenchido dinamicamente
frame_botoes.pack(expand=True, fill="both", padx=PADX_FRAMES, pady=(5,10))

# --- ELEMENTOS DO frame_topo ---
entrada = tk.Entry(frame_topo, font=("Arial", 28), justify="right")
entrada.pack(side=tk.LEFT, expand=True, fill="x", ipady=10)

# --- ELEMENTOS DO frame_modos ---
botao_modo_padrao = tk.Button(frame_modos, text="Padrão", font=("Arial", 10), command=lambda: configurar_botoes_para_modo("Padrão"), width=10)
botao_modo_padrao.pack(side=tk.LEFT, padx=5, pady=2)
botao_modo_cientifica = tk.Button(frame_modos, text="Científica", font=("Arial", 10), command=lambda: configurar_botoes_para_modo("Científica"), width=10)
botao_modo_cientifica.pack(side=tk.LEFT, padx=5, pady=2)

# --- ELEMENTOS DO frame_botao_tema_container ---
botao_tema = tk.Button(frame_botao_tema_container, text="Alternar Tema", font=("Arial", 10), command=alternar_tema, width=15, height=1)
botao_tema.pack(pady=2)

# --- ELEMENTOS DO frame_historico_e_imagem ---
label_imagem_tema_no_historico = tk.Label(frame_historico_e_imagem)
label_imagem_tema_no_historico.place(relx=1.0, rely=0.0, x=-5, y=5, anchor='ne')

historico = tk.Text(frame_historico_e_imagem, height=5, font=("Arial", 12), wrap=tk.WORD)
historico.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, IMAGE_TARGET_SIZE[0] + 10))
historico.config(state=tk.DISABLED)

# --- BINDINGS E CHAMADA INICIAL DO MODO E TEMA ---
janela.bind('<Key>', tecla_pressionada)
janela.bind('<Return>', lambda event: calcular())
janela.bind('<BackSpace>', lambda event: apagar())

configurar_botoes_para_modo(modo_calculadora_atual) # Configura botões para o modo inicial
# alternar_tema() # Aplicar tema inicial (já é chamado dentro de configurar_botoes_para_modo)

janela.mainloop()