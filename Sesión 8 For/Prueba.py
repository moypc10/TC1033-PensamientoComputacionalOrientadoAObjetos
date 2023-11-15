#Prueba For
'''
for i in range (1,11,2): #Se inicia en 0
    print(i)

edad= int(input("Dime tu edad"))

for i in range(1,edad+1):
    print (i)
    
for i in range(edad):
    print(i+1)

suma= 0

for i in range(1,11):
    suma=suma+i

print(suma)
'''

for m in range (1,6):
    for n in range(1,6):
        print(m,"x",n,"=",m*n,"\t",end="")
    print()