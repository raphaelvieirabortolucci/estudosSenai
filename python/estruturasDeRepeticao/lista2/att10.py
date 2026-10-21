"""
10.Duas cidades:
○ A: 1000 habitantes, cresce 3% ao ano
○ B: 5000 habitantes, cresce 1.5% ao ano
○ Regras:
■ Usar laço para simular anos
■ Mostrar em quantos anos A ultrapassa B
■ Mostrar população final de cada uma
"""
# Declara as variaveis das duas cidades e a variavel do ano
cidadeA = 1000
cidadeB = 5000
ano = 0


# Inicia uma laço de repetição
while True:

    # Exibe o ano atual e a quantidade de habitantes
    print(f"no ano {ano}, a cidade A tem {cidadeA} habitantes e a B tem {cidadeB} habitantes")

    # Esse if garante com que enquanto a cidadeA for menor que a cidadeB, o laço continua funcionando
    if cidadeA < cidadeB:
        # Aumenta a população da cidadeA em 3% relação dos habitantes atuais
        cidadeA = cidadeA + (cidadeA * 0.03)
        # Aumenta a população da cidadeB em 1,5% relação dos habitantes atuais
        cidadeB = cidadeB + (cidadeB * 0.015)
        # Aumenta o ano para marcar a passagem de tempo
        ano += 1
        # Apos isso o laço se repete

    # Se a cidadeA for maior que a cidadeB, esse elif quebra o codigo
    elif cidadeA > cidadeB:
        break

# Descobre a diferencia entre as cidades
diferencia = cidadeA - cidadeB

# Exibe a diferencia
print(f"Apos {ano} anos, a cidade A ultrapassou a cidade B por {diferencia}")