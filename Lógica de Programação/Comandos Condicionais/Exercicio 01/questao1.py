salario= float(input("Informe o seu salário: "))

if salario > 1000:
    imposto = salario * 0.17

else:
    imposto = salario * 0.8

print(f"O valor do imposto a ser pago é: R$ {imposto:.2f}")
