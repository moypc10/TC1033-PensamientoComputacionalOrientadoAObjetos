#Vocales en Mayúsculas

x=input("Dime una frase: ")
long=len(x)

for i in range(0,long):
    y=x[i]
    z=ord(y)
    if z== 97 or z== 101 or z==105  or z== 111 or z== 117:
        y=y.upper()
    print(y,end="")
