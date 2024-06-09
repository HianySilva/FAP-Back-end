vogais= 0
espacos= 0
frase= input("Escreva uma frase: ")

for caracter in frase:
    if caracter == " ":
        espacos+= 1
    elif caracter in "aeiouAEIOU":
        vogais += 1

print("Quantidade de espaços na frase :", espacos)
print("Quantidade de vogais na frase :", vogais)
