desconto_ipva = 0.05
valor_ipva = float(input("Digite o valor do IPVA: "))
valor_taxa_transito = float(input("Digite o valor da taxa de trânsito: "))

valor_ipva_com_desconto = valor_ipva * (1 - desconto_ipva)
valor_total = valor_ipva_com_desconto + valor_taxa_transito

print(f"O valor total a ser pago por um motorista que deseja quitar sua dívida cinco dias antes do prazo é: R$ {valor_total:.2f}")