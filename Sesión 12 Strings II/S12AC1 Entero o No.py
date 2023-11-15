#Entero o No

cont=0

x=input("Dime un número: ")
long=len(x)

for i in range(0,long):
    y=x[i]
    z=ord(y)
    if z >= 48 and z <= 57:
        cont+=1

if cont==long:
    print("Es Entero")
else:
    print("No es Entero")
    