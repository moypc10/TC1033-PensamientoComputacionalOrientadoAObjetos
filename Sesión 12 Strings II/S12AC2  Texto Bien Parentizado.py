#Bien Parentizado
cont=0
pal=0

x=input("Escribe un texto bien parentizado: ")
long=len(x)

for i in range(0,long):
    y=x[i]
    z=ord(y)
    pal+=1
    if z == 40:
        cont+=1
    elif z == 41:
        cont-=1
        pal=0

if pal==0 and cont==0:
    print("Tu texto esta bien parentizado")
else:
    print("Tu texto no esta bien parentizado")