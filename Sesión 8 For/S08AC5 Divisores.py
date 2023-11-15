#Divisores For

def divisores(a):
    for i in range(a,0,-1):
        p=a%i
        if i==1:
            r=a/i
            print(r,end="")
            break
        if p==0:
            r=a/i
            print(r,end=", ")
    
x=int(input("Dime un número: "))

divisores(x)