"""
13. Crie uma variável raio com o valor escolhido pelo usuário. Calcule a área de um
círculo e imprima o resultado.
"""

#pede ao usuario o raio do circulo usando o float(input), pois pde ser valor quebrado
raio = float(input("fala seu raio ai: "))

#calcula a area do circulo, fazendo o valor de pi(3.14) vezes o raio elevado a 2
areaCirculo = 3.14 * (raio ** 2)

print(areaCirculo)
