qualidade = float(input('Informe a nota de qualidade (0-10): '))
preco = float(input('Informe a nota de preço (0-10): '))
prazo = float(input('Informe a nota de prazo (0-10): '))


if qualidade < 7:
    nota_geral = 0
elif qualidade >= 7 and preco >= 7:
    nota_geral = (qualidade + preco + prazo) / 3
elif qualidade >= 7 and preco < 7:
    nota_geral = (qualidade + 2 * preco + prazo) / 4

print("\n===== RESULTADO DA AVALIAÇÃO =====")
print(f"Nota de Qualidade: {qualidade:.2f}")
print(f"Nota de Preço:     {preco:.2f}")
print(f"Nota de Prazo:     {prazo:.2f}")
print("---------------------------------")
print(f"Nota Final:       {nota_geral:.2f}")
print("=================================\n")
