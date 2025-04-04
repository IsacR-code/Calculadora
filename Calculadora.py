import tkinter as tk

# Função que realiza o cálculo
def calcular(operador):
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        
        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = "Erro: divisão por zero"
        else:
            resultado = "Operação inválida"
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Digite números válidos.")

# Criação da janela
janela = tk.Tk()
janela.title("Calculadora Simples")

# Entradas de número
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Botões de operação
tk.Button(janela, text="+", width=5, command=lambda: calcular("+")).grid(row=2, column=0)
tk.Button(janela, text="-", width=5, command=lambda: calcular("-")).grid(row=2, column=1)
tk.Button(janela, text="*", width=5, command=lambda: calcular("*")).grid(row=3, column=0)
tk.Button(janela, text="/", width=5, command=lambda: calcular("/")).grid(row=3, column=1)

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

# Inicia o loop da janela
janela.mainloop()