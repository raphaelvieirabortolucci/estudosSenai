"""
5. Crie uma variável texto com o valor "150" como string. Converta esse valor para
inteiro e calcule a multiplicação do valor por 2, imprimindo o resultado
"""


valor = "150"

#jeito 1 - sem criar uma nova variavel

mult1 = int(valor) * 2 #define o valor com int e multiplica por 2

print(mult1)# exibe a multiplicacao

#jeito 2 -  craindo uma nova variavel

valorCovertido = int(valor) #cria um variavel para dizer que o valor virou um int

mult2 = valorCovertido * 2 #multiplicacao do valor convertido por 2

print(mult2)# exibe a multiplicacao
