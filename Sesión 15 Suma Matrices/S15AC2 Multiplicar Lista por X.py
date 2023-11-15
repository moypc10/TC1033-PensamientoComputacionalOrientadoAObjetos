#Sumar Listas

n="0"
r=0
c=0
m=[]
p=[]

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

def SumList(e,f):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            e[i][j]=e[i][j]*f
        print()
        
def ImpMat(e):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            print(e[i][j],"\t",end="")
        print()

Inic(r,c,n,m)
p=m

PidDatos(m)
v=int(input("Dime el número por el que deseas multiplicar tu lista: "))

SumList(p,v)

ImpMat(p)
