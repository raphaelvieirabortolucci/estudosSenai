"""
16. Crie quatro variáveis, x1, y1, x2 e y2, representando as coordenadas de dois
pontos no plano cartesiano (por exemplo, x1 = 1, y1 = 2, x2 = 4, y2 = 6). Os
valores devem ser solicitados pelo usuário. Calcule a distância entre esses dois
pontos usando a fórmula da distância euclidiana
"""

import math

x1 = int(input("fala o x1: "))
x2 = int(input("fala o x2: "))
y1 = int(input("fala o y1: "))
y2 = int(input("fala o y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distancia é {distancia}")
