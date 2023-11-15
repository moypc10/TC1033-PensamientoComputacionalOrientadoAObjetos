#Mayúsculas en Palabra

cont=0

x=(input("Dime una palabra: "))
long=len(x)

for i in range(0,long):
    y=x[i]
    z=ord(y)
    if z >= 65 and z <= 90:
        cont+=1

print("Hay un total de",cont,"mayúsculas en tu palabra")
        
