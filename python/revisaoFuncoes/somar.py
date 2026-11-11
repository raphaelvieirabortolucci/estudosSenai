def somarPontos(fase1, fase2):
    if fase1 + fase2 >= 100:
        print("Você passou de fase!")

    elif fase1 + fase2 < 100:
        print("Pontuação insuficiente, tente de novo!")

somarPontos(50, 50)
somarPontos(60, 50)
somarPontos(30, 40)

