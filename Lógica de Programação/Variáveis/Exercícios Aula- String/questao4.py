def numero_por_extenso(numero):
    unidades=["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return "dezesseis" if numero == 16 else dezenas[numero - 10]
    else:
        dezena = dezenas[numero // 10]
        unidade = unidades[numero % 10]
        return dezena + (" e " + unidade if unidade else "")

numero =int(input("Digite um número até 99: "))
print(f"O número {numero} por extenso é : {numero_por_extenso(numero)}")