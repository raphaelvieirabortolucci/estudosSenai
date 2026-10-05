"""8. Simule uma eleição com candidatos (1, 2, 3) e votos até o usuário digitar 0.
○ Regras:
■ Contar votos por candidato
■ Contar votos nulos
■ Mostrar vencedor
■ Mostrar porcentagem de cada um
"""


# laço infinit que pede para o usuario votar em candidatos, apois isso ele exibe o vencedor o refaz caso empate

candidato1 = 0
candidato2 = 0
candidato3 = 0
nulos = 0

while True:

    
    # Pede para votar em um candidato
    resposta = int(input('Você quer votar em 1. João Matador de porco || 2. Carlos "O Maluco" || 3. Rogerin do grau || 4. Nulo || 0. encerra as eleições: '))

    # Conta 1 voto para o candidato 1 caso o usuario vote em 1
    if resposta == 1:
        candidato1 += 1

    # Conta 1 voto para o candidato 2 caso o usuario vote em 2
    elif resposta == 2:
        candidato2 += 1

    # Conta 1 voto para o candidato 3 caso o usuario vote em 3
    elif resposta == 3:
        candidato3 += 1

    # Conta 1 voto para nulo caso o usuario vote em 4
    elif resposta == 4:
        nulos += 1

    # Ao digitar 0 para a votação e conta os votos, exibe a quantidades de nulos e a soma dos votos
    elif resposta == 0:
        print("fim eleição")
        print(f"quantidade nulos : {nulos}")
        soma = candidato1 + candidato2 + candidato3
        # Caso o candidato 1 tenha mais votos ele ganha, depois exibe a quantidade de votos e seu percentual
        if candidato1 > candidato2 and candidato1 > candidato3:
            percentual =(candidato1 * 100) / soma
            print(f"O candidato vencedor é João Matador de porco, com {candidato1} votos, com {percentual}% dos votos")
            break

        # Caso o candidato 2 tenha mais votos ele ganha, depois exibe a quantidade de votos e seu percentual
        elif candidato2 > candidato1 and candidato2 > candidato3:
            percentual =(candidato3 * 100) / soma
            print(f"O candidato vencedor é João Matador de porco, com {candidato2} votos, com {percentual}% dos votos")
            break
        # Caso o candidato 3 tenha mais votos ele ganha, depois exibe a quantidade de votos e seu percentual    
        elif candidato3 > candidato2 and candidato3 > candidato1:
            percentual =(candidato2 * 100) / soma
            print(f"O candidato vencedor é João Matador de porco, com {candidato1} votos, com {percentual}% dos votos")
            break

        # Se der empate, refaz a eleição    
        else:
            print("Deu impate, refaz esse eleição")
            candidato1 = 0
            candidato2 = 0
            candidato3 = 0
            nulos = 0
            continue
