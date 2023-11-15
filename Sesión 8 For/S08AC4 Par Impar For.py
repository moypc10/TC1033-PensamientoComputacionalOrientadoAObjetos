#Suma For Impar Par

def par(a,b):
    for i in range(a,b+1):
        p=i%2
        if p==0:
            print(i,"es par")
        else:
            print(i,"es impar")

x=int(input("Dime tu primer número: "))
y=int(input("Dime tu segundo número: "))

if y<=x:
    y=print("Error en los datos de Entrada")
else:
    par(x,y)