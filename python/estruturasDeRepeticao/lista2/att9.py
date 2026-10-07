"""
9. Um número é perfeito quando a soma dos seus divisores (exceto ele) é igual a ele.
○ Ex: 6 → 1 + 2 + 3 = 6
○ Regras:
■ Pedir um número
■ Verificar usando laço
■ Mostrar os divisores
■ Informar se é perfeito ou não
"""
# Pede para o usuario para digitar um numero
numero = int(input("Digite um numero inteiro para eu verificar se ele é perfeito: "))

# Declara as variaveis
soma = 0
contador = 1
divisores = []

# Inicia um laço de repetição com um contador que nao pode passar o numero digitado pelo usuario
while contador < numero:
    # Cria um if para definir a condição de que o contador dividido por 2 sera armazenado na variavel divisores
    if numero % contador == 0:

        # Caso se a condição seja atendida o contador sera somado dentro da variavel soma e armazenado na lista de divisores
        soma += contador
        divisores.append(contador)
    # Adiciona 1 no contador para independente se o if foi feito ou nao. Depois repete o laço
    contador += 1

print(f"Divisores: {divisores}")

# Esse if define que se o numero for maior de zero e a soma igual ao numero, sera um numero perfeito
if numero > 0 and soma == numero:
    print("É um número perfeito")

# Caso a condição anterior não seja atendida ele executara o print
else:
    print("Não é um número perfeito")
    