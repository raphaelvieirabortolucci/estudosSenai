numero = int(input("digite um numero: "))
condicao = 0
fatorial = 1

while True:
    
    if numero > 0:  
        fatorial = fatorial * numero
        numero -= 1

    else:
        break
print(fatorial)    