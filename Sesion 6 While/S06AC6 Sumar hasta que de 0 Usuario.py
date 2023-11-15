#Sumar Números hasta que de 0

m=int(input("Dime un número: "))
 
s=m

while m!=0:
    m=int(input("Dime otro número: "))
    s=s+m
    
print("Tu suma total es:",s)