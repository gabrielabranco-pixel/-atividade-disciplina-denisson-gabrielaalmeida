import customtkinter as ctk
import time

ctk.set_appearance_mode("Dark") #Dark, System, Light
ctk.set_default_color_theme("blue") # blue, green, dark-blue

#janela = ctk.CTk() #já é uma classe do python

class Aplicativo(ctk.CTk): #criamos uma cópia da classe ctk por isso colocamos ela entre parenteses "subclasse" - ela vai importar todas as funcionalidades
    def __init__(self): #função init 
         super().__init__() 
         #ele execulta os meus códigos personalizados.
         self.title("Sistema de cadastro de clientes")
         self.geometry("900x600")
        
#----------------------------------------------------------------------
        
        #grid.system = um sistema de linhas e colunas 
        #configuramos o peso de cada coisa
        #criar divisão da tela, weight = 1 -> expande junto com a tela 
        #a coluna que tiver peso igual a zero - não expande junto a tela
        
 #-------------------------------------------------------------------

        #Configurações do Gridy
         self.grid_columnconfigure(1, weight= 1)#coluna da direita
         self.grid_rowconfigure(0, weight = 1)#coluna da esquerda 
 #-------------------------------------------------------------------

        #Um frame - é fixo 
        #Tabview - tem várias abas

#----------------------------------------------------------------------
        #parte lateral 
        
         self.barra_lateral = ctk.CTkFrame(self, width=200)
         self.barra_lateral.grid(row=0, column=0, sticky="ns")
         #frame expande a barra esquerda
#-----------------------------------------------------------------------
         #parte principal

         self.janela_abas = ctk.CTkTabview(self)
         self.janela_abas.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
         #o sticky -  é a parte interna direcionada para norte, sul, leste e oeste 
         #TabView expande barra direita  

         self.janela_abas.add("Perfil")
         self.janela_abas.add("Preferências")
         self.janela_abas.add("Dashboard")    
#-----------------------------------------------------------------------

        #preencher minhas partes/abas
        #preencher aba lateral
         self.construir_tela()
        #preencher aba perfil
         self.construir_abaperfil()
        #preencher aba preferências 
         self.construir_abapreferencias()
        #preencher aba sistema 
         self.construir_abasistema()

#-----------------------------------------------------------------------

    def construir_tela(self):
        self.titulo = ctk.CTkLabel(self.barra_lateral, 
                                   text = "Meu App",
                                   font = ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=(30, 5), padx=(20, 20))

        self.subtitulo = ctk.CTkLabel(self.barra_lateral, 
                                   text = "" ) # elemento vazio
        self.subtitulo.pack(pady=(0, 5))

        self.botao_principal = ctk.CTkButton(self.barra_lateral,
                                             text= ("Dashboard Principal"), 
                                             command= self.ir_para_dashboard)
        self.botao_principal.pack(pady=(30, 30),padx=(10, 10) )

        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral,
                                            text="Modo Escuro",
                                            command=self.mudar_modo_dark)
        self.switch_mododark.pack(pady=(10, 10), side="bottom")
        self.switch_mododark.select()
#-------------------------------------------------------------------------
#COMPARTILHANDO VARIÁVEIS 

#Se eu construir essas variáveis inicializando com self.algumacoisa
# dentro da minha função -> def 
#eu posso utilizar essas váriáveis em qualquer outra função def do meu código.

#CONFIGURANDO AS VÁRIAVEIS 

# 1. indicar onde a variável vai ser localizada 
# (nas abas?/ na área do app?) - ele pede o master dentro da variável
# master = mestre dele 

# 2. 
#-------------------------------------------------------------------------
    def construir_abaperfil(self):
     self.aba_perfil = self.janela_abas.tab("Perfil")
            #campo de nome
     self.campo_nome = ctk.CTkEntry(self.aba_perfil, 
                        placeholder_text="Digite o seu nome",
                        width=300 )
     
     self.campo_nome.pack(pady=(20, 20))
            #radio buttom do nível de usuário
     self.nivel_usuario = ctk.IntVar(value=0)
     self.radio_label = ctk.CTkLabel(self.aba_perfil, text="Nível de Usuário")
     self.radio_basico = ctk.CTkRadioButton(self.aba_perfil,
                                            text="Básico",
                                            variable=self.nivel_usuario,
                                            value = 1 )
     self.radio_admin = ctk.CTkRadioButton(self.aba_perfil, 
                                              text="Admin",
                                              variable=self.nivel_usuario,
                                              value = 2)
     self.radio_label.pack()
     self.radio_basico.pack()
     self.radio_admin.pack()
            #checkbox de notificações
     self.checkbox_notificacoes = ctk.CTkCheckBox(self.aba_perfil,
                                                  text="Receber Notificações")
     self.checkbox_notificacoes.pack(pady = (20, 20))   
            #botão salvar perfil 
     self.botao_salvarperfil = ctk.CTkButton(self.aba_perfil,
                                             text="Salvar Perfil",
                                              fg_color="green",
                                              hover_color="darkgreen",
                                              command= self.salver_perfil)

    #função command atribui uma função a variável 
    #ou seja, ela salva as informações 

     self,self.botao_salvarperfil.pack(pady=(20, 20))

#------------------------------------------------------------------------
#A cor padrão do botão é a cor definida "Azul claro"
#mas apos passarmos o mouse em cima ele troca para verde
#chamamos essa ação de passar o mouse em cima de hover_color 

