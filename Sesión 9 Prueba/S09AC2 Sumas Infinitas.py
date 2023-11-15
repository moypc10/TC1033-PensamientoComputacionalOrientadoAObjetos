#Sumas Infinitas
s=("si")
n=("no")

x=int(input("Dime el valor de x: "))
y=int(input("Dime el valor de y: "))
print("Tu suma es:",x+y)
suma = input("¿Deseas hacer otra suma?")

if suma==s:
    while suma==s:
        x=int(input("Dime el valor de x: "))
        y=int(input("Dime el valor de y: "))
        print("Tu suma es:",x+y)
        suma = input("¿Deseas hacer otra suma? ")

if suma==n:
    print("Vuelva pronto")