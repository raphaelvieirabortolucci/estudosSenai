"""
5. Gerar um número aleatório entre 1 e 100.
○ Regras:
■ Usuário tenta adivinhar
■ Dar dicas:
■ "Muito alto" (diferença > 20)
■ "Alto"
■ "Muito baixo"
■ "Baixo"
■ Mostrar número de tentativas
■ Limite de 10 tentativas
"""
# Paga a biblioteca que randomiza os numeros
import random
# Cria as variaveis e aleatoriza um numero
tentativas = 10
diferencia = 0
numero = random.randint(1, 100)

# Define que o laço continua enquanto houver tentativas 
while tentativas!= 0:
     # mostra as tentativas para o usuario, pede um chute ao usuario e faz a diferencia entre chute e o numero
    print(f"tentativas: {tentativas}")
    chute = int(input("digite um numero entre 1 e 100: "))
    diferencia = chute - numero

    # Define que o numero tem que ser menor que 100 e maior que 0. Se a diferencia for maior que 20, o chute sera muito alto
    if diferencia >= 20 and chute <= 100 and chute > 0:
        print("chute muito alto")
        tentativas -= 1

    # Se a diferencia for maior que o numero e não for 20 numeros acima, diz que o chute é alto
    elif diferencia >= 1 and diferencia < 20:
        print("chute alto")
        tentativas -= 1

    # Se a diferencia der que falta 20 numeros para o numero, diz que o chute foi baixo
    elif diferencia <= -1 and diferencia <= 20:
        print("chute baixo")
        tentativas -= 1

    # Se a diferencia ser que falta mais de 20 numeros, diz que o chute foi muito baixo
    elif diferencia <= -20:
        print("chute muito alto")
        tentativas -= 1

    # Se a diferencia for zero, o usuario acertou o numero, diz "Você acertou o numero : {numero}"
    elif diferencia == 0:
        print(f"Você acertou o numero : {numero}")
        tentativas -= 1

    # Para caso o usuario digitar um numero maior que 100 ou menor que 0
    else:
        print("Opção invalidade, somente numero entre 1 e 100")