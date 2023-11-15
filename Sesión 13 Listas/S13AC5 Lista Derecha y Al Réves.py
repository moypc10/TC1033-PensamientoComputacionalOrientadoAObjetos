#Lista Derecha y Al Réves

x=int(input("Dime el número de palabras que deseas tener en tu lista: ")) 

a=[]
b=[]

for i in range (0,x):
    y=input("Dime la palabra que deseas agregar: ")
    a.append(y)
    b.insert(0,y)

print(a)
print(b)