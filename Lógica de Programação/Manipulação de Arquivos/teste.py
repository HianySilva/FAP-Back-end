arquivo = open("arquivo.txt", "wt")
conteudo = "Um texto qualquer"
arquivo.write(conteudo)
arquivo.close()

arquivo= open("arquivo.txt", "wt")
conteudo2= "Outro texto qualquer"
arquivo.write(conteudo2)
arquivo.close()


arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()