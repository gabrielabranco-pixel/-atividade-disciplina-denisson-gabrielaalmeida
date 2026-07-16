
#while True:
   # print("isso nunca para")
   # break


#x=0
#while x <= 10:
     #   print(x)
       # x = x+1


#contador = 1
#while contador <= 5: #ele chega até o 6 para execultar
       # print(f"Valor: {contador}")
      #  contador += 1


#continuar = True
#while continuar:
       # resposta = input("Deseja continuar? (s/n)")
        #if resposta.lower() == "n":
         #continuar = False


#for variavel in sequencia
#execute


#for i in range(5):
#    print(i)


#arrayNumeros = [10, 11, 13, 20, 27] #ficam guardados na memoria Ram
#for numero in arrayNumeros:
    #print(numero)


#arraynomes = ["Gabi","Abilen","Jessica","Isabella"]
#for elemento in arraynomes:
  #  print(elemento)


#CRUD - creat,read,update,delete


#manipular com range
#metodos de CRUD para array


# ARRAYS
#nao guardamos eles em um banco de dados, ele só vai ser guardado na memoria RAM quando esse código for rodado
#frutas = ['maça', 'banana']


#print(frutas)


# como adicionar dados
#frutas.append('uva')


#print(frutas)


#bala = ['morango', 'chocolate']


#print(bala)


#bala.append('chocomenta')


#print(bala)


#carrinho = []
#valorDigitado = input("Digite o item")
#carrinho.append(valorDigitado)
#print(carrinho)


#nomes = []
#valorDigitado = input('digite o nome:')
#nomes.append(valorDigitado)
#print(nomes)


#nome = []
#valorDigitado = input('Digite o nome:')
#nome.append (valorDigitado)
#continuar = True
#while continuar:
 #   resposta = input("Deseja continuar? (s/n)")
#    valorDigitado = input('digite o nome:')
#    nome.append (valorDigitado)
 #   if resposta.lower() == "n":
 #     print(nome)
#      continuar = False
 


#listaPessoas = []

#continuar = 's'
#while continuar == 's':
   # nomePessoas = input ('Digite o nome da pessoa:')
   # listaPessoas.insert(0, nomePessoas)
   # continuar = input('Deseja adicionar outra pessoa? (s/n):')
   # excluirPessoa= input('Deseja excluir alguém da lista? (s/n)')
   # if excluirPessoa == 's':
       # nomeExcluir = input ('Digite o nome da pessoa excluida:')
       # if nomeExcluir in listaPessoas:
           # listaPessoas.remove(nomeExcluir)
           # print(f'{nomeExcluir} foi removido da lista.')
       # else:
          #  print(f'{nomeExcluir} não encontrado na lista.')
#print('lista de pessoas:', listaPessoas)

#.insert ( inserir dados na lista)
#.append (inserir dados na lista)
#.remove ( remove algo da lista)
#.pop (erve para remover um elemento de uma estrutura de dados (como listas ou dicionários) e, ao mesmo tempo, retornar o valor removido para que você possa utilizá-lo em outra parte do seu código)
#.clear (refere-se a duas funções principais: limpar o terminal enquanto o programa roda ou esvaziar uma lista/dicionári)

#EXERCICIO 1: 
#inserir um novo convidado ao inicio da lista
#remover o ultimo convidado da lista
#utilizar o .pop para remover 

#Convidados = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

#continuar = 's'
#while continuar == 's':
  #  continuar = input('Deseja adicionar outra pessoa? (s/n):')
   # nome = input ('Digite o nome da pessoa:')
  #  Convidados.insert(0, nome)
   # print(f'{Convidados} nome adicionado na lista com sucesso!')

   # excluirPessoas= input ('Deseja ecluir alguém da lista? (s/n)')
    #if excluirPessoa == 's':
    # if excluirPessoa in Convidados:   
     # item = Convidados.pop()
  #  print(f'{Convidados}, pessoa removida com sucesso!')
#else:   
 
 #print(f'{Convidados}')

#Convidados = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

