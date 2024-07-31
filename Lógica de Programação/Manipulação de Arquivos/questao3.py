
nome_arquivo_criacao = "arquivo3.txt"
conteudo = "A persistencia leva ao sucesso."

with open(nome_arquivo_criacao, "w") as arquivo:
    arquivo.write(conteudo)


nome_arquivo = input("Digite o nome do arquivo texto: ")


vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
contador_vogais = 0
contador_consoantes = 0

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    for char in conteudo:
        if char in vogais:
            contador_vogais += 1
        elif char in consoantes:
            contador_consoantes += 1

print(f"O arquivo {nome_arquivo} possui {contador_vogais} vogais e {contador_consoantes} consoantes.")
