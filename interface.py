import customtkinter as ctk
from codigo_principal import processar_financas

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Divida Segura")
        self.geometry("450x500")

        # Título da Interface
        self.label_titulo = ctk.CTkLabel(self, text="Divida Segura", font=("Roboto", 28, "bold"))
        self.label_titulo.pack(pady=30)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=30, fill="both", expand=True)

        # Entrada de Dívidas
        self.lbl_div = ctk.CTkLabel(self.frame, text="Valores de Dívidas (use +):", font=("Roboto", 14))
        self.lbl_div.pack(pady=(20, 0))
        self.entry_dividas = ctk.CTkEntry(self.frame, width=300, placeholder_text="Ex: 150.50 + 200")
        self.entry_dividas.pack(pady=10)

        # Entrada de Ganhos
        self.lbl_gan = ctk.CTkLabel(self.frame, text="Valores de Ganhos (use +):", font=("Roboto", 14))
        self.lbl_gan.pack(pady=(10, 0))
        self.entry_ganhos = ctk.CTkEntry(self.frame, width=300, placeholder_text="Ex: 3000 + 500")
        self.entry_ganhos.pack(pady=10)

        # Botão de Calcular
        self.btn = ctk.CTkButton(self.frame, text="CALCULAR", font=("Roboto", 16, "bold"), command=self.calcular)
        self.btn.pack(pady=30)

        # Resultado
        self.res_label = ctk.CTkLabel(self.frame, text="", font=("Roboto", 16, "bold"), wraplength=350)
        self.res_label.pack(pady=10)

    def calcular(self):
        d = self.entry_dividas.get()
        g = self.entry_ganhos.get()
        
        if d and g:
            try:
                # Chama a sua função do arquivo codigo_principal.py
                v_div, v_gan, saldo = processar_financas(d, g)
                
                if saldo >= 0:
                    msg = f"Você pode gastar nesse mês até:\nR$ {saldo:.2f}"
                    cor = "#2ecc71" # Verde
                else:
                    msg = f"O recomendado é juntar mais e gastar menos!\nSaldo: R$ {saldo:.2f}"
                    cor = "#e74c3c" # Vermelho
                
                self.res_label.configure(text=msg, text_color=cor)
            except Exception as e:
                self.res_label.configure(text="Erro: Verifique os valores digitados!", text_color="orange")

if __name__ == "__main__":
    app = App()
    app.mainloop()