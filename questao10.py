peso_prato = int(input("Digite o peso total do prato do cliente em gramas: "))
valor_kilo = 20
peso_prato_vazio=  peso_prato - 230
valor_refeicao = peso_prato_vazio * valor_kilo / 1000

print(f"O valor da refeição é: R$ {valor_refeicao:.2f}")

