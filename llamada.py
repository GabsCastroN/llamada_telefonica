#input
X = int (input ("Dime los minutos: "))

#Proccesing 

if X < 4:
    Y = 300

else:
    Y = (X * 50) + 300 - 150


if Y > 999:
    msj = "mil"

else:
    msj = "pesos"

#output
print ("los gastos totales son " + str(Y) + " " + msj)