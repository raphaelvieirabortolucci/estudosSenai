"""
14. Crie duas variáveis, a e b, com valores escolhidos pelo usuário. Troque os valores
dessas variáveis sem usar uma terceira variável e imprima os novos valores de a e b.
"""
#pede ao usuario um valor usando o float(input), pois pde ser valor quebrado
a = float(input("escolhe o valor de a: "))
#pede ao usuario um valor usando o float(input), pois pde ser valor quebrado
b = float(input("agora faz o de b: "))

a, b = b, a # inverte o valor de a e b


print("Inverti os valores pq eu sou do mal hahaha")
print(f"valor novo de a: {a}")
print(f"valor novo de b: {b}")
