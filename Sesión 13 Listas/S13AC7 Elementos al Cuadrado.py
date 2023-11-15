#Elementos al Cuadrado

x=int(input("Dime el número de elementos que deseas tener en tu lista: "))

a=[] 

for i in range (0,x):
    y=int(input("Dime el número que deseas agregar: "))
    y=y**2
    a.append(y)

print(a)