#continuar = 's'
#while continuar == 's':
   # continuar = input('Deseja adicionar outra pessoa? (s/n):')
   # nome = input ('Digite o nome da pessoa:')
   # Convidados.insert(0, nome)
   # print(f'{Convidados} nome adicionado na lista com sucesso!')

#excluirPessoa = input('Deseja excluir alguém da lista? (s/n): ')

#if excluirPessoa == 's':

   # item = Convidados.pop()

   # print(f'{item} foi removido com sucesso!')

#print(f'{Convidados}')

#USANDO O CLEAR 
#Convidados = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

#continuar = 's'
#while continuar == 's':
   # continuar = input('Deseja adicionar outra pessoa? (s/n):')
   # nome = input ('Digite o nome da pessoa:')
   # Convidados.insert(0, nome)
   # print(f'{Convidados} nome adicionado na lista com sucesso!')

#excluirPessoa = input('Deseja excluir alguém da lista? (s/n): ')

#if excluirPessoa == 's':

   # item = Convidados.clear()

#print(f'{Convidados}')

#Desenvolva um programa que:

#Exiba a lista de tarefas atual.

#Adicione uma nova tarefa no final da lista (use append). O nome da tarefa deve ser digitado pelo usuário.

#Adicione uma tarefa urgente no início da lista (posição 0) usando insert. O nome também será digitado pelo usuário.

#Remova a última tarefa da lista com pop e mostre qual tarefa foi removida.

#Pergunte ao usuário qual tarefa ele já concluiu (pelo nome) e remova-a com remove. Se o nome não existir, mostre uma mensagem informando.

#Ao final, exiba a lista resultante.

#artistas = ['Michelangelo','Leo DVinci','Rafael', 'Donatello' ]
#print(f'{artistas}')

#novo_artistas= input('Adicione mais um artista:')
#artistas.append(novo_artistas)
#print(f'{artistas}')

#melhor_artista= input('Adicione o melhor artista:')
#artistas.insert(0,melhor_artista)
#print(f'{artistas}')

#item= artistas.pop()
#print(f'{item} o artista foi removido com sucesso!')
#print('------------------------------------------------------------------------------')
#concluida = input('Qual artista você já leu a  biografia?')
#if concluida in artistas:
  #  artistas.remove(concluida)
  #  print(f'"{concluida}"foi removido da lista.') 
#else:
 # print(f'"{concluida}" ops!não existe esse artista')
#print('-------------------------------------------------------------------------------')

#print ('\nlista de artistas:')
#print(artistas)

#carros = []

#while True:
   # inputNomeCarro = input ("Digite o nome do carro:")
    #carros.append (inputNomeCarro)
   # resposta = input ("Deseja adicionar outro carro? (s/n):")
    #if resposta.lower() == 'n':
        # break
    #addCarro = input("deseja editar o nome do carro? (s/n):")
   # if addCarro.lower() =='n':
     #   break
    #else:
      # novoNomeCarro = input ("Digite o novo nome do carro:")  
      # indiceCarro = int(input("Digite o indice do carro a ser editado:"))
      # carros[indiceCarro] = novoNomeCarro
#print ("lista de carros:", carros)     
    
#for index, carro in enumerate(carros):
    #se o que usuario digitar for igual a carro
    #entao ele vai editar o nome carro
    # se nao for igual ele vai adicionar o nome do carro
    #Use o codigo para rodar com o for
 #   print(f"Carro: {index}: {carro}")


#carros = ["Gol", "Ford", "Ferrari", "Fusca"]

#print(carros)

#nome= input("Digite o nome do carro que deseja editar:")

#if nome in carros:
       # indice = carros.index(nome) #encontra a posicao do carro
       # novo_nome = input ("Digite o novo nome do carro:")
       # carros[indice] = novo_nome

       # print("Lista atualizada:")
           # print(f"{i}-{carro}")

#for i, carro in enumerate(carros):
  #  print(f"{i} - {carro}")

#indice = int(input("Digite o índice do carro que deseja editar: "))
#novo_nome = input("Digite o novo nome: ")

