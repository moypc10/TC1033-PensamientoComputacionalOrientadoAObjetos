x=int(input("Dime el número de palabras que deseas tener en tu lista: ")) 

a=[] 

for i in range (0,x):
    y=input("Dime la palabra que deseas agregar: ")
    a.append(y)

a=list(set(a))
print(a)