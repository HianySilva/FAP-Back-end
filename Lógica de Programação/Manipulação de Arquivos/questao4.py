
nome_arquivo_criacao = "arquivo4.txt"
conteudo = (
    "Acredite em si mesmo e você será imbatível.\n"
    "A persistência leva ao sucesso.\n"
    "Encare cada desafio como uma chance de crescimento…\n"
)

with open(nome_arquivo_criacao, "w") as arquivo:
    arquivo.write(conteudo)

nome_arquivo = input("Digite o nome do arquivo texto: ")
caractere = input("Digite o caractere para contar: ")


if len(caractere) != 1:
    print("Por favor, digite apenas um caractere.")
else:
    
    contador = 0

    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        contador = conteudo.count(caractere)
    
    print(f"O caractere '{caractere}' ocorre {contador} vezes no arquivo {nome_arquivo}.")
