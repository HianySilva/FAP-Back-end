codigo = int(input("Digite o codigo  do produto: "))

Classificacao= ""
if codigo == 1:
    Classificacao= "Alimento não-perecível"

elif codigo in [2,3,4]:
    Classificacao = "Alimento perecível"

elif codigo in [5,6]:
    Classificacao= "Vestuário"

elif codigo == 7:
    Classificacao= "Higiene Pessoal"

elif codigo>=8 and codigo <=15:
    Classificacao = "Limpeza e Utensílios Domésticos"

else:
    Classificacao = "Código Invalido"

print(f"+----------------------------------------------+")
print("|        CLASSIFICAÇÃO DO PRODUTO              |")
print(f"+----------------------------------------------+")
print(f"| Código do Produto |   Classificação          |")
print(f"+----------------------------------------------+")
print(f"|         {codigo}         | {Classificacao}   |")
print(f"+----------------------------------------------+")