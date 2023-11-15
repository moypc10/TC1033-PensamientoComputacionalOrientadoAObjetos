#Numeros y Operacion

def suma(f,g):
    O= f + g
    return O

def resta(a,b):
    Op= a - b
    return Op

def mult(D,e):
    Ope= D * e
    return Ope

def div(h,i):
    Oper= h / i
    return Oper

x = int(input("Dime tu primer valor: "))
y = int(input("Dime tu segundo valor: "))
c = input("s = Suma \nr = Resta \nm = Multiplicación \nd = División \nDime la Operación que desees hacer: ")

Sum = "s"
Rest = "r"
Multip = "m"
Div = "d"

if c == Sum:
    R = suma(x,y)
    print("La Suma de",x,"+",y,"es de",R)
    
elif c == Rest:
    Re = resta(x,y)
    print("La Resta de",x,"-",y,"es de",Re)
    
elif c == Multip:
    Res = mult(x,y)
    print("La Multiplicación de",x,"*",y,"es de",Res)
    
elif c == Div:
    Resu = div(x,y)
    print("La División de",x,"/",y,"es de",Resu)
