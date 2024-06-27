
opcao = int(input("Digite a opção: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print("---------------------------------------")

if opcao==2:
    resultado = num1 + num2 + num3
    print(f"A soma dos números : {num1} + {num2} + {num3}  \nO resultado : {resultado:.2f}")
elif opcao == 3:
    resultado = num1 * num2 * num3 
    print(f"A mutiplicação dos números: {num1} * {num2} * {num3}  \nO resultado : {resultado:.2f}")

elif opcao == 4:
    if num1 + num2 > num3:
        resultado = "maior que"
    elif num1 + num2 < num3:
        resultado = "menor que"
    else:
        resultado = "igual a"
    print(f"A soma de {num1} e {num2} é {resultado} {num3}")
else:
    print("Opção inválida. Digite 2, 3 ou 4 para realizar a operação desejada.")