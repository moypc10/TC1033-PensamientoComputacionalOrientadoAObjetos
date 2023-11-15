#Números entre a y b

a=int(input("Dime el valor de a: "))
b=int(input("Dime el valor de b: "))

P1= a%2

if P1 == 0:
    while a<=b:
        print(a)
        a=a+2
        if a > b:
            break

if P1 == 1:
    a= a+1
    while a<=b:
        print(a)
        a=a+2
        if a > b:
            break