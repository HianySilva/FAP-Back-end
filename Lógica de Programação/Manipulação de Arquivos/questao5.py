from collections import Counter
import string


nome_arquivo_criacao = "arquivo5.txt"
alfabeto = string.ascii_letters  # Inclui tanto letras maiúsculas quanto minúsculas
conteudo = f"{alfabeto}\n"

with open(nome_arquivo_criacao, "w") as arquivo:
    arquivo.write(conteudo)

nome_arquivo = input("Digite o nome do arquivo texto: ")

contador_letras = Counter()

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    for caractere in conteudo:
        if caractere in alfabeto:
            contador_letras[caractere] += 1

for letra in sorted(alfabeto):
    if contador_letras[letra] > 0:
        print(f"A letra '{letra}' aparece {contador_letras[letra]} vezes.")
