#B mayor que A

a=int(input("Dime el valor de A: "))
b=int(input("Dime el valor de B: "))

while b < a:
    b=int(input("Dime otro valor de B: "))
    
print(b,"es mayor que",a)