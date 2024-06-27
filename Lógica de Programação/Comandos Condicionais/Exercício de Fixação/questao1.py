numero1= int(input("Informe o primeiro número: "))
numero2= int(input("Informe o segundo número: "))
numero3= int(input("Informe o terceiroo número: "))

if numero1 >= numero2 >= numero3:
    print(f"Os valores em ordem decrescente são: {numero1}, {numero2}, {numero3}")
elif numero1 >= numero3 >= numero2:
    print(f"Os valores em ordem decrescente são: {numero1}, {numero3}, {numero2}")
elif numero2 >= numero1 >= numero3:
    print(f"Os valores em ordem decrescente são: {numero2}, {numero1}, {numero3}")
elif numero2 >= numero3 >= numero1:
    print(f"Os valores em ordem decrescente são: {numero2}, {numero3}, {numero1}")
elif numero3 >= numero1 >= numero2:
    print(f"Os valores em ordem decrescente são: {numero3}, {numero1}, {numero2}")
else:  # numero3 >= numero2 >= numero1
    print(f"Os valores em ordem decrescente são: {numero3}, {numero2}, {numero1}")