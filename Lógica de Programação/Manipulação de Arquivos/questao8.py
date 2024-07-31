nome_arquivo_criacao1 = "arquivo8.txt"
conteudo1 = (
    "Este é o conteúdo do primeiro arquivo. "
    "Será concatenado com o conteúdo do segundo arquivo.\n"
)

with open(nome_arquivo_criacao1, "w") as arquivo:
    arquivo.write(conteudo1)

nome_arquivo_criacao2 = "arquivo2.txt"
conteudo2 = (
    "Este é o conteúdo do segundo arquivo. "
    "Ele será adicionado após o conteúdo do primeiro arquivo.\n"
)

with open(nome_arquivo_criacao2, "w") as arquivo:
    arquivo.write(conteudo2)

nome_arquivo_entrada1 = input("Digite o nome do primeiro arquivo de entrada: ")
nome_arquivo_entrada2 = input("Digite o nome do segundo arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
ar
with open(nome_arquivo_entrada1, 'r') as arquivo_entrada1:
    conteudo1 = arquivo_entrada1.read()

with open(nome_arquivo_entrada2, 'r') as arquivo_entrada2:
    conteudo2 = arquivo_entrada2.read()

with open(nome_arquivo_saida, 'w') as arquivo_saida:
    arquivo_saida.write(conteudo1)
    arquivo_saida.write("\n")  
    arquivo_saida.write(conteudo2)

print(f"O conteúdo dos arquivos {nome_arquivo_entrada1} e {nome_arquivo_entrada2} foi concatenado e salvo em {nome_arquivo_saida}.")
