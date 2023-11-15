#Suma
suma=0

x=int(input("Dime cuántos números deseas sumar: "))

for i in range(0,x):
    x=float(input("Dime tu número: "))
    suma=suma+x

print("Tu suma es:",suma)