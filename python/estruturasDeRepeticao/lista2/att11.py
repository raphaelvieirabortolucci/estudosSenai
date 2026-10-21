"""
11. Peça um número inteiro N e encontre todos os números primos até N usando o
algoritmo do Crivo de Eratóstenes.
○ Regras:
■ Deve usar estrutura de marcação (lista/array)
■ Mostrar:
■ Lista de primos
■ Quantidade total
■ Calcular tempo de execução (opcional para desafio extra)
"""
import math
numeros =[]
for i in range(1, 101):
    i = True
    numeros.append(i)



for numero in numeros:
    numeros[math.pow(numero, 2)] = False
    for j in numeros(math.pow(numero, 2), 1, numeros):
        if j % numero == 0:
            numeros[j] = False
            continue

        else:
            continue
        
        


