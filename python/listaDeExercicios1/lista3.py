"""
3. Crie uma variável preco com o valor 50 e uma variável desconto com o valor 10.
Calcule o preço final após aplicar o desconto e imprima o resultado
"""


preco = 50
desconto = 10

#divide o desconto por 100% para dar 0.10 assim quando multiplicar com o o preco, vai dar os 10% de descontos no preco final
descontamento = desconto/100 * preco

# subtrai o preco inicial com a porcentagem do mesmo, para dar o valor do produto com o desonto
precoFinal = preco - descontamento 

print(precoFinal)
