#Número primo
x=0
contador= 0

def primo (a,b,c):
    for i in range (1,a+1):
        b= a%i
        if b==0:
            c+=1
    if c<=2:
        return True
    else:
        return False
        

n=int(input("Dime un número: "))

if n<1:
    print("Error de Entrada")
else:
    z= primo(n,x,contador)

if z==True:
    print("Tu número es primo")
elif z==False:
    print("Tu número no es primo")