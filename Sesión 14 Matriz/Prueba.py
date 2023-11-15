#Prueba Matriz

m=[ [0,0,0] , [0,0,0] , [0,0,0]]

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
                       