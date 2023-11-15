#Número Menor que 10

n=int(input("Dime un número"))

while n > 10:
    n= int(input("Dime otro número"))
    if n <= 10:
        print("Tu número es menor que 10")
        break