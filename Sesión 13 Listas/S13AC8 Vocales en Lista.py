#Vocales en Lista

a=0

vocales= ['a','e','i','o','u','A','E', 'I', 'O', 'U']

x=input("Dime una palabra: ")
long=len(x)

for i in range(0,long):
    y=x[i]
    if y in vocales:
        a+=1

print(x,"tiene",a,"vocales")
