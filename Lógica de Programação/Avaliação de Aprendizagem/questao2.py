horas_trabalhadas= int(input("Informe a quantidade de horas trabalhadas: "))
valor_hora= float(input("Informe o valor da hora trabalhada: "))

salario= horas_trabalhadas * valor_hora * 22 

print(f"O funcionario trabalha {horas_trabalhadas} horas por dia e o seu salário é de: {salario:.2f}")