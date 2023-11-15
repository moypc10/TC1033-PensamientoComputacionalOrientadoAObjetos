#Contar Caracteres

m=input("Dime una palabra: ")
long=len(m)
cont=0

'''
z="Moisés"
print(z[0])
'''
while cont < long:
    print(m[cont])
    cont+=1
    
for i in range (0,long):
    print(m[i])


    
print("Tu palabra tiene",long,"caracteres")

