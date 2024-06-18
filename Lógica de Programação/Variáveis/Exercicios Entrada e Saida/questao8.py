qtd_folhas = int(input("Digite a quantidade de folhas do livro: "))
valor_copia = 0.08
qtd_paginas = qtd_folhas * 2
valor_total= qtd_paginas * valor_copia

print(f"O valor total a ser pago é: R$ {valor_total:.2f}")
