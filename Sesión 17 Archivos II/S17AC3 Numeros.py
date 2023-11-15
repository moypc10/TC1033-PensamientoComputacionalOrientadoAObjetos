#Números por Línea

arch=open("Num.txt","w")

for i in range(1,6):
    msg= str(i)+"\n"
    arch.write(str(msg))

arch.close()

arch_i=open("Num.txt","r")
print(arch_i.read())

arch_i.close()