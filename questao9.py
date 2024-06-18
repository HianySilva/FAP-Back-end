dias_atraso= int(input("Informe a quantidade de dias de atraso do empréstimo do livro: "))
custo_multa_por_dia= 0.75
valor_multa= dias_atraso * custo_multa_por_dia

print(f"O valor da multa a ser paga é de : R$ {valor_multa:.2f}")