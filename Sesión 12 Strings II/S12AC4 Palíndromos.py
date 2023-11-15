#Palíndromo
suma=0
cont=0

x=input("Dime un texto: ")
y=x.replace(" ","")

z=''.join(reversed(y))

if y == z:
    print("Tu frase es palíndroma")
else:
    print("Tu frase no es palíndroma")
