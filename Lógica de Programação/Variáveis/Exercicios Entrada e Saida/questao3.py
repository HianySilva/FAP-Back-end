brigadeiros= 0.90
cajuzinhos= 0.70
qtd_brigadeiros= int(input("Digite a quantidade de brigadeiros que você deseja encomendar:  "))
qtd_cajuzinhos= int(input("Digite a quantidade de cajuzinhos que você deseja encomendar:  "))

valor_total= brigadeiros * qtd_brigadeiros +  cajuzinhos * qtd_cajuzinhos

print("       ==== Brigadeiros e Cajuzinhos encomendados ===="    )
print(f"O valor total gasto com os doces encomendados é de : R$ {valor_total:.2f}")
