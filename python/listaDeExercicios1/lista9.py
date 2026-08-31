"""
9. Crie duas variáveis, num1 e num2, com valores solicitados ao usuário,
respectivamente. Verifique se num1 é maior que num2 e imprima o resultado
(True ou False). SEM USAR IF-ELIF-ELSE.
"""

#pede ao usario usando o input um numero, depois usa o float para a string transformar em um numero, pois pde ser valor quebrado
num1 = float(input("digite um numero: "))

#pede ao usario usando o input um numero, depois usa o float para a string transformar em um numero, pois pde ser valor quebrado
num2 = float(input("digite um numero: "))

resultado = num1 > num2 # veriafica de o valor do num 1 eh maior que num2

print(resultado)
