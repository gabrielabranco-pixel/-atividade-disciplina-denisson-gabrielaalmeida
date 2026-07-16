'''
notas = [8.5, 7, 10, 9.5, 5, 6]

def calcular_media(notas):
    if len(notas) ==  0:
        return 0
    return sum(notas) / len(notas)

def classificar_media(media):
    if media >=9:
        return "Aprovado com sucesso"
    elif media >=6: 
        return "Aprovado mas precisa melhorar"
    else:
        return "Reprovado"
    
media_final = calcular_media(notas)
resultado = classificar_media(media_final)

print(f"A media final é: {media_final:.2f}")
print(f"Resultado: {resultado}")

'''

'''
def calcular_desconto(preco, percentual):
    preco = float(preco)
    desconto = (percentual / 100) * preco
    valor_final = preco - desconto
    return round(valor_final, 2)

print(calcular_desconto(14, 8))
'''