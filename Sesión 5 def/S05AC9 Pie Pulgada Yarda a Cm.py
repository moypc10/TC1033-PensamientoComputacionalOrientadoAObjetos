#Pies Pulgadas CYardas a Centimetros

def Pies(a):
    Op= a * 30.48
    return Op

def Pulg(b):
    Ope= b * 2.54
    return Ope

def yard(d):
    Oper= d*91.44
    return Oper

x = int(input("Dime la cantidad que desees convertir: "))
c = int(input("1 = Pies a Centímetros \n2 = Pulgadas a Centímetros \n3 = Yardas a Centímetros \nDime la Conversión que desees hacer: "))

if c == 1:
    R = Pies(x)
    print(x,"pies son",R,"centímetros")
    
elif c == 2:
    Re = Pulg(x)
    print(x,"pulgadas son",Re,"centímetros")
    
elif c == 3:
    Res = yard(x)
    print(x,"yardas son",Res,"centímetros")
    
else:
    print("Error")