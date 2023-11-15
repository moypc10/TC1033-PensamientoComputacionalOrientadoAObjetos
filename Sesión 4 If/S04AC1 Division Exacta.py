#Division Exacta o No

N1= int(input("Dime un numero: "))
N2= int(input("Dime otro numero: "))

R = N1%N2

if R == 0:
    print(N1,"/",N2,"es una división exacta")
    
else:
    print(N1,"/",N2,"no es una división exacta")