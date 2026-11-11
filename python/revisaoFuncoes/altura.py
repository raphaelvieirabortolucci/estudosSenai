# teste de mesa:
teste = """
-----------------------------------------------------------------------------------------
|       Situação      | altura | condição > 120 |               resposta                |
|   altura Raphael    |   180  |   verdadeiro   |             Acesso Liberado           |
|   altura Baixinho   |   120  |   verdadeiro   |             Acesso Liberado           |
|   altura Minusculo  |   119  |   falso        |    Desculpe, você é muito baixo ...   |
-----------------------------------------------------------------------------------------
"""

# Cria um função com 1 condição, se for maior ou igual a 120, retorna "Acesso Liberado", se for menor retorna "Desculpe, você é muito baixo ..."
def verificarAltura(alturaCm):
    if alturaCm >= 120:
        return "Acesso Liberado"
    elif alturaCm < 120:
        return "Desculpe, você é muito baixo ..."

# Cria 3 variaveis e atribui que os valores delas são as função com os respectivos valores: 180, 120 e 119
Raphael = verificarAltura(180)
Baixinho = verificarAltura(120)
Minusculo = verificarAltura(119)

# Exibe as variveis, como foi usado as funções como resposta das variaveis, vai retornar as resposta das funções de acordo com os parametros
# Exibe o teste de mesa
print(f"Raphael: {Raphael}, Baixinho: {Baixinho}, Minusculo: {Minusculo},")
print(f"Teste de mesa: {teste}")

