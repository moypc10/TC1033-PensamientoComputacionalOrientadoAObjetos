#Multiplicar Listas

n="0"
r=3
c=3
m=[]
p=[]
l=[]

def Inic(a,b,d,e):
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

def MultList(h,e,f):
    h[0][0]=(e[0][0]*f[0][0])+(e[0][1]*f[1][0])+(e[0][2]*f[2][0])
    h[0][1]=(e[0][0]*f[0][1])+(e[0][1]*f[1][1])+(e[0][2]*f[2][1])
    h[0][2]=(e[0][0]*f[0][2])+(e[0][1]*f[1][2])+(e[0][2]*f[2][2])
    
    h[1][0]=(e[1][0]*f[0][1])+(e[1][1]*f[1][0])+(e[1][2]*f[2][0])
    h[1][1]=(e[1][0]*f[0][1])+(e[1][1]*f[1][1])+(e[1][2]*f[2][1])
    h[1][2]=(e[1][0]*f[0][1])+(e[1][1]*f[1][2])+(e[1][2]*f[2][2])
    
    h[2][0]=(e[2][0]*f[0][1])+(e[2][1]*f[1][0])+(e[2][2]*f[2][0])
    h[2][1]=(e[2][0]*f[0][1])+(e[2][1]*f[1][1])+(e[2][2]*f[2][1])
    h[2][2]=(e[2][0]*f[0][1])+(e[2][1]*f[1][2])+(e[2][2]*f[2][2])

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

MultList(l,m,p)
ImpMat(l)


