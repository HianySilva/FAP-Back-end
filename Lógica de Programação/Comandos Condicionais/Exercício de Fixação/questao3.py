nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 4:
    situacao = "na Prova final"
else:
    situacao = "Reprovado"



print("\n===== RESULTADO DO ALUNO ====")
print(f"Nota 1:    {nota1}")
print(f"Nota 2:    {nota2}")
print(f"Nota 3:    {nota3}")
print(f"Média:     {media:.2f}")
print("---------------------------------\n")
print(f"Situação: O aluno está {situacao}.")
print("=================================")
