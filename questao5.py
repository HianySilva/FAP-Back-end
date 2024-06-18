minutos_processo = int(input("Digite quantos minutos Betina leva para analisar cada processo: "))
total_minutos_dia = 8 * 60
processos_revisados = total_minutos_dia / minutos_processo

print(f"Betina revisa {processos_revisados:.0f} processos por dia.")
