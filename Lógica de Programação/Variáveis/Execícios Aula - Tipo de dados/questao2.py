altura=int(input("Informe a altura da sala em metros: "))
comprimento=int(input("Informe o comprimento da sala em metros: "))
largura=int (input("Informe a largura da sala em metros: "))

piso = comprimento*largura
paredes = 2 * (altura * comprimento) + 2 * (altura * largura)
volume = altura * comprimento * largura
print("")

print("A aréa do piso é:", piso, " m² ") 
print("A aréa das paredes é:", paredes," m² ")
print("O volume da sala é:", volume, "m^³")