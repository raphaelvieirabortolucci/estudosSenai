inicio = "---- Bem Vindo ao setor de emprestimo"

resquisitos = "o minimo para o emprestimo é: \n" \
"18 anos e uma renda de mais 1500 \n" \
"ou \n" \
"menor de idade com \n"

def verificarEmprestimo(idade, renda, nome):
    if idade >= 18 and renda > 1500:
        print(f"{nome}, você pode pedir um emprestimo")
        
    elif idade >= 18 and renda <= 1500:
        print(f"{nome}, você não pode pedir um emprestimo, pois você ganha só {renda} , o minimo é acima 1500")
        
    
    elif idade < 18 and renda > 1000:
        print(f"{nome}, você pode pedir um emprestimo")
        
    
    elif idade < 18 and renda <= 1000:
        print(f"{nome}, você não pode pedir um emprestimo, pois você ganha só {renda} , o minimo para menor de idade é acima 1500")
        
  
print(inicio)

print(resquisitos)

nome = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))
renda = float(input("digite a sua renda: "))


print(verificarEmprestimo(idade, renda, nome))
