#Palabra Alfabética
a=0
cont=0

x=input("Dime una palabra: ")
long=len(x)

for i in range(0,long):
    y=x[i]
    z=ord(y)
    if z > a:
        a=z
        cont+=1
    else:
        break

if cont==long:
    print("Tu palabra es Alfabética")
else:
    print("Tu palabra no es Alfabética")