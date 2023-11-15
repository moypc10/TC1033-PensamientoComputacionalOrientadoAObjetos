#Elevar un número

def potencia(n,e):
    r=n**e
    return r

x= int(input("Dime un número:: "))
y = int(input("Dime el número al que quiero ser elevado: "))

Res=potencia(x,y)
print(x,"elevado a la",y,"da igual a:",Res)