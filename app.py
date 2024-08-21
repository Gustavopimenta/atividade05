import tkinter as tk
from tkinter import messagebox, scrolledtext
from swiplserver import PrologMQI, PrologThread

# Função para realizar a consulta à base de conhecimento
def consultar_prolog(query):
    try:
        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog_thread:
                # Carregar a base de conhecimento
                prolog_thread.query("consult('knowledge_base.pl')")
                # Realizar a consulta
                result = prolog_thread.query(query)
                return result
    except Exception as e:
        return f"Erro: {e}"

# Função para exibir a resposta na interface
def buscar_resposta():
    consulta = entry.get()
    if not consulta.strip():
        messagebox.showwarning("Entrada Inválida", "Por favor, digite uma consulta válida.")
        return

    resposta = consultar_prolog(consulta)
    if isinstance(resposta, str) and resposta.startswith("Erro"):
        result_text = resposta
    elif resposta:
        result_text = "\n".join([str(res) for res in resposta])
    else:
        result_text = "Nenhuma resposta encontrada."
    
    result_display.config(state=tk.NORMAL)
    result_display.delete(1.0, tk.END)
    result_display.insert(tk.END, result_text)
    result_display.config(state=tk.DISABLED)

# Função para limpar a entrada e a saída
def limpar():
    entry.delete(0, tk.END)
    result_display.config(state=tk.NORMAL)
    result_display.delete(1.0, tk.END)
    result_display.config(state=tk.DISABLED)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Consulta Prolog")

# Título e Instruções
tk.Label(root, text="Consulta Prolog", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Digite sua consulta abaixo e clique em 'Buscar':", font=("Arial", 12)).grid(row=1, column=0, columnspan=2, pady=5)

# Campo de entrada para a consulta
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.grid(row=2, column=0, padx=10, pady=5)

# Botão para realizar a consulta
button = tk.Button(root, text="Buscar", font=("Arial", 12), command=buscar_resposta)
button.grid(row=2, column=1, padx=10, pady=5)

# Campo de texto para exibir a resposta com scrollbar
result_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=10, width=70, wrap=tk.WORD, font=("Arial", 12))
result_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Botão para limpar
clear_button = tk.Button(root, text="Limpar", font=("Arial", 12), command=limpar)
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar a aplicação
root.mainloop()

# Regras Prolog explicadas:

# 1. Regra: mortal(X) :- human(X).
#    Significado: "X é mortal se X for humano."
#    Essa regra define que todo humano é mortal. Se algo (X) é considerado humano,
#    então automaticamente é considerado mortal.

# 2. Regra: ancestor(X, Y) :- parent(X, Y).
#    Significado: "X é ancestral de Y se X for pai/mãe de Y."
#    Esta regra define a relação direta de ancestralidade. Se X é pai ou mãe de Y,
#    então X é um ancestral de Y.

# 3. Regra: ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
#    Significado: "X é ancestral de Y se X for pai/mãe de Z e Z for ancestral de Y."
#    Esta regra é recursiva e define que X é ancestral de Y não apenas se X for pai/mãe de Y,
#    mas também se X for pai/mãe de alguém (Z) que, por sua vez, é ancestral de Y.
#    Isso permite a identificação de ancestrais como avós, bisavós, etc.

"""
Este código Python implementa uma interface gráfica utilizando Tkinter para realizar consultas a uma base de conhecimento Prolog.

Principais componentes do código:

1. Importações:
   - `tkinter`: Biblioteca padrão do Python para criar interfaces gráficas (GUIs).
   - `messagebox` e `scrolledtext`: Componentes específicos de Tkinter usados para exibir mensagens e criar caixas de texto com barra de rolagem.
   - `swiplserver`: Utilizada para estabelecer uma conexão com o servidor Prolog, permitindo consultas à base de conhecimento.

2. Função `consultar_prolog(query)`:
   - Esta função é responsável por abrir uma sessão com o Prolog, carregar a base de conhecimento (`knowledge_base.pl`), e executar a consulta fornecida pelo usuário.
   - Em caso de erro, uma mensagem de erro é retornada.

3. Função `buscar_resposta()`:
   - Coleta a entrada do usuário e realiza a consulta utilizando a função `consultar_prolog`.
   - A resposta da consulta é formatada e exibida na interface.
   - A função também lida com entradas inválidas e exibe uma mensagem de alerta apropriada.

4. Função `limpar()`:
   - Limpa tanto o campo de entrada quanto a área de exibição da resposta, permitindo que o usuário inicie uma nova consulta.

5. Configuração da Interface Gráfica:
   - O layout da interface é organizado em uma grade com labels, campos de entrada, botões e um campo de texto com barra de rolagem para exibir as respostas.
   - A interface é simples e intuitiva, facilitando o uso para consultas em Prolog.

6. `root.mainloop()`:
   - Inicia o loop principal da aplicação Tkinter, mantendo a interface aberta e responsiva para o usuário.

Este código é útil para integrar consultas Prolog dentro de uma aplicação Python com uma interface gráfica, facilitando o uso de lógica Prolog em um ambiente interativo e acessível.
"""

