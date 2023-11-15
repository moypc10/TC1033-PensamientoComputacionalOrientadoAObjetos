#Funcion Sumar

def suma(a,b):
    for i in range(a,b+1):
        print(a,"+",i,"=",i+b)

x=int(input("Dime tu primer número: "))
y=int(input("Dime tu segundo número: "))

suma(x,y)