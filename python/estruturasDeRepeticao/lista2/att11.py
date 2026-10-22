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

numeros = []
for i in range(0, 101):
    numeros.append(True)

numeros[0] = False
numeros[1] = False

for numero in range(2, int(math.sqrt(100)) + 1):
    if numeros[numero]:
        for j in range(numero * numero, 101, numero):
            numeros[j] = False

primos = []
for i in range(2, 101):
    if numeros[i]:
        primos.append(i)

print("Primos:", primos)
print("Quantidade:", len(primos))
