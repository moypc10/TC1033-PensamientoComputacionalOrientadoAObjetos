#Dígito en Palabra

cont=0

x=(input("Dime una palabra: "))
long=len(x)

for i in range(0,long):
    y=x[i]
    z=ord(y)
    if z >= 48 and z <= 57:
        cont+=1

if cont > 0:
    print("Contiene Dígito")

else:
    print("No Contiene Dígito")
    