#Sumar Sin Positivos hasta que de 0

m=int(input("Dime un número: "))
 
s=m

while m!=0:
    m=int(input("Dime otro número: "))
    if m>0:
        s=s+m
    if m<=0:
        s=s
    
print("Tu suma total es:",s)