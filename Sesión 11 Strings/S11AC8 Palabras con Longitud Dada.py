#Palabras De Longitud Dada

cont=0
pal=0

x=input("Dime un texto: ")
y=int(input("Dime el número de carácteres que revisemos: "))
long=len(x)

for i in range(0,long):
    c=x[i]
    if c== " ":
        if cont==y:
            pal+=1
        cont=0
    if c!= " ":
        cont+=1
    if i==long-1:
        if cont==y:
            pal+=1
            
print("Hay un total de",pal,"palabras con",y,"dígitos")