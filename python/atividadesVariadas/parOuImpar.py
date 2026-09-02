numero = int(input("digite um numero"))

identificador = numero % 2
if numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0:
    print("esse numero é par e divisivel por 3 e 5")

elif numero % 2 == 0  and numero % 3 == 0 :
    print("esse numero é par e divisivel por 3 e nao por 5")

elif numero % 2 == 0:
    print("esse numero é par nao divisivel por 3 e 5")

elif numero % 2 == 0 and numero % 5 == 0:
    print("esse numero é par e divisivel 5 e nao por 3")

elif numero % 3 == 0 and numero % 5 == 0:
    print("esse numero é impar e é divisivel por 3 e 5")

elif numero % 3 == 0:
    print("esse numero é impar e nao é divisivel por 3 e nao por 5")

elif numero % 5 == 0:
    print("esse numero é impar e nao é divisivel por 5 e nao por 3")

else:
    print("eh apenas um numero impar")