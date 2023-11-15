#Nombre y Edad

arch=open("NombEdad.txt","w")

n=input("Dime tu nombre: ")
nom= (n)+"\n"
arch.write(str(nom))

e=input("Dime tu Edad: ")
edad= (e)+"\n"
arch.write(str(edad))

arch.close()

