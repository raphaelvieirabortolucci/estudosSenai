"""
8. Crie uma variável x com o valor escolhido pelo usuário e outra y com o valor
escolhido pelo usuário. Calcule e imprima o resultado da divisão inteira de x por y.
"""

#pede ao usario usando o input um numero, depois usa o float para a string transformar em um numero, pois pde ser valor quebrado
x = float(input("digite um numero: "))

#pede ao usario usando o input um numero, depois usa o float para a string transformar em um numero, pois pde ser valor quebrado
y = float(input("digite um numero: "))

divisao = x // y # duas // para indicar que sera a divisao inteira, ou seja se der resto ele ignora

print(divisao)
