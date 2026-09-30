"""6. Peça números ao usuário e calcule o fatorial.
○ Regras:
■ Não aceitar negativos
■ Permitir múltiplos cálculos até o usuário decidir sair
■ Mostrar passo a passo do cálculo
"""
# Pega a biblioteca para fazer o fatorial
import math

# Inicia um laço infinito
while True:

    # Pede para o usuario tomar uma dicisão
    print("Você quer: 1. Descobrir um fatorial || 2. Sair")
    resposta = int(input("Digite a sua escolha: "))

    # Caso seja 1, pede o numero e faz o fatorial
    if resposta == 1:
        numero = int(input("Digite o numero que você quer fatoriar: "))
        # Cria a variavel texto para colocar no print
        texto = f"!{numero} ="
        # Faz o fatorial
        resultado = math.factorial(numero)

        # Laço segundario para fazer exclusivo para fazer o texto de todos os fatoriais
        while numero > 0:
            texto += f" + {numero}"
            numero -= 1
        print(f"{texto} = {resultado}")

    # Acaba o laço principal
    elif resposta == 2:
        print("fim do programa")
        break

    # Caso o usuario digite errado
    else:
        print("opção invalida")