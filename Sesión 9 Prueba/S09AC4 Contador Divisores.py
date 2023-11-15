#Contador Divisores
suma=0

def divisores(a):
    for i in range(a,0,-1):
        p=a%i
        if i==1:
            r=a/i
            print(r,end="")
            break
        if p==0:
            r=a/i
            print(r,end=", ")
    
x=int(input("Dime un número: "))

while x!=-1:
    divisores(x)
    suma+=1
    x=int(input("\nDime un número: "))

print("Se ingresaron",suma,"números válidos")