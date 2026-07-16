import tkinter as tk

# 1. Instanciar a janela principal
janela = tk.Tk()
janela.title("Sucesso!")
janela.geometry("300x200")

# 2. Adicionar um widget (ex: Rótulo)
texto = tk.Label(janela, text="Olá, mundo!")
texto.pack(pady=50)

# 3. Rodar a aplicação
janela.mainloop()
