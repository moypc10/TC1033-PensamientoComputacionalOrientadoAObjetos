#Archivos de Salida

arch=open("Exit.txt","w")

for i in range(20,25):
    msg= str(i)+"\n"
    arch.write(str(msg))

arch.close()

arch_i=open("Exit.txt","r")
y=arch_i.readline()
print(y*5)

arch_i.close()