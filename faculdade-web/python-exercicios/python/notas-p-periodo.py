#funções = são blocos de código reutilizaveis 
#para invocar uma função coloca um conjunto de parentes apos o nome da função 
#place () after the function name to invoke it

#Se eu quisesse cantar parabens 3 vezes seria necessario colar esse codigo 3 vezes ou coloca - lo em um loop de repetição

#print("Happy Birthday to you!")
#print("You're are old")
#print("Happy Birthday to you!")
#print()

#A função serve para escrever esse codigo uma vez e reutiliza - lo sempre que necessário 

#def happy_birthday(): #//nome da funcao
   # print("Happy Birthday to you!")
   # print("You're are old")
   # print("Happy Birthday to you!")
   # print()

#happy_birthday() #//invoca o nome da funcao
#para invoca-la 3 vezes é necessário chamar a funcao 3 vezes

#É possivel enviar valores e variaveis a funcao 
#enviar dados diretamente na funcao - chamamos isso de argumentos // coloque quaisquer dados dentro de um conjunto de parenteses

#def happy_birthday(name): #//adicionarei um parametro nome a minha funcao de feliz aniversario
    #um paramtro é como uma variavel temporaria usada na funcao 

   # print(f"Happy Birthday to {name}!")
   # print("You're are old")
   # print("Happy Birthday to you!")
   # print()

#happy_birthday("Bro") #o dado que esta sendo enviado aqui é um nome 
#happy_birthday("Steve") 
#happy_birthday("Joe") 

# ao invocar uma funcao voce pode enviar mais de um argumento 

#def happy_birthday(name, age): 

   # print(f"Happy Birthday to {name}!")
   # print(f"You're are {age} years old")
   # print("Happy Birthday to you!")
   # print()

#happy_birthday("Bro",20)
#happy_birthday("Steve",30) 
#happy_birthday("Joe",40) 

#Também é possivel nomear os paramentros com algo unico


#def happy_birthday(x, y): 

   # print(f"Happy Birthday to {x}!")
   # print(f"You're are {y} years old")
   # print("Happy Birthday to you!")
   # print()

#happy_birthday("Bro",20)
#happy_birthday("Steve",30) 
#happy_birthday("Joe",40) 

#AGORA VAMOS CRIAR UMA FUNCAO PARA EXIBIR UMA FATURA 

#def display_invoice(username, amount, due_date):
   # print(f"Hello {username}")
   # print(f"Your bill of ${amount:.2f} is due: {due_date}")

#display_invoice("BroCode", 40.45, "01/03/2005")

#INSTRUÇAO RETURN 

#return = é usada para encerrar uma funcao e enviar um resultado de volta para quem a chamou

#def add(x, y):
   # z = x + y 
   # return z


#def subtract(x, y):
   # z = x - y 
   # return z


#def multiply(x, y):
   # z = x * y 
   # return z


#def divide(x, y):
  #  z = x / y 
   # return z

#print(add(1,2))
#print(subtract(1,2))
#print(multiply(1,2))
#print(divide(1,2))

#VAMOS CRIAR UMA FUNCAO PARA FORMAR UM NOME COMPLETO:

'''
def create_name(first, last):
    #agora colocamos o que queremos fazer dentro dessa funcao
    first = first.capitalize() #usamos o metodo .capitalize que transforma a primeira letra do nome em maiscula 
    last = last.capitalize()
    return first + "" + last

full_name = create_name("bro", "code")
print(full_name)
'''

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
def validar_nome(nome):
    if nome != "":
        return True
    return False

def validar_data(data):
    if "/" in data:
        return True
    return False

def validar_email(email):
    if "@" in email:
        return True
    return False

usuarios = []

while True:

    nome = input("Digite o nome: ")

    if not validar_nome(nome):
        print("Nome inválido!")
        continue

    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

    if not validar_data(data):
        print("Data inválida!")
        continue

    email = input("Digite o email: ")

    if not validar_email(email):
        print("Email inválido!")
        continue

    usuario = [nome, data, email]
    usuarios.append(usuario)

    print("Usuário cadastrado!")

    continuar = input("Deseja cadastrar outro usuário? (s/n): ")

    if continuar.lower() == "n":
        break

