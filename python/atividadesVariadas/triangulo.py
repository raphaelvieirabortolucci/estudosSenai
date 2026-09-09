# nenhum dos lados pode ser maior que a soma dos outros lados
menu = "verificador de triangulos" \
"para dar certo, digite 3 numeors onde cada um deles não pode ser maior que a soma deles"

print(menu)

lado1 = int(input("digite um lado: "))
lado2 = int(input("agora digite outro lado: "))
lado3 = int(input("agora digite mais um lado: "))

def verificadorTriangulo(A, B, C):

    soma = B + C
    if A <= soma:
        return True

    else:
        return False

def verificadorEquilatero(A, B, C):
    if A == B == C:
        return True
    else:
        return False

def verificadorIsosceles(A, B, C):
    if A == B:
        return True
    
    elif A == C:
        return True
    
    elif C == B:
        return True
    
    else:
        return False


verificarlado1 = verificadorTriangulo(lado1, lado2, lado3)
verificarlado2 = verificadorTriangulo(lado2, lado1, lado3)
verificarlado3 = verificadorTriangulo(lado3, lado2, lado1)
equilatero = verificadorEquilatero(lado1, lado2, lado3)
isosceles = verificadorIsosceles(lado1, lado2, lado3)


if verificarlado1 == False:
    print("Não pode ser usado para um triangulo pois o lado 1 é maior que a soma dos outros")

elif verificarlado2 == False:
    print("Não pode ser usado para um triangulo pois o lado 2 é maior que a soma dos outros")

elif verificarlado3 == False:
    print("Não pode ser usado para um triangulo pois o lado 3 é maior que a soma dos outros")

elif equilatero == True:
    print("É um triagulo equilatero")

elif isosceles == True:
    print("É um triagulo isosceles")

else:
    print("É um tringulo escaleno")

