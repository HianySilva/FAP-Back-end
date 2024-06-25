ano = int(input('Informe um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("\n===== RESULTADO DA VERIFICAÇÃO =====")
    print(f'O ano {ano} que você informou é um ano bissexto.')
    print("====================================\n")


else:
    print("\n===== RESULTADO DA VERIFICAÇÃO =====")
    print(f'O ano {ano} que você informou não é um ano bissexto.')
    print("====================================\n")