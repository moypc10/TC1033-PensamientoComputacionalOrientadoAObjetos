#Suma Resta, Mulltiplicacion y Residuo

def Operaciones(x,y):
    S= x + y
    Re= x - y
    D= x / y
    R= x % y
    print("Suma:",S,"\nResta:",Re,"\nDivisión:",D,"\nResiduo:",R)
    
a=int(input("Dime tu Primer Valor: "))
b=int(input("Dime tu Segundo Valor: "))

Operaciones(a,b)