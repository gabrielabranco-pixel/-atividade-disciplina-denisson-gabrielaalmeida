import tkinter as tk 
from tkinter.font import Font 

janela = tk.Tk()

janela.title("Sistema de Cadastro de Usuários")#o Título da janela 
janela.geometry("900x600")#tamanho da janela

#Criar o elemento
#Texto de introdução
titulo = tk.Label(janela, text="Meu App de Cadastro", font=Font(size=22, weight="bold", familly="Arial"))
#posicionar o elemento na janela
titulo.pack(pady=(20, 20))#pady é o espaçamento entre o elemento e o topo da janela, nesse caso 10px e 100px do topo do elemento para o próximo elemento 


titulo =tk.Label (text="Bem-vindo(a)!", font=("Arial", 16))
titulo.pack(pady=(20, 20))
janela.mainloop()

#ESSE CÓDIGO FOI CRIADO PARA TESTAR A INTERFACE ANTIGA DO TKINTER 

#------------------------------------------------------------------------------------------

#CLASSE ORIENTADA A OBJETOS EM PYTHON OOP

#Uma classe é um modelo que serve para criar objetos para não ter de criar códigos do zero 
#quando estivermos iniciando algo novo, nos usamos as classes para organizar e reaproveitar 
#código 

#IMAGINE 
#uma classe = a uma planta de uma casa com ela podemos construir várias outras
# casa (objetos) com o mesmo designe

#PARA QUE SERVE?
# 1. Organizar o código
# 2. reutilização da lógica
# 3.representação de entidades do mundo real
# 4. facilidade de manutenção e escalabilidade 

#COMPONETES DE UMA CLASSE SÃO:

# 1. CLASS = palavra-chave para definir uma classe
# 2. __init__ = metodo especial chamado para criar o objeto, ele também serve
# para inicializar dados
# 3. Self = é uma referência ao próprio objeto criado(obrigatório nos metódos da classe)
# 4. Atributos = são váriaveis que pertecem ao objeto 
# 5. Métodos = são funções definidas dentro da classe 

#COMO CRIAR E USAR OBJETOS DENTRO DE UMA CLASSE?

# Os atributos são características podendo ser: nome, idade e cor....
# Métodos são comportamentos podendo ser: falar, correr e calcular....
#Existe também os modificadores de acesso como: private ou public (usamos no java)
#porém usamos convenções.
#Dessa forma:
#nome - público
#_nome - protégido 
# __nome - privado 

#Metódos especiais como:

#__init__ = inicializador(construtor)
#__str__ = define como objeto sendo representado como string 
#__repr__ = é uma representação para debug 


# HERANÇA EM CLASSES: 
# 1. Uma classe pode herdar de outra para reaproveitar o código dessa forma 
# 2. Já no encapsulamento ele oculta detalhes internos para proteger os dados



