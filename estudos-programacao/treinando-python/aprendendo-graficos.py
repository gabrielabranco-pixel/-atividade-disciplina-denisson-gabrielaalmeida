'''
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
'''

'''
import tkinter as tk #Caso eu queira usar a biblioteca para criar uma janela personalizada usarei apenas essa função + o loop
# Essa janela é uma box de mensagem que aparece na tela, com um título e uma mensagem 
from tkinter import messagebox, simpledialog, filedialog

#root = tk.Tk()

'''

'''
#EXIBIR MENSAGEM:
Para exibir essa subferramenta da tkbox so preciso chamar a messagebox

import tkinter as tk
from tinkinter import messagebox 

#messagebox.showinfo("Título da Janela", "Mensagem de Sucesso!")
#messagebox.showinfo("Sucesso!", "Sua operação foi realizada com sucesso!")

#mensagem de texto/avisos 
#messagebox.showwarning("Aviso!", "Esta é uma mensagem de aviso.")

#mensagem de erro 
#messagebox.showerror("Erro!", "Ocorreu um erro durante a operação.")

'''

'''

#PEGAR INFORMAÇÕES DO USUÁRIO:
import tkinter as tk #Caso eu queira usar a biblioteca para criar uma janela personalizada usarei apenas essa função + o loop
# Essa janela é uma box de mensagem que aparece na tela, com um título e uma mensagem 
from tkinter import messagebox, simpledialog

nome = simpledialog.askstring("Identificação", "Qual é o seu nome?")
#O simpledialog.askstring() é uma função que cria uma caiza de dialogo para o usuário digitar um nome 
# existe também o askinteger() e o askfloat() para números inteiros e decimais 

if nome:
    print(f"Olá {nome}, ! Seja bem-vindo(a)!")

'''

'''
#PEGAR UM ARQUIVO:
#cria uma automção, por exemplo: desejo pegar um lista de clientes

#arquivo = filedialog.askopenfilename()
#filedialog.askopenfilename() é uma função que cria uma caiza de dialogo para o usuário selecionar um aquivo do computador

#print(arquivo) #irá imprimir o caminho do arqivo selecionado, caso a pessoa não slecione nenhum arquivo, ele ira imprimir uma string vazia.


lista_de_arquivos = filedialog.askopenfilenames(
    title="Selecione os arquivos",#define o título da janela de seleção de arquivos e dá uma orientação ao usuário sobre o que ele deve fazer
    filetypes=[("Arquivos de Texto", "*.txt"),
                ("Todos os Arquivos", "*.*")],
    #o filetypes é uma lista de tuplas que define/limita os tipos de arquivos que o usuário pode selecionar
    # o "*.txt" é um coringa que significa "qualquer arquivo com a extensão .txt"

)   
#O filedialog.askopenfilenames() para selecionar varios arquivos(lista_de_arquivos) e etc...

print(lista_de_arquivos)

'''

