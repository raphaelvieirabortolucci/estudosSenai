"""
15. Crie três variáveis, nota1, nota2 e nota3, com valores escolhidos pelo usuário.
Calcule a média ponderada dessas notas, onde os pesos são 2, 3 e 5,
respectivamente. Imprima o resultado.
"""


#pede a primera nota ao usario usando o float(input), pois pode ser valor quebrado
nota1 = float(input("digite a primeira nota: "))

#pede a segunda nota ao usario usando o float(input), pois pode ser valor quebrado
nota2 = float(input("digite a segunda nota: "))

#pede a terceira nota ao usario usando o float(input), pois pode ser valor quebrado
nota3 = float(input("digite a terceira nota: "))

#faz a multipicacao de cada nota e seu peso e depois divide pela soma dos pessos
mediaPoderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

print(f"a media das notas é {mediaPoderada}")
