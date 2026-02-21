import tkinter as tk
from codigo_principal import processar_financas # Importa seu arquivo original

def acao_calcular():
    # Coleta o que o usuário digitou na interface
    d = entry_dividas.get()
    g = entry_ganhos.get()
    
    # Executa a sua lógica e pega os resultados
    res_div, res_gan, res_mensal = processar_financas(d, g)
    
    # Exibe os resultados na janela do Front-end
    lbl_status.config(text=f"Total Dívidas: R$ {res_div:.2f}\nTotal Ganhos: R$ {res_gan:.2f}")
    
    if res_mensal >= 0:
        lbl_final.config(text=f"você pode gastar nesse mês até R$ {res_mensal:.2f}", fg="green")
    else:
        lbl_final.config(text=f"o recomendado é juntar mais e gastar menos pois o valor é R$ {res_mensal:.2f}", fg="red")

# --- Estrutura da Janela ---
app = tk.Tk()
app.title("Sistema Financeiro")
app.geometry("400x350")

# Textos idênticos aos seus inputs para o usuário saber o que digitar
tk.Label(app, text="coloque todos os valores de dividas\n(use + para somar):").pack(pady=10)
entry_dividas = tk.Entry(app, width=30)
entry_dividas.pack()

tk.Label(app, text="coloque todos os valores de ganhos\n(use + para somar):").pack(pady=10)
entry_ganhos = tk.Entry(app, width=30)
entry_ganhos.pack()

tk.Button(app, text="Calcular", command=acao_calcular).pack(pady=20)

lbl_status = tk.Label(app, text="")
lbl_status.pack()

lbl_final = tk.Label(app, text="", font=("Arial", 10, "bold"), wraplength=350)
lbl_final.pack(pady=10)