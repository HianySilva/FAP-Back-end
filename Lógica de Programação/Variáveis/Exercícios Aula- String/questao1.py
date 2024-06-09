data=input("Informe a  sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")

meses= {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembo",
    "12": "Dezembro",
    
}
print(f"Você nasceu em {dia} de {meses[mes]} de {ano}")