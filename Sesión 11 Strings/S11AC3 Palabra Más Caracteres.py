#Palabra con más Caracteres

x=input("Dime tu primer palabra: ")
y=input("Dime tu segunda palabra: ")
lx=len(x)
ly=len(y)

if lx > ly:
    print(x)

elif lx < ly:
    print(y)
    
else:
    print(y,x)
    