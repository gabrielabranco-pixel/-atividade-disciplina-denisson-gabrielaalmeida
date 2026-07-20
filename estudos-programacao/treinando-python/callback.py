#Aprendendo sobre callbacks em Python 

#EXERC_01
def processar(numero, callback):
    # Chame o callback passando o dobro do número
    resultado = numero * 2 
    callback(resultado) 

def exibir(resultado):
    print(f"O resultado é: {resultado}")

processar(7, exibir)
#ele ira imprimir "O resultado é: 14" no console, pois o callback exibir é chamado com o resultado do processamento.
