#Multiplos 100

arch=open("babynames.txt","r")

for i in range(1,1001):
    x=i%100
    if x==0:
        print(arch.readline())
    else:
        (arch.readline())

arch.close()
        
