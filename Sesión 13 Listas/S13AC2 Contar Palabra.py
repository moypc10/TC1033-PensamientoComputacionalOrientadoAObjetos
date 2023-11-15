#Count en lista 

x=int(input("Dime el número de palabras que deseas agregar: "))

a=[] 

for i in range (0,x):
    y=input("Dime la palabra que deseas agregar")
    a.append(y)
    
j=input("Dime la palabra que deseas contar")
b=a.count(j)

print(j," esta ",b," veces en la lista")
