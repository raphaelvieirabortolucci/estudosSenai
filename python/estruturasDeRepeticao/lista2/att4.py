"""
4. Calcule a soma da série:
○ S= 1 + ( ½ ) + ( ⅓ ) + ( ¼ ) + ...
○ Regras:
■ Continuar até que o valor da parcela seja menor que 0.001
■ Mostrar quantos termos foram necessários
■ Mostrar soma final
"""

numero = 1
# Cria a variavel necessaria para fazer a conta dentro do while e difine a condição "termo" do while como 1 para o laçoe funcionar
termoParenteses = 2
termo = 1 
# Variavel de tentativas
tentativas = 0
# Variavel coma conta total (sera aumentada)
resposta = "S: 1 + 1/2"

# Laço de retição que para quando a conta do termo (1/termoParenteses) for 0.001
while termo != 0.001:
    # Realiza a conta do termo
    termo = 1 / termoParenteses
    # Aumenta em 1 o termoParenteses para continuar a fazer a conta do termo
    termoParenteses += 1
    # Armazena a resposta do termo na variavel resposta
    resposta += f"+ 1/{termoParenteses}"
    # Aumente as tentativa realizadas
    tentativas += 1
    

print(f"Conta: {resposta}")
print(f"tentativas: {tentativas}")
