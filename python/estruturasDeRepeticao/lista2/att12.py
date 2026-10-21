"""
12.Simule um caixa eletrônico COMPLETO.
○ Regras:
■ Menu com opções (usar laço infinito até sair):
a. Depositar
b. Sacar
c. Ver saldo
d. Sair
● Saldo inicial: R$ 1000
■ Para saque:
a. Só permitir valores múltiplos de 2
b. Calcular automaticamente notas (100, 50, 20, 10, 5, 2)
c. Se não for possível sacar → informar erro
■ Para depósito:
● Validar valores positivos
■ Extras:
● Impedir saque maior que saldo
● Registrar histórico simples (últimas operações usando lista)
● Mostrar resumo ao sair
"""

# Declara as variaveis de notas, de saldo, do registro de saques e o numero de saque
saldo = 1000
registro = []
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
numeroSaque = 0

# Inicia um laço de repetição
while True:

    # Cria uma mensagem monstrando as opções para o cliente
    print("Bem vindo ao caixa eletronico" \
    "\nQual opção você deseja: " \
    "\n 1-Depositar" \
    "\n 2-Sacar" \
    "\n 3-Verificar Saldo" \
    "\n 4-Sair")

    # Cria uma variavel para a resposta do cliente
    resposta = int(input("Digite a sua escolha: "))

    # Caso a resposta seja 1 executara esse if, para entra na area de deposito
    if resposta == 1:
        # Questiona o quanto vai depositar
        deposito = float(input("Quanto deseja depositar: "))

        # Verifica caso o deposito seja menor ou igual a zero
        if deposito > 0:
            print(f"Um deposito de {deposito}R$ foi realizado com sucesso")

        # Caso o valor seja menor ou igual a zero ele nao armazena os dados
        else:
            print("Digite um numero positivo e diferente que zero")
        continue

    # Caso a resposta seja 2 executara esse if, para entra na area de saque
    elif resposta == 2:
        # Pede ao usuario digitar a quantidade que vai sacar
        saque = int(input("Digite o valor que deseja sacar, apenas numeros multiplos de 2! " \
        "Saque: "))

        # Verifica se em saldo o insuficinete, caso sim ele ira parar o saque
        if saque > saldo:
            print("Digite um valor dentro de seu saldo atual!")
            continue

        # Verifica se o saque é um numero divisivel por 2
        if saque % 2 != 0:
            print("Digite um numero divisivel por 2!")

        # Caso passe pelos dos ifs ele ira executar o saque
        else:
            # Cria uma variavel para armazenar o total sacado (sera ultilzado no historico)
            # Diminui o saldo sobre o saque e iguala o valor total ao saque
            valorTotal = 0
            saldo -= saque
            valorTotal = saque

            # Caso o saque seja divisivel por 100 ele ira fara uma divisao inteira por 100
            # Apos isso vai pegar o resto do saque para o proximo if
            if saque >= 100:
                notas100 = saque // 100
                saque = saque % 100

            # Caso o saque seja divisivel por 50 ele ira fara uma divisao inteira por 50
            # Apos isso vai pegar o resto do saque para o proximo if
            if saque >= 50:
                notas50 = saque // 50
                saque = saque % 50

            # Caso o saque seja divisivel por 20 ele ira fara uma divisao inteira por 20
            # Apos isso vai pegar o resto do saque para o proximo if
            if saque >= 20:
                notas20 = saque // 20
                saque = saque % 20

            # Caso o saque seja divisivel por 10 ele ira fara uma divisao inteira por 10
            # Apos isso vai pegar o resto do saque para o proximo if
            if saque >= 10:
                notas10 = saque // 10
                saque = saque % 10

            # Caso o saque seja divisivel por 5 ele ira fara uma divisao inteira por 5
            # Apos isso vai pegar o resto do saque para o proximo if
            if saque >= 5:
                notas5 = saque // 5
                saque = saque % 5

            # Caso o saque seja divisivel por 2 ele ira fara uma divisao inteira por 2
            # Apos isso vai pegar o resto do saque para o proximo if
            if saque >= 2:
                notas2 = saque // 2
                saque = saque % 2

            # Se sobrar algo no saque ele ira perguntar ao usuario se ele que sacar esse valor sem o que sobrar ou se prefere digitar uam nova quantia
            if saque != 0:
                print(f"Houve um erro ao sacar o seu dinheiro, pois sobrou {saque} e não temos nota para essa quantia")
                resposta2 = int(input("Deseja sacar sem a quantia extra ou digitar outro valor ?" \
                "\n 1-Sacar" \
                "2-Digitar outro valor" \
                ": "))

                # caso queira sacar sem o extra ele ira devolver esse valor ao saldo e tirar o do valor total
                # Tambem zera o saldo para o proximo if
                if resposta == 1:
                    saldo += saque
                    valorTotal -= saque
                    saque = 0

                # Caso ele queira digitar um novo valor ele recomeca o laça
                else:
                    continue

            # Caso nao sobre saldo ele executa esse if
            if saque == 0:

                # Cria uma varivel mensagem para exebir as notas
                exibir = f"Você recebeu {notas100} notas de 100," \
                f" {notas50} notas de 50," \
                f" {notas20} notas de 20," \
                f" {notas10} notas de 10," \
                f" {notas5} notas de 5," \
                f" {notas2} notas de 2," 
                # Aumenta o numero do saque para registro do historico
                numeroSaque += 1
                # Cria u, historico para armazenar o dinheiro sacado
                historico = f"O valor total retirado no saque numero {numeroSaque} foi de {valorTotal} R$"
                # Armazena esse historico no registro
                registro.append(historico)
                print(exibir)

    # Exibe o saldo total e sua um for para percorrer o registro
    elif resposta == 3:
        print(f"Saldo total: {saldo}R$")
        for i in registro:
            print(i)

    # Finaliza o programa
    elif resposta == 4:
        print("FIm do banco...")
        break

    # Caso digite uma informação errada ele entra nesse else e repete o laço
    else:
        print("resposta invalida")