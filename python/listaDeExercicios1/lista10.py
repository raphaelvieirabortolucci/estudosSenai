"""
10. Crie uma variável idade com o valor escolhido pelo usuário. Calcule quantos dias
de vida aproximadamente essa pessoa já viveu (considerando 365 dias por ano) e
imprima o resultado.
"""


#pede ao usario usando o input um numero, depois usa o int para a string transformar em um numero inteiro
idade = int(input("digite a sua idade camaradinha do meu coracao: "))

tempoVida  = idade * 365 # multiplica seus anos de vida com os dias do ano, sem considerar ano bissexto

print(f"você viveu por {tempoVida} dias")
