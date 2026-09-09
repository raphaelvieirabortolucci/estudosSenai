import random




menu = "Escolha entre " \
"1 - Pedra" \
"/ 2 - Papel" \
"/ 3 - Tesoura"

jogo = ["pedra", "papel", "tesoura"]

jogador = ""

print(menu)

escolha = int(input("digite o numero da sua escolha: "))

if escolha == 1:
    jogador = "pedra"

elif escolha == 2:
    jogador = "papel"

elif escolha == 3:
    jogador = "tesoura"

else:
    print("opção invalida")

computador = random.choice(jogo)
print(computador)

if jogador == computador:
    print("empatou")

elif jogador == "papel" and computador == "pedra":
    print("jogador ganhou")

elif jogador == "tesoura" and computador == "papel":
    print("jogador ganhou")

elif jogador == "pedra" and computador == "tesoura":
    print("jogador ganhou")

else:
    print("computador ganhou")