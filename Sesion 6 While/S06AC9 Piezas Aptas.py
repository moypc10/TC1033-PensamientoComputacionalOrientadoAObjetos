#Piezas Aptas

n=int(input("Dime la cantidad de piezas que deseas evaluar: "))
 
i=1
s=0

while i<=n:
    m=float(input("Dime la longitud de tu pieza: "))
    if m >= 1.2 and m <= 1.3:
        s+=1
        i +=1
    if m < 1.2 or m > 1.3:
        i +=1
    
print("Tienes un total de",s,"piezas aptas")