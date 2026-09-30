"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

NAO ESTA FUNCIONANDO

Planejado: usar um laço infinito para pegar o voto do usuario, apos ele digitar 0, somar todos os votos e ver qual tirou o maior para exibir o ganhador. Em caso
de empate refaz a eleição


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""




"""8. Simule uma eleição com candidatos (1, 2, 3) e votos até o usuário digitar 0.
○ Regras:
■ Contar votos por candidato
■ Contar votos nulos
■ Mostrar vencedor
■ Mostrar porcentagem de cada um
"""


# laço infinit que pede para o usuario votar em candidatos, apois isso ele exibe o vencedor o refaz caso empate
while True:

    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    nulos = 0

    resposta = int(input('Você quer votar em 1. João Matador de porco || 2. Carlos "O Maluco" || 3. Rogerin do grau || 4. Nulo || 0. encerra as eleições: '))

    if resposta == 1:
        candidato1 += 1

    elif resposta == 2:
            candidato2 += 1

    elif resposta == 3:
            candidato3 += 1

    elif resposta == 4:
        nulos += 1

    elif resposta == 0:
        print("fim eleição")
        print(f"quantidade nulos : {nulos}")
        soma = candidato1 + candidato2 + candidato3

        if candidato1 > candidato2 and candidato1 > candidato3:
            percentual =(soma / candidato1) * 100
            print(f"O candidato vencedor é João Matador de porco, com {candidato1} votos")
            break

        elif candidato2 > candidato1 and candidato2 > candidato3:
            print(f"O candidato vencedor é João Matador de porco, com {candidato2} votos")
            break

        elif candidato3 > candidato2 and candidato3 > candidato1:
            print(f"O candidato vencedor é João Matador de porco, com {candidato1} votos")
            break

        else:
            print("Deu impate, refaz esse eleição")
