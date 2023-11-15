#1000 pesos Regalo
suma=10
edad=0

x=int(input("Dime la edad a la que empiezas a recibir dinero: "))

while suma < 1000:
    edad+=1
    suma=suma*2

print("Recibiras",suma,"a los",edad+x,"años")