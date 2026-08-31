"""
12. Crie uma variável preco com o valor escolhido pelo usuário. Converta esse valor
para uma string e concatene com a string "O preço é R$". Imprima o resultado.
"""

#pede ao usario usando o input um numero, depois usa o int para a string transformar em um numero inteiro
preco = int(input("digite o seu preco e se venda ao capitalismo: "))


#jeito 1 - sem criar uma nova variavel
#em uma linha so, pega a variavel preco e converte em texto 
#depois faz a concatenacao
contatenacao1 = "O preço é R$" + str(preco) 

print(contatenacao1)

#jeito 2 - criando uma nova variavel

precoConvertido = str(preco) #converte a variavel preco em string
contatenacao2 = "O preço é R$" + precoConvertido #faz a concatenacao

print(contatenacao2)
