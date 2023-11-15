#Multiplos 100 Formato

arch=open("babynames.txt","r")

for i in range(1,1001):
    x=i%100
    if x==0:
        m=(arch.readline())
        sp=m.split()
        formato="Tu índice es "+ sp[0] + " y te llamas : " + sp[1] + " " + sp[2] +"\n"
        print(formato)
    else:
        (arch.readline())

arch.close()