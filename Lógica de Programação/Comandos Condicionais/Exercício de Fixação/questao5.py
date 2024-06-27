dia_nascimento = int(input("Digite o dia do seu  nascimento: "))
mes_nascimento = int(input("Digite o mês do seu nascimento: "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

# Data de hoje
dia_atual = 26
mes_atual = 6
ano_atual = 2024

dias_totais = 0

if mes_atual > mes_nascimento or (mes_atual == mes_nascimento and dia_atual >= dia_nascimento):
    anos_completos = ano_atual - ano_nascimento
else:
    anos_completos = ano_atual - ano_nascimento - 1

dias_totais += anos_completos * 365

if mes_atual > mes_nascimento:
    dias_totais += (mes_atual - mes_nascimento) * 30  # Considera todos os meses com 30 dias
    dias_totais += dia_atual - dia_nascimento
elif mes_atual == mes_nascimento:
    if dia_atual >= dia_nascimento:
        dias_totais += dia_atual - dia_nascimento
    else:
        dias_totais += (30 - dia_nascimento) + dia_atual  # Considera todos os meses com 30 dias


print(f"Você viveu {dias_totais} dias até hoje.")
