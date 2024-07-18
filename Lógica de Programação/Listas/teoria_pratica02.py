
valores = []

while True:

    print("\nMenu:")
    print("1. Inserir valores")
    print("2. Calcular média")
    print("3. Calcular soma")
    print("4. Calcular maior")
    print("5. Calcular menor")
    print("6. Sair")
    
    escolha = input("\nEscolha uma opção (1-6): ")
    
    if escolha == '1':
        valores = []
        for i in range(8):
            valor = float(input(f"Insira o {i+1}º valor: "))
            valores.append(valor)
        print("Valores inseridos com sucesso!")
    elif escolha == '2':
        if not valores:
            print("Nenhum valor inserido ainda. Insira valores primeiro.")
        else:
            media = sum(valores) / len(valores)
            print(f"Média dos valores: {media}")
    elif escolha == '3':
        if not valores:
            print("Nenhum valor inserido ainda. Insira valores primeiro.")
        else:
            soma = sum(valores)
            print(f"Soma dos valores: {soma}")
    elif escolha == '4':
        if not valores:
            print("Nenhum valor inserido ainda. Insira valores primeiro.")
        else:
            maior = max(valores)
            print(f"Maior valor: {maior}")
    elif escolha == '5':
        if not valores:
            print("Nenhum valor inserido ainda. Insira valores primeiro.")
        else:
            menor = min(valores)
            print(f"Menor valor: {menor}")
    elif escolha == '6':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Escolha uma opção válida (1-6).")
