"""
1. Peça dois números inteiros (início e fim).
○ Exiba todos os números primos no intervalo.
○ Regras:
■ Não pode testar até o número inteiro → otimizar até √n
■ Validar entrada (início < fim)
■ Mostrar quantidade total de primos encontrados
"""
primos = []

print("Digite 2 números que eu vou falar todos os primos entre eles")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verifica se o numero 1 é menor que o 2, necessario para a sequencia
if numero1 >= numero2:
    print("Intervalo inválido! O primeiro número deve ser menor que o segundo.")

else:
    # Percorre todos os números do intervalo
    for numero in range(numero1, numero2 + 1):

        # Números exclui o 0 e o 1 da conta
        if numero <= 1:
            continue

        # É um verificador, ao setar o numero como primo = true, se ele nao for basta alterar o valor para false
        primo = True

        # Testa os divisores somente até a raiz quadrada
        for i in range(2, int(numero ** 0.5) + 1):

            # Se o numero ao divitido pelo i ter resto 0, ele é divisivel por ele, logo não é primo
            if numero % i == 0:
                primo = False
                break

        # Se não encontrou nenhum divisor, é primo
        if primo:
            primos.append(numero)

    print("Números primos:", primos) # Mostra os primos achados
    print("Quantidade de primos encontrados:", len(primos)) # Mostra a quantidade de primos
