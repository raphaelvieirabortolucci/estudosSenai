"""
10.Duas cidades:
○ A: 1000 habitantes, cresce 3% ao ano
○ B: 5000 habitantes, cresce 1.5% ao ano
○ Regras:
■ Usar laço para simular anos
■ Mostrar em quantos anos A ultrapassa B
■ Mostrar população final de cada uma
"""

cidadeA = 1000
cidadeB = 5000
ano = 0


while True:
    print(f"no ano {ano}, a cidade A tem {cidadeA} habitantes e a B tem {cidadeB} habitantes")

    if cidadeA < cidadeB:
        cidadeA = cidadeA + (cidadeA * 0.03)
        cidadeB = cidadeB + (cidadeB * 0.015)
        ano += 1

    elif cidadeA > cidadeB:
        break

diferencia = cidadeA - cidadeB

print(f"Apos {ano} anos, a cidade A ultrapassou a cidade B por {diferencia}")