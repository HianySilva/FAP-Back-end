notas=[6,7,5,8,9]
soma= 0
x= 0
while x < 5:
    soma+=notas[x]
    x+=1
print("A media das notas é : %5.2f" % (soma/x))
