nome = str(input("Informe o nome: "))
cont = 0

for i in nome.lower():
  if i == "a":
    cont += 1
print(f"Foram detectados {cont} letras A, no nome: {nome}")