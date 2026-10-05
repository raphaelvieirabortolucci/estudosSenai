"""
9. Um número é perfeito quando a soma dos seus divisores (exceto ele) é igual a ele.
○ Ex: 6 → 1 + 2 + 3 = 6
○ Regras:
■ Pedir um número
■ Verificar usando laço
■ Mostrar os divisores
■ Informar se é perfeito ou não
"""

numero = int(input("Digite um numero inteiro para eu verificar se ele é perfeito: "))

soma = 0
contador = 1
divisores = []

while contador < numero:
    if numero % contador == 0:
        soma += contador
        divisores.append(contador)
    contador += 1

print(f"Divisores: {divisores}")

if numero > 0 and soma == numero:
    print("É um número perfeito")
else:
    print("Não é um número perfeito")
    