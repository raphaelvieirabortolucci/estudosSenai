"""
3. Crie um sistema de login com senha fixa.
○ Regras:
■ Usuário tem 3 tentativas
■ Após errar 3 vezes → bloquear acesso
■ Se acertar → exibir mensagem de sucesso
■ Mostrar quantas tentativas foram usadas



tentativaLogin == login and tentativaSenha == senha
"""
# Variaveis pre definiddas para usar no while
login = "RaphaelGatão"
senha = 3200
tentativas = 0
sobrando = 3

# Cria um laço que funciona enquando o valor não for 3
while tentativas != 3:

    # Input de tentativas do usuario
    tentativaLogin = input("Digite o Usuario de login: ")
    tentativaSenha = int(input("digite a senha: "))

    # Caso a tentativa de login e senha sejam iguais as variaveis login e senhas definidas antes, esse if vai ser executado
    if tentativaLogin == login and tentativaSenha == senha:
        print(f"login efetuado com sucesso")
        print(f"Bem vindo {login}")
        print(f"tentativas para logar = {tentativas}")
        
    # Caso alguma tentativa de login e senha seja diferente da variavel login e senhas definidas antes, esse if vai ser executado
    elif tentativaLogin != login or tentativaSenha != senha:
        print("login ou senha incorretas")
        sobrando -= 1
        print(f"Tentativas restantes: {sobrando}")
        tentativas += 1

# Como o laço quebra ao chegar a 3, esse if serva para dizer que o laço quebrou e o usuario não pode tentar
if tentativas == 3:
    print("\n !!!! Você não pode mais tentar !!!!")
    print(f"tentativas para tentarlogar = {tentativas}")        


