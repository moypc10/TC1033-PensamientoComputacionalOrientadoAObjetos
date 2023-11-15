#Número Menor que el Número Anterior

x=int(input("Dime cuántos números deseas evaluar: "))
y=int(input("Dime tu primer número: "))

for i in range (0,x):
    z=int(input("Dime otro número: "))
    if z < y:
        print(z,"es menor que",y)
        y=z
    else:
        y=z
