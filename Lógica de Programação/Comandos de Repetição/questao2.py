cont = 0
while (cont <= 10) :
  numero = float(input("Informe um número: "))
  if (numero % 2 == 0):
    print(f" número {numero} é par!")


  elif numero == 1:
    print(f"O número {numero} é par")

  else:
    print(f"O número {numero} é impar!")


print("Programa encerrado!")