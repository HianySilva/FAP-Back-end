def Menu():
    print("====MENU====\n")
    print("1- Somar\n")
    print("2- Subtrair\n")
    print("3- Multiplicar\n")
    print("4- Dividir\n")
    print("5- Sair\n")
    
    opcao= int (input ("Digite a opção que deseja: "))
    return opcao

def somar (numero1,numero2):
    solucao = numero1 + numero2
    return solucao


def subtrair (numero1,numero2):
    solucao = numero1 - numero2
    return solucao

def multiplicar (numero1,numero2):
    solucao = numero1 * numero2
    return solucao

def dividir (numero1,numero2):
    solucao = numero1 / numero2
    return solucao
 
i=0
opcao=0
num1=0
num2=0
solucao=0


while True:
    opcao= Menu()

    if opcao==1:
        num1= float(input("Informe o primeiro numero para a operação:"))
        num2= float(input("Informe o segundo  numero para a operação:"))

        solucao= somar(num1,num2)
        print(f"A solução da soma de {num1} e {num2} é :{solucao}")

    elif opcao==2:
        num1= float(input("Informe o primeiro numero para a operação:"))
        num2= float(input("Informe o segundo  numero para a operação:"))

        solucao= subtrair(num1,num2)
        print(f"A solução da subtração de {num1} e {num2} é :{solucao}")
        
    elif opcao==3:
        num1= float(input("Informe o primeiro numero para a operação:"))
        num2= float(input("Informe o segundo  numero para a operação:"))

        solucao= multiplicar(num1,num2)
        print(f"A solução da multiplicação de {num1} e {num2} é :{solucao}")

    elif opcao==4:
        num1= float(input("Informe o primeiro numero para a operação:"))
        num2= float(input("Informe o segundo  numero para a operação:"))

        solucao= dividir(num1,num2)
        print(f"A solução da divisão de {num1} e {num2} é :{solucao}")

    elif opcao==5:
        print(f"Finalizando Programa...")
        break
    else:
        print("Opção Invalida !")



