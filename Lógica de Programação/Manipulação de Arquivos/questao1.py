arquivo = open("arquivo1.txt", "wt")
conteudo = "Acredite em si mesmo e voce sera imparavel.\n A persistencia leva ao sucesso.\n Encare cada desafio como uma chance de crescimento…\n"
arquivo.write(conteudo)
arquivo.close()

arquivo = open("arquivo1.txt", "r")
conteudo1 = arquivo.read()

def contar_linhas(nome_arquivo):

  num_linhas = 0
  with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
      num_linhas += 1
  return num_linhas

nome_arquivo = input("Digite o nome do arquivo: ")
num_linhas = contar_linhas(nome_arquivo)
print("O arquivo possui {} linhas.".format(num_linhas))
