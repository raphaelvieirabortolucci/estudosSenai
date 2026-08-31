"""
11. Crie duas variáveis, base e expoente, com valores escolhidos pelo usuário,
respectivamente. Calcule o valor de base elevado a expoente e imprima o
resultado.
"""

#pede ao usario usando o input uma base, depois usa o float para a string transformar em um numero que pode ser quebrado
#pois a base nao precisa ser inteira
base = float(input("Qual a base coleguina? "))

#pede ao usario usando o input um expoente, depois usa o int para a string transformar em um numero inteiro
#esse precisa ser inteiro, pois nao existe expoente com numero quebrado
expoente = int(input("Qual é o expoente coleguina? "))

resultado = base ** expoente #O ** faz a base pelo expoente

print(resultado)
