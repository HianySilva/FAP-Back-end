valor_duzia= 9.00
valor_laranja = valor_duzia / 12

qtd_laranjas = int(input("Digite a quantidade de laranjas que Soraia deseja comprar: "))

valor_total= qtd_laranjas * valor_laranja
print(f"O valor total da compra de Soraia é de: R$ {valor_total:.2f}")
