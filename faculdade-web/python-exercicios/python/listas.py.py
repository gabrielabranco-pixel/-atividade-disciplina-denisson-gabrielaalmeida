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

artistas = ['Michelangelo','Leo DVinci','Rafael', 'Donatello' ]
print(f'{artistas}')

novo_artistas= input('Adicione mais um artista:')
artistas.append(novo_artistas)
print(f'{artistas}')

melhor_artista= input('Adicione o melhor artista:')
artistas.insert(0,melhor_artista)
print(f'{artistas}')

item= artistas.pop()
print(f'{item} o artista foi removido com sucesso!')
print('------------------------------------------------------------------------------')
concluida = input('Qual artista você já leu a  biografia?')
if concluida in artistas:
    artistas.remove(concluida)
    print(f'{artistas} foi removido da lista.') 
else:
  print(f'{concluida} ops!não existe esse artista')
  artistas  = artistas + concluida
  print(concluida)



