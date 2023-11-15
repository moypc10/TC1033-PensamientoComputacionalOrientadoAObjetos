#Nombre y Edad con Formato

arch=open("NombEdad.txt","w")

n=input("Dime tu nombre: ")
nom= "Nombre: "+(n)+"\n"
arch.write(str(nom))

e=input("Dime tu Edad: ")
edad= "Edad: "+(e)+"\n"
arch.write(str(edad))

arch.close()