#a modificação feita transforma a cor verde do botão em verde escuro 
#com a funcionalidade hover_color atribuida 
#------------------------------------------------------------------------
    def construir_abapreferencias(self):
        self.aba_preferencias = self.janela_abas.tab("Preferências")

        self.label_idiomas = ctk.CTkLabel(self.aba_preferencias,
                                          text="Selecione o idioma:")
        self.label_idiomas.pack(pady=(20, 5))

# label
# menu opções de idiomas 
        self.menu_idiomas = ctk.CTkOptionMenu(self.aba_preferencias,
                                        values = ["Português", "Inglês", "Espanhol", ])
        self.menu_idiomas.pack()   
# label
        self.label_volume = ctk.CTkLabel(self.aba_preferencias,
                                         text="Volume do Sistema")  
        self.slider_volume = ctk.CTkSlider(self.aba_preferencias,
                                           from_= 0, to=100,
                                           command=self.atualizar_volume)
        
        #essa função command automaticamente recebe o valor do parametro 
        #self.slider_volume =

        self.slider_volume.pack(pady=(30, 5))
        self.slider_volume.pack()
        self.slider_volume.set(50) #volume padrão definido 

        self.label_valor_volume = ctk.CTkLabel(self.aba_preferencias,
                                          text="50%")
        #esse label define o valor textual ao volume padrão de 50%

        self.label_valor_volume.pack()

# slider (armazenar a informação onde você vai posiciona - lo)
#------------------------------------------------------------------------

#O RadioButton:
# é especial, ele possui mais de um elemento editando
#a mesma variável - precisando criar uma variável externa e atribuir 
#essa variável para cada um deles para ele saber que esta conectado 

#Checkbox/Menu de Opções:
#Não é necessário porque ele é unico elemento editando uma única 
#variável, então passamos para ele uma lista de valores mesmo 
# lista_de_valores = ["Mação", "Pêra", "Abobrinha"]

# quando utilizamos uma variavel restrita daquele programa é preciso
#atribuir o "uderline_" a ela 


#------------------------------------------------------------------------ 
    def construir_abasistema(self): # aba dashboard  
        self.aba_sistema = self.janela_abas.tab("Dashboard")            
        self.label_carregamento = ctk.CTkLabel(self.aba_sistema, 
                                             text="Testar Carregamento do Sistema",
                                             font=ctk.CTkFont(size=16) )

        self.label_carregamento.pack(pady=(30, 30))

        self.barra_progresso = ctk.CTkProgressBar(self.aba_sistema,
                                                  width=400)

        self.barra_progresso.pack(pady=(10, 10))
        self.barra_progresso.set(0) #ela apenas exibe uma informação 

        self.botao_progresso = ctk.CTkButton(self.aba_sistema,
                                             text="Iniciar Carregamento",
                                             command=self.carregar)

        self.botao_progresso.pack(pady=(20, 20))
#------------------------------------------------------------------------

    def ir_para_dashboard(self):
        self.janela_abas.set("Dashboard")
    
    def mudar_modo_dark(self):
        if self.switch_mododark.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("System")
#--------------------------------------------------------------------------

    def salver_perfil(self):
        nome = self.campo_nome.get()
        if self.nivel_usuario.get() == 2:
            nivel = "Admin"
        else:
            nivel = "Básico"

        receber_notificacoes = self.checkbox_notificacoes.get()
        print("Nome", nome)
        print("Nìvel", nivel)
        print("Receber notificações", receber_notificacoes)

#EDITANDO A FUNÇÃO DO TITULO E DO SUBTITULO 
        self.titulo.configure(f"{nome} App")
        self.subtitulo.configure(text=nivel)
#------------------------------------------------------------------------

    def atualizar_volume(self, novo_valor_volume):
        #atribuir mais um valor além do self para preencher essa função

        self.label_valor_volume.configure(text=f"{int(novo_valor_volume)}%")
        #novo_valor_volume = percentual dessa variável % 
        #porém o valor aparece com casas decimais 

        #int = apacere o valor inteiro da porcetagem
#------------------------------------------------------------------------

#BOTÃO INICIAR CARREGAMENTO(COMO CARREGAR A BARRA DE PROGRESSO?)

    def carregar(self):
        for i in range(100):
         #executar uma tarefa que pode demorar
         
         time.sleep(0.1)#biblioteca que faz a contagem

         #a barra de progresso vai de 0% a 100%
         # o valor 1 = 100% pois os valores percentuais são decimais 
         #ou seje, 50% = 0,5 

         self.barra_progresso.set((i + 1)/100)# esse valor é divido por 100
         
#pra economizar memória a interface gráfica não mostra o carregamento
#então para cada atualização além mudar o valor da barra de progresso
# rodamos o comando:
         self.update()#atualiza toda a tela



#-----------------------------------------------------------------------

'''
Usamos a função init + a super init porque ao criarmos a janela do Aplicativo 
eu vou querer personalizar ela e adicionar outras coisas nela. O comando que ele 
execulta quando ele roda e quando é criada a classe dessa automaticamente 
o python execulta o comando init da classe. A partir de execultar tudo que ele fazia
na classe principal, então ele pode execultar os meus códigos personalizados.

OU seja, eu digo para o python:
tudo que tinha no init da classe original do tkinter 
eu quero que você continue execultando. 
Depois que você execultar tudo da classe antiga eu quero que você 
execulte os meus códigos personalizados.

SELF = sempre que eu quiser falar da janela do meu app
'''

app = Aplicativo() # Cria a instância usando a sua classe
app.mainloop()     # Inicia o loop do programa