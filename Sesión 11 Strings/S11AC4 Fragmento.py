#Fragmento

x=(input("Dime una palabra: "))
long=len(x)

print("La longitud de tu palabra es de:",long)
print("El primer caracter es:",x[0])
print("El último caracter es:",x[long-1])

for i in range(0,long):
    r=i%2
    if r==1:
        print(x[i])
    
        