#carros[indice] = novo_nome

#print(carros)

#else:
         #   print("Carro não encontrado!")    

#for index, carro in enumerate (carros):
   # inputNome = input('Digite o nome do carro:')
    #if inputNome == carro: 
    #  novoNome = input('Digite o novo nome do carro:')
    #  carros(f'Carro{index}: {carros}')
'''
def ola_aluno (nome):
    print(f'olá, {nome}!')

ola_aluno("Lucas")
ola_aluno("Maria")

def soma (primeiroNumero, segundoNumero):
   resultado = primeiroNumero + segundoNumero 
   return resultado 

print(soma(5,3)) #chama a funcao imprimi o resultado 
'''
#def calculo_desc (valor_total_prod, taxa_desconto):
#   desconto = valor_total_prod * ( taxa_desconto / 100 )
#   return valor_total_prod - desconto 
 
#chamar funcao e imprimir resultado 

#EXERCICIO 1
#VALOR_SAPATO = 150
#Criar print: calcule o valor do desconto 
#perguntar o valor do deconto ao o usuario 
#entao o valor do produto vai ser fixo 
#chamar a funcao e imprimir resulto 
#o valor do sapato com desconto é:

'''
VALOR_SAPATO = 150 
print("Seu sapato custa: $", VALOR_SAPATO)
print("-----------------------------------------------------")
print("Calcule o desconto!!!")
print("---------------------------------------------------")
taxa_desconto = float(input("Digite a taxa de desconto (em %): "))
valor_com_desconto = calculo_desconto (VALOR_SAPATO, taxa_desconto) 
print(f" valor do sapato com o desconto é: R$ {valor_com_desconto:.2f}") 
'''

#EXERCICIO 2
#perguntar o valor do produto 
#perguntar a taxa de desconto o resultado do valor com o desconto 

'''
print("----------------------------------------------")
print("Calcule o valor do desconto")
print("----------------------------------------------")

valor_sapato =(input("Qual o valor do sapato?"))
taxa_desconto = float(input("Digite a taxa de desconto (em %): "))
valor_com_desconto = calculo_desconto (valor_sapato, taxa_desconto) 
print(f" valor do sapato com o desconto é: R$ {valor_com_desconto:.2f}") 
'''

#EXERCICIO 3
#CHAMAR A FUNCAO DE AUTENTICACAO 
#PASSANDO VALORES ERRADOS
#PASSANDO VALORES CORRETOS 

''''
def auth_user( user: str, token: int ) -> bool: 
#simulação de autenticacao (apenas o exemplo) 

   USUARIO_CORRETO = "admin"
   TOKEN_CORRETO = 1234
   if user == USUARIO_CORRETO and token == TOKEN_CORRETO:
     return True 
   else:
      return False
   
# Chamando a função com valores errados
resultado1 = auth_user("joao", 1111)
print("Autenticação com dados errados:", resultado1)

# Chamando a função com usuário correto e token errado
resultado2 = auth_user("admin", 9999)
print("Usuário correto e token errado:", resultado2)

# Chamando a função com valores corretos
resultado3 = auth_user("admin", 1234)
print("Autenticação com dados corretos:", resultado3)

'''

#EXERCICIO PARA CASA
# crie uma funcao que valide o nome do usuario
# crie uma funcao que valide a data de nascimento do usuario (dd/mm/aaaa)
# crie uma funcao que valide o email do usuario (nome@dominio.com)

#crie um cadastro de usuario em uma lista para 
# armazenar nome, data de nascimento e email do usuario

# COMPLEMENTO - Crie um loop para adicionar varios usuarios na lista.

