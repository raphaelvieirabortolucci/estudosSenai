idade = int(input("Qual a sua idade? "))

if idade < 2:
    print("voce eh um bebe")

elif idade < 13:
    print("vc eh crianca")

elif idade < 18:
    print("vc eh adolescente") 

elif idade < 67:
    print("vc eh adulto")

else:
    print("vc eh idoso")
