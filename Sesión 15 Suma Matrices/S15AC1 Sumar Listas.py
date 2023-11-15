#Sumar Listas

n="0"
r=0
c=0
m=[]
p=[]
l=[]

def Inic(a,b,d,e):
    a=int(input("Dime el número de renglones que deseas tener: "))
    b=int(input("Dime el número de columnas que deseas tener: "))
    for i in range(a):
        x=[d]*b
        e.append(x)
    return a,b,c
    
def PidDatos(e):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            print("Elemento[",i,"][",j,"]: ",end="")
            e[i][j]=int(input())
    print()

def SumList(h,e,f):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            h[i][j]=e[i][j]+f[i][j]
        print()

def ImpMat(e):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            print(e[i][j],"\t",end="")
        print()

Inic(r,c,n,m)
Inic(r,c,n,p)
l=m

PidDatos(m)
PidDatos(p)

SumList(l,m,p)
ImpMat(l)

