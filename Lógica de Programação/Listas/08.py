valores = []


while len(valores) < 8:
    valor = float(input(f"Digite o {len(valores) + 1}º valor: "))
    valores.append(valor)

while True:
    print("\nMENU:")
    print("1. Calcular média")
    print("2. Calcular soma")
    print("3. Calcular maior valor")
    print("4. Calcular menor valor")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        
        media = sum(valores) / len(valores)

        print(f"A média dos valores é: {media}")
    elif opcao == '2':

        soma = sum(valores)
        print(f"A soma dos valores é: {soma}")

    elif opcao == '3':

        maior = max(valores)
        print(f"O maior valor é: {maior}")
    elif opcao == '4':

        menor = min(valores)
        print(f"O menor valor é: {menor}")
    elif opcao == '5':

        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
