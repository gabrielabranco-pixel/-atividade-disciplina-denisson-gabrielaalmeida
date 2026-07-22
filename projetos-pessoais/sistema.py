import tkinter as tk 

janela = tk.Tk()

janela.title("Sistema de Cadastro de Usuários")#o Título da janela 
janela.geometry("900x600")#tamanho da janela

#Criar o elemento
#Texto de introdução
titulo = tk.Label(janela, text="Meu App de Cadastro")
#posicionar o elemento na janela
titulo.pack(pady=(10, 100))#pady é o espaçamento entre o elemento e o topo da janela, nesse caso 10px e 100px do topo do elemento para o próximo elemento 
janela.mainloop()

titulo =tk.Label (text="Bem-vindo(a)!")
tiulo.pack(pady=(10, 100))