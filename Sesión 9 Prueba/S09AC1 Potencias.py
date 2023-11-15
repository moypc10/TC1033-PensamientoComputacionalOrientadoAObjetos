#Potencias

suma=0

x=int(input("Dime las potencias a las que deseas elevar 2: "))

for i in range(1,x+1):
    n=(2**i)
    suma=suma+n

print("La suma de tus potencias es",suma)