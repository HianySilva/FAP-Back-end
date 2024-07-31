
nome_arquivo_criacao = "arquivo2.txt"
conteudo = "aeiou"
with open(nome_arquivo_criacao, "w") as arquivo:
    arquivo.write(conteudo)


nome_arquivo = input("Digite o nome do arquivo texto: ")


vogais = 'aeiou'
contador_vogais = 0


with open(nome_arquivo, 'r') as arquivo:
    for char in arquivo.read():
        if char in vogais:
            contador_vogais += 1

print(f"O arquivo {nome_arquivo} possui {contador_vogais} vogais.")
