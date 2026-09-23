condicao = 0
maior = 0

while condicao < 5:
    numero = int(input("digite um numero: "))

    if numero > maior:
        maior = numero

    condicao += 1

print(maior)
    