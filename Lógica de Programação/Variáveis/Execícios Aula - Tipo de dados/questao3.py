horas= int(input("Informe a hora de 0 à 23: "))
minutos =int(input("Informe os minutos de 0 à 59: "))
segundos= int(input("Informe os segundos de 0 à 59: "))

segundos_desde_meiaNoite= horas * 3600 + minutos * 60 + segundos
 
print(f"Já se passaram {segundos_desde_meiaNoite:.0f} segundos desde a meia-noite. ")