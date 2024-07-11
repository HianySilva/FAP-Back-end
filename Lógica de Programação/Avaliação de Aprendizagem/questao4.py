dias = int(input("Informe a quantidade de dias: "))
opcao_quarto = int(input("Escolha a opção de quarto (1 para uma pessoa, 2 para duas pessoas): "))

if opcao_quarto == 1:
    valor_total = dias * 110.00
elif opcao_quarto == 2:
    valor_total = dias * 130.00
else:
    print("Opção de quarto inválida. Informe 1 ou 2.")
  

print(f"O valor total a ser pago é: R${valor_total:.2f}")


