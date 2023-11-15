#Número primo
x=0
contador= 0

def primo (a,b,c):
    for i in range (1,a+1):
        b= a%i
        if b==0:
            c+=1
    return c
        

n=int(input("Dime un número: "))

if n<1:
    print("Error de Entrada")
else:
    z= primo(n,x,contador)

if z<=2:
    print("Tu número es primo")
else:
    print("Tu número no es primo")
