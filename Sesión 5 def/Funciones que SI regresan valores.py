#Funciones que SI regresan valores

def suma(a,b):
    c=a+b
    return c #Regresarlo para que no sea variable local
    
print("Suma")
x=int(input("Dime tu Primer Valor: "))
y=int(input("Dime tu Segundo Valor: "))

z=suma(x,y)
print(z)

t=int(input("Dime tu Tercer Valor: "))
cu=int(input("Dime tu Cuarto Valor: "))
r=suma(t,cu)
print(r)