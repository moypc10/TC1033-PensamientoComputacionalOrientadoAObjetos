#Mayor - Menor y Media
suma=0

n=int(input("Dime cuantos números deseas evaluar: "))
x=int(input("Dime un número: "))
a=x
b=x

for i in range (0,n-1):
    x=int(input("Dime un número: "))
    suma=suma+x
    if x<a:
        a=x
    if x>b:
        b=x

prom=(suma/n)
print("Tu promedio es:",prom,"\n",a,"es el número más chico\n",b,"es el número más grande")