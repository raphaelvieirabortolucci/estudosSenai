numero = int(input("digite um numero"))
tabuada = 0

for i in range(0, 11):
    tabuada = i * numero
    print(f"{numero} x {i} = {tabuada}")