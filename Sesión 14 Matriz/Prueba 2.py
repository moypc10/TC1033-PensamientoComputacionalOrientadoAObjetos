#Crear Lista

n="0"
r=int(input("Dime el número de renglones que deseas tener: "))
c=int(input("Dime el número de rengolnes que deseas tener: "))

m=[]

for i in range(r):
    a=[n]*c
    m.append(a)
    

for i in range(len(m)):        #N. Renglones
    for j in range(len(m[0])): #N. Columnas
        print("Elemento[",i,"][",j,"]: ",end="")
        m[i][j]=int(input())

print()

for i in range(len(m)):        #N. Renglones
    for j in range(len(m[0])): #N. Columnas
        print(m[i][j],"\t",end="")
    print()

print()
print(m)