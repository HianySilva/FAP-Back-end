peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe a altura em metros: '))

imc = peso / (altura ** 2)


classificacao = ""
if imc < 18.5:
    classificacao = "baixo peso"
elif imc < 25:
    classificacao = "peso adequado"
elif imc < 30:
    classificacao = "sobrepeso"
else:
    classificacao = "obesidade"


print("\n===== RESULTADO DO IMC DO PACIENTE =====")
print(f"Seu Peso é:   {peso}")
print(f"Sua Altura é: {altura}")
print(f"Seu IMC é:    {imc:.2f}")
print("---------------------------------\n")
print(f"Classificação: Adulto com {classificacao}.")
print("=================================")

