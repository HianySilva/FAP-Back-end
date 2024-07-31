
nome_arquivo_criacao = "arquivo7.txt"
conteudo = (
    "O objetivo é converter todas as letras minúsculas para maiúsculas.\n"
)

with open(nome_arquivo_criacao, "w") as arquivo:
    arquivo.write(conteudo)

nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    conteudo = arquivo_entrada.read()
    conteudo_modificado = conteudo.upper()

with open(nome_arquivo_saida, 'w') as arquivo_saida:
    arquivo_saida.write(conteudo_modificado)

print(f"O conteúdo do arquivo {nome_arquivo_entrada} foi convertido para maiúsculas e salvo em {nome_arquivo_saida}.")
