#Sumas

def cont(a,b):
    for i in range(a,b+1):
        print(i,end=" ")

x=int(input("Dime el valor de x: "))
y=int(input("Dime el valor de y: "))

if x<y:
    cont(x,y)

else:
    cont(y,x)