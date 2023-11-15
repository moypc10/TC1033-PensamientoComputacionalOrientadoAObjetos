#Prefijos

x=str(input("Dime una palabra: "))
y=input("Dime el prefijo de la palabra: ")

if x.startswith (y):
    print ("El prefijo es correcto")
else:
    print ("El prefijo es incorrecto")