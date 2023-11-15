#Número Menor A Inicial

x=int(input("Dime cuantos números deseas evaluar: "))
y=int(input("Dime tu Primer Número: "))

for i in range(0,x):
    #print("Dime un número: ",end="")
    n=int(input("Dime un número: "))
    if n<y:
        print(" Tu número",n,"es menor que",y)
    