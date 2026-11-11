"""
Criar uma calculadora que possui as seguintes funções:

- Desenhar menu ( Com a calculadora desenhada)
- Somar 
- Subtrair
- Dividir
- Multiplicar
- Raiz quadrada
- Potencia
- Porcentagem
- Desafio: Fotorial sem usar for ou while (e sem biblioteca)

usar def main
"""



# Cria uma variavel de desenho de um menu
def menu(resultado):
    return f"""
+---------------------------+
| ///////////////////////// |
+---------------------------+
|     [  {resultado} ]      |
+---------------------------+
|                           |
| [sto] [rcl] [<--] [AC/ON] |
|                           |
| [ ( ] [ ) ] [sqr] [ /  ]  |
|                           |
| [ 7 ] [ 8 ] [ 9 ] [ *  ]  |
|                           |
| [ 4 ] [ 5 ] [ 6 ] [ -  ]  |
|                           |
| [ 1 ] [ 2 ] [ 3 ] [ +  ]  |
|                           |
| [ 0 ] [ . ] [+/-] [ =  ]  |
+---------------------------+
"""

# Importa a biblioteca com as formulas necessarias
import math

# Cria as funcoes: Somar, subtrair, dividir, multiplicar, raiz, pontecia e porcentagem
# As 4 primeiras funcoes, usam os operadores basicos da matematica
# As Funções raiz e pontecia, usando respectivamente: math.sqrt -> faz a raiz quadrada, math.pow -> faz a pontecia do numero 1 sobre o 2
# A função Porcentagem, divide a porcentagem(numero1) por 100 e apos multiplica pelo valor total(numero2) 
def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def dividir(numero1, numero2):
    return numero1 / numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def raiz(numero):
    return math.sqrt(numero)

def pontecia(numero1, numero2):
    return math.pow(numero1, numero2)

def porcentagem(numero1, numero2):
    return (numero1 / 100) * numero2

# função que chama todoas as outras
def main():
    # Define o resultado igual a 0 para a calculadora
    resultado = 0
    # Cria um laço para printar o resultado na calculadora ou exibir o 0 caso nao tenha feito nenhuma operação
    while True:
        print(menu(resultado))

        # Usa um try para lidar com o caso de digitar letras no lugar de numero
        try:
            # Pede o primeiro numero ao usuario
            numero1 = int(input("Digite um numero: "))

            # Pede o operador para o usuario
            operador = input("Escolha entre: + - * / raiz potencia %: ")

            # Cria um if para a raiz, caso nao o operador escolhido nao seja a raiz, ele pede o segundo numero para se usar nas outras contas
            if operador == "raiz":
                numero2 = 0

            else:
                numero2 = int(input("Digite o segundo numero: "))

            # gera um cadeia de if e elif, que de acordo com o operador digitado, ele vai chamar a função correspondente e executar a conta
            if operador == "+":
                resultado = somar(numero1, numero2)
                continue

            elif operador == "-":
                resultado = subtrair(numero1, numero2)
                
                continue
            elif operador == "*":
                resultado = multiplicar(numero1, numero2)
                continue
            elif operador == "/":
                resultado = dividir(numero1, numero2)
                continue
            elif operador == "raiz":
                resultado = raiz(numero1)
                continue
            elif operador == "potencia":
                resultado = pontecia(numero1, numero2)
                continue
            elif operador == "%":
                resultado = porcentagem(numero1, numero2)
                continue
            else:
                print("Operador invalido")
                continue
        except ValueError:
            print("Valor invalido")

main()