'''
cad_usuario = {
    
    'nome' : input("Digite seu nome:"),
    'data_nascimento' : input("Digite sua data de nascimento(dd/mm/aaaa):"), 
    'email' : input("Digite seu email(nome@dominio.com):"),
}

print('\n Cadastro de usuarios: ')

for chaves in sorted(cad_usuario.keys()):
   print(f'{chaves} : {cad_usuario[chaves]}')

'''
'''
print("--------------------------------------------------")
print("---------------------Cadastre-se aqui!------------")
print("--------------------------------------------------")

def validar_nome(nome):
    if nome != "":
        return True
    else:
        return False

def validar_data(data):
    if data != "/":
        return True 
    else: 
        return False

def validar_email(email):
    if email != "@":
        return True
    else:
        return False
      
cad_usuario = []

while True:   

   nome = input("Digite seu nome: ")
   if not validar_nome(nome):
      print("Nome incorreto")
      continue
               
   data_nascimento = input("Digite sua data de nascimento(dd/mm/aaaa): ")
   if not validar_data(data_nascimento):
      print("Data incorreta")
      continue
               
   email = input("Digite seu email(nome@dominio.com): ")
   if not validar_email(email):
      print("Email incorreto")
      continue
      
   usuario = [nome,data_nascimento,email]
   usuario.append(cad_usuario)
   print("---------------Usuário cadatrado!-------------------")

   continuar = input("Deseja cadastrar mais usuarios? (s/n): ").lower()

   if continuar != 's':
      break

   print("\n ------------Cadastro de usuario------------------")
   for i, usuario_atual in enumerate(usuario, start = 1):     
            print(f"Usuário{i} : {usuario_atual}")

   print("-----------------------------------------------------------")
'''

# entregar via email para jorgelucasalima@gmail.com as 22:00 de 26/06

   # EXERCICIO PARA CASA
# 1. crie uma funcao que valide o nome do usuario
# 1.1 na funcao validar_nome verificar se está acima acima ou igual a 3 caracteres
# 2. crie uma funcao que valide a data de nascimento do usuario (dd/mm/aaaa)
# 2.1 na funcao validar_data verificar se o dia está entre 1 e 31, 
# o mes entre 1 e 12 e o ano entre 1900 e 2024
# 3.crie uma funcao que valide o email do usuario (nome@dominio.com)
# 3.1 tudo que estiver antes do @ verificar se tem 5 caracteres

# AGORA: crie um cadastro de usuario em uma lista para 
# armazenar nome, data de nascimento e email do usuario

# COMPLEMENTO - Crie um loop para adicionar varios usuarios na lista.

print("--------------------------------------------------")
print("---------------------Cadastre-se aqui!------------")
print("--------------------------------------------------")

def validar_nome(nome):
    if len(nome) < 1 or len(nome) > 4:
        return True
    else:
        return False

def validar_email(email):
    if "@" not in email:
        return False

    if "." not in email:
        return False

    if len(email) < 5:
        return False

    return True


cad_usuario =[]

while True:   

   nome = input("Digite seu nome: ")
   if not validar_nome(nome):
      print("Nome incorreto")
      continue

    
   dia = int(input("Digite o dia do seu nascimento:"))
   if dia < 1 or dia > 31:
       print ("Dia invalido!, apenas dias entre 1 e 31 ")
   
   mes = int(input("Digite o mês do seu nascimento:"))
   if mes < 1 or mes > 12:
       print ("Mês invalido!, o anos tem apenas 12 meses ")

   ano = int(input("Digite o ano do seu nascimento:"))
   if ano < 1900 or ano > 2026:
       print("Ano invalido!, tente novamente ")

   if not(dia,mes,ano):
       print("Data invalida!")
       continue
   
   email = input("Digite seu e-mail (nome@dominio.com): ")
   if not validar_email(email):
    print("E-mail incorreto!")
    continue

   usuario = [nome,dia,mes,ano,email]
   usuario.append(cad_usuario)
   print("---------------Usuário cadatrado!-------------------")

   continuar = input("Deseja cadastrar mais usuarios? (s/n): ").lower()

   if continuar != 's':
      break

   print("\n ------------Cadastro de usuario------------------")
   for i, usuario_atual in enumerate(usuario, start = 1):     
            print(f"Usuário{i} : {usuario_atual}")

   print("-----------------------------------------------------------")
   print("-----------------------------------------------------------")