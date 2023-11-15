#Vocal o No

def Vocal(l):
    if l==1 or l==5 or l==9 or l==15 or l==21:
        print("Tu letra si es vocal")
    elif l>26:
        print("Tu letra no existe")
    else:
        print("Tu letra no es vocal")

Letra=int(input("A=1 \nB=2 \nC=3 \nD=4 \nE=5 \nF=6 \nG=7 \netc \nDime una letra del Abecedario: "))

Vo=Vocal(Letra)
