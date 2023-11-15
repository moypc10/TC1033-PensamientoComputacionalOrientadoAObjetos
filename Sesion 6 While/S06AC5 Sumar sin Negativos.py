#Sumar Número sin Negativos

n=int(input("Dime cuantos números deseas sumar: "))
 
i=1
s=0

while i<=n:
    m=int(input("Dime tu número: "))
    if m>0:
        s=s+m
        i +=1
    if m<=0:
        i +=1
    
print("Tu suma total es:",s)
           