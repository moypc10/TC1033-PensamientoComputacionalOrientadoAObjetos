#Lista Determinante

n="0"
r=3
c=3
det=0
m=[]

def Inic(a,b,d,e):
    for i in range(a):
        x=[d]*b
        e.append(x)
    return a,b,e
    
def PidDatos(e):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            print("Elemento[",i,"][",j,"]: ",end="")
            e[i][j]=int(input())
    print()

def ImpMat(e):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            print(e[i][j],"\t",end="")
        print()

def Det(e,dt):
    r1=e[0][0]*(e[1][1]*e[2][2]-e[2][1]*e[1][2])
    r2=e[1][0]*(e[0][1]*e[2][2]-e[2][1]*e[0][2])
    r3=e[2][0]*(e[0][1]*e[2][2]-e[1][2]*e[0][2])
    dt=r1-r2+r3
    print()
    return dt

Inic(r,c,n,m)
PidDatos(m)
ImpMat(m)
dete=Det(m,det)

print("El Resultado de las Determinantes es:",dete)