from collections import Counter
import string

nome_arquivo_criacao = "arquivo6.txt"
conteudo = (
    "Este é um exemplo de arquivo de texto. "
    "O objetivo é substituir todas as vogais por '**'.\n"
)

with open(nome_arquivo_criacao, "w") as arquivo:
    arquivo.write(conteudo)


nome_arquivo_entrada = input("Digite o nome do arquivo de entrada : ")
nome_arquivo_saida = "arquivo_saida.txt"

vogais = 'aeiouAEIOU'
substituicao = "**"

with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    conteudo = arquivo_entrada.read()
    conteudo_modificado = ''
    for caractere in conteudo:
        if caractere in vogais:
            conteudo_modificado += substituicao
        else:
            conteudo_modificado += caractere


with open(nome_arquivo_saida, 'w') as arquivo_saida:
    arquivo_saida.write(conteudo_modificado)

print(f"As vogais do arquivo {nome_arquivo_entrada} foram substituídas por '**' e o resultado foi salvo em {nome_arquivo_saida}.")
