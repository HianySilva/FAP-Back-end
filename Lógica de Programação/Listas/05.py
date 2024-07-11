num =[]

while True: 
    valor =(input("digite um numero: "))
    if valor.lower() == "sair":
        break
    num.append(float(valor))

num.sort()
print("Números Ordenados :", num)