print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(usuario)
'''

'''
def validar_data(dia, mes, ano):
    if dia < 1 or dia > 31:
        return False

    if mes < 1 or mes > 12:
        return False

    if ano < 1900 or ano > 2024:
        return False

    return True

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if not validar_data(dia, mes, ano):
    print("Data inválida!")
    continue
Opção 3 (a mais correta)

A melhor forma é usar o módulo datetime, porque ele verifica datas reais. Assim, datas como 31/02/2024 serão rejeitadas.

from datetime import datetime

def validar_data(dia, mes, ano):
    try:
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

Então:

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if not validar_data(dia, mes, ano):
    print("Data inválida!")
    continue

Essa última abordagem também detecta casos como:

❌ 31/02/2024
❌ 30/02/2023
❌ 31/04/2025
✅ 29/02/2024 (ano bissexto)

Ela é a mais recomendada para um sistema de cadastro.

A melhor forma é usar o módulo datetime, porque ele verifica datas reais. Assim, datas como 31/02/2024 serão rejeitadas.

from datetime import datetime

def validar_data(dia, mes, ano):
    try:
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

Então:

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if not validar_data(dia, mes, ano):
    print("Data inválida!")
    continue

Essa última abordagem também detecta casos como:

❌ 31/02/2024
❌ 30/02/2023
❌ 31/04/2025
✅ 29/02/2024 (ano bissexto)

Ela é a mais recomendada para um sistema de cadastro.

'''

'''
def validar_nome(nome):
    if len(nome) < 1 or len(nome) > 4:
        return True
    else:
        return False
    
def validar_dia(dia):
 if dia < 1 or dia > 31:
        return True 
 else:
        return False
 
def validar_mes(mes):
    if mes <1 or mes > 11:
        return True
    else:
        return False

def validar_ano(ano):
    if ano <1900 or ano > 2024:
         return True
    else:
         return False
'''                                                 

'''
def validar_nome(nome):
    if len(nome) < 1 or len(nome) > 4:
        return True
    else:
        return False
    
cad_usuario =[]

while True:   

   nome = input("Digite seu nome: ")
   if not validar_nome(nome):
      print("Nome incorreto")
      continue
   
   dia = int(input("Digite o dia do seu nascimento:"))
   if dia < 1 or dia > 31:
       print ("Dia invalido!, apenas dias entre 1 e 31: ")
   
   mes = int(input("Digite o mês do seu nascimento:"))
   if mes < 1 or mes > 12:
       print ("Mês invalido!, o anos tem apenas 12 meses: ")

   ano = int(input("Digite o ano do seu nascimento:"))
   if ano < 1900 or ano > 2026:
       print("Ano invalido!, tente novamente: ")


   if not(dia,mes,ano):
       print("Data invalida!")
       continue
   


   dia =int(input("Digite o dia do seu nascimento:" )) 
   if dia < 1 or dia > 31: 
     print ("Digite novamente!, agora entre dia 1 e 31.") 
     continue 
   mes = int(input("Digite o mês do seu nascimento:")) 
   if mes < 1 or mes > 12:
        print("Mês incorreto!, tente digitar entre o mês 1 e 12.")
        continue 
   ano = int(input("Digite o ano do seu nascimento: ")) 
   if ano < 1900 or ano > 2024: 
    print("Ano invalido!, apenas múmias podem acessar essa data") 
    continue
'''

'''
   email = input("Digite seu email(nome@dominio.com): ")

   nome_email = input("Digite o nome do seu email: ")
   if len (nome_email) <5:
       print("Email invalido!")
   dominio_email = input("Digite o dominio do seu email: ")
   if "@" not in email:
    print("Email inválido!")

   if not email(email):
      print("Email incorreto")
      continue
'''
'''
n = 5
for i in range(6):
    for j in range(7):
        if (i==0 or j % 3 != 0 )or \
              (i == 1 and j % 3 == 0) or \
              ( i - j == 2) or \
              (i + j == 8):
            print("*", end="")
        else:
            print("", end="")
    print()
'''

def nome_completo (nome, sobrenome): 
    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()
    return nome + " " + sobrenome 

#return f"{nome} {sobrenome}" // forma mais moderna 

nome = input("Digite seu nome:")
sobrenome = input("Digite seu sobrenome:")

print(nome_completo(nome, sobrenome))


