#Tablas de Mult

arch=open("Tabla.txt","r")

x=(arch.readline())
y=(arch.readline())
X=int(x)
Y=int(y)
arch.close()

arch=open("Tabl.txt","w")

for i in range(1,11):
    msg= str(X) + " x " + str(i) + " = " + str(Y*i) +"\n"
    arch.write(str(msg))

arch.close()
