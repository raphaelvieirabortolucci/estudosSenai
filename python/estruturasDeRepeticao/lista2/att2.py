"""2. Peça um número inteiro positivo e gere a sequência de Collatz até chegar em 1.
○ Regras:
■ Mostrar cada passo
■ Contar quantas iterações foram necessárias
■ Informar o maior número atingido na sequência"""
""" sequecia:
• Se o número for par, divida-o por 2 (n / 2).
• Se o número for ímbar, multiplique-o por 3 e some 1 (3n + 1).
• Repita o processo com o novo resultado até chegar ao número 1
"""
# Da um input pedindo a variavel numero
numero = int(input("Digite um numero: "))

# Uma variavel para realizar a contagem das interações e uma para os resultados das interações
contador = 0
resultado = 0

# Cria um laço de repeticão que so vai parar quando o numero for 1
while numero != 1:
    
    # Só executa quando o numero é divisivel por 2, logo par
    if numero % 2 == 0:
        print(f"{numero} é par")
        # Uma variavel apenas para fazer um texto bonito no print
        numeroExp = numero
        # Realiza a conta da sequencia de Collatz, caso a numero seja par
        numero = numero / 2
        # Define o resultado
        resultado = numero
        print(f"{numeroExp} / 2 = {resultado}")
        print("continua a sequencia! ")
        #continua a contagem
        contador += 1


    else:
        print(f"{numero} é impar")
        # Uma variavel apenas para fazer um texto bonito no print
        numeroExp = numero
        # Realiza a conta da sequencia de Collatz, caso a numero seja impar
        numero = (numero * 3) + 1 
        # Define o resultado
        resultado = numero
        print(f"({numeroExp} * 3) + 1 = {resultado}")
        #continua a contagem
        contador += 1

print(f"O numero final é:{numero}")
print(f"a contagem ficou em {contador}")