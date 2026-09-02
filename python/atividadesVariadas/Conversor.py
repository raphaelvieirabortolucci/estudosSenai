menu = """
--------------Convertor-----------------
1 - Celsius para Fahrenheit
2 - Fahrenheit para Celsius
"""
print(menu)


escolha = int(input("digite o numero da sua escolha: "))


if escolha == 1:
    tempCelsius = int(input("temperatura em Celsius: "))
    conta = (tempCelsius * 9/5) + 32
    print(f"conversao para Fahrenheit: {conta}")

elif escolha == 2: 
    tempFahrenheit = int(input("temperatura em Fahrenheit: "))
    conta = (tempFahrenheit - 32) * 5/9
    print(f"conversao para Celsius: {conta}")

else:
    print("opcao invalidade")
