lista1 = ["maca", "banana", "pera"] #alteravel

tupla = ("maca", "banana", "pera") #nao alteravel

dicionario = {
    "nome": "Maca",
    "cor": "vermelha",
}

# for ELEMENTO in SEQUENCIA:
for fruta in lista1:
    print(fruta)

for fruta in tupla:
    print(fruta)

print("separar") 
for i in range(5): #percorre os 5 numeros da posicao zero ate 4
    print(i)


#while True
#funciona ate ter um break
x = 0

print("separar")
while True:
    print(x)
    x += 2     
    if x > 10:  
        break

#while
#funciona enquanto a 
contador = 0

while contador <= 10: # vai realizar a contagem ate chegar a 10
    print("contagem:", contador)
    contador += 2
