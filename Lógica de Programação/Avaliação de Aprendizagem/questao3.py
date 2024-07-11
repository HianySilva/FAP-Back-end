nome= str(input("Digite seu nome: "))

qtd_horas_dormidas=int(input("Informe a quantidade de horas que voce passa dormindo: "))

percentual_tempo= (qtd_horas_dormidas / 24 * 100)

print(f"{nome},  você passa {percentual_tempo:.2f}% do seu tempo de vida dormindo")

