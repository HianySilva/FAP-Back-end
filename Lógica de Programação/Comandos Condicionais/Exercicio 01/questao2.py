idade= int(input("Digite a idade do comprador:  "))

if idade <= 5:
    preco= 10

elif idade >=60:
    preco= 15

else:
    preco= 25

print(f"O valor que você pagará no ingresso é de: R$ {preco:.2f}")