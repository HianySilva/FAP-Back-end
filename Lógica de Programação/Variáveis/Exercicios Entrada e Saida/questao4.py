brigadeiros= 0.90
cajuzinhos= 0.70
qtd_brigadeiros= int(input("Digite a quantidade de brigadeiros que você deseja encomendar:  "))
qtd_cajuzinhos= int(input("Digite a quantidade de cajuzinhos que você deseja encomendar:  "))
qtd_criancas= int(input("Digite a quantidade de crianças convidadas: "))


qtd__total_docinhos= qtd_brigadeiros + qtd_cajuzinhos
qtd_docinhos_por_crianca= qtd__total_docinhos / qtd_criancas

valor_total= brigadeiros * qtd_brigadeiros +  cajuzinhos * qtd_cajuzinhos

print("=============== Doces por crianças ================="    )
print(f"O valor total gasto com os brigadeiros e cajuzinhos é de : R$ {valor_total:.2f}")
print(f"Cada criança poderá comer {qtd_docinhos_por_crianca:.0f} docinhos.")
