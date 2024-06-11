def remover_espacos(texto):
    return texto.replace(" ", "")


frase= input("Digite uma frase : ")
resultado = remover_espacos(frase)
print(f"Resultado da sua frase sem espaços : {resultado}")