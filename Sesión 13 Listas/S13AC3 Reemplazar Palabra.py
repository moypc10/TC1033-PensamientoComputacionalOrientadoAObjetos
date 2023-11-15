#Reemplazar Elemento por Usuario 

x=int(input("Dime el número de palabras que deseas agregar: ")) 

a=[] 

for i in range (0,x):
    y=input("Dime la palabra que deseas agregar")
    a.append(y) 

r=int(input("Dime el número de palabra desea reemplazar"))

z=input("Dime tu nueva palabra") 
print(z,"va a reemplazar",a[r-1])

a[r-1]=z
print(a)