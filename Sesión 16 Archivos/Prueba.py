#Prueba

print("Tu Bloc de Notas dice:")
print()

arch=open("Hol.txt","r")
nomb=(arch.readline())
apell=(arch.readline())
edad=(arch.readline())

print("Nombre:",nomb,"Edad:",apell,"Edad:",edad)
arch.close()

