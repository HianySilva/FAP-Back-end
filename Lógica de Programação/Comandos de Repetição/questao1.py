numero = float(input("Informe um número: "))
while (numero > 0) :
  if (numero % 2 == 0):
    print(f" número {numero} é par!")
  else:
    print(f"O número {numero} é impar!")
  numero = float(input("Informe um número: "))
print("Programa encerrado!")