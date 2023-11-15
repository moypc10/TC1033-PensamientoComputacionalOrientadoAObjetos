#1 en 1 incrementando y decrementando

i= 1

n=int(input("Dime un número: "))

while i <= n:
    print (i,end=", ")
    i+=1

while n !=1:
    n-=1
    if n==1:
        print(n,end="")
    else:
        print(n,end=", ")
    

