"""
4. Calcule a soma da série:
○ S= 1 + ( ½ ) + ( ⅓ ) + ( ¼ ) + ...
○ Regras:
■ Continuar até que o valor da parcela seja menor que 0.001
■ Mostrar quantos termos foram necessários
■ Mostrar soma final
"""

# Declara as variaveis
n = 1 
soma= 0 

# Usa de um laço para diminuir valor da parcela ate chegar em 0.001
while 1/n >= 0.001:

    # soma a parcela com a soma
    soma = soma + 1/n

    # Aumenta a parcela
    n += 1

print(f"A soma é {soma} e os termos utilizados foi {n - 1}")