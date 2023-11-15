#Quitar Elemento
m=0
cont=0

x=int(input("Dime el número de palabras que deseas tener en tu lista: ")) 

a=[] 

for i in range (0,x):
    y=input("Dime la palabra que deseas agregar: ")
    a.append(y) 

z=input("Dime la palabra que deseas eliminar: ")
long=len(a)

for i in range(0,long):
    if z==a[i]:
        m=i
        cont+=1

if cont>=1:
    del a[m]
    print (a)
else:
    print(a)