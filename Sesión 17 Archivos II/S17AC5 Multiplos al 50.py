#Archivos de Salida

arch=open("Mult.txt","w")

n=int(input("Dime un número: "))

for i in range(0,51):
    msg= "El término "+str(i)+" es: "+str(i*n)+"\n"
    arch.write(str(msg))

arch.close()

