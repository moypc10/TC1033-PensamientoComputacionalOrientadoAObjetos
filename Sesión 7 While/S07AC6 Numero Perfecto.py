#Numeros Perfectos

suma=0
d=0

n=int(input("Dime un número: "))
NP=n
m=n

while m != 0:
    r=n%m
    if r == 0:
        d= n/m
        suma= suma + d
        m-=1
    else:
        m-=1

suma=suma-n

if suma == NP:
    print("Tu número es perfecto")

else:
    print("Tu número no es perfecto")
        
        
