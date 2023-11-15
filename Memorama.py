#Crear Lista

n="0"
aste="*"
r=4
c=4
m=[]
ast=[]
par=1
x1=0
y1=0
xx1=0
yy1=0
cont=0

def Inic(a,b,d,e):
    for i in range(a):
        x=[d]*b
        e.append(x)
    return a,b,c

def ImpMat(e):
    for i in range(len(e)+1): #N. Renglones
        for j in range(5):    #N. Columnas
            if i==0:
                print(j,"\t",end="")
            elif j==0:
                print(i,"\t",end="")
            else:
                print(e[i-1][j-1],"\t",end="")
        print()

def turnos(aster,xt,yt,xxt,yyt,jt,p,con):
    print("\n")
    ImpMat(aster)
    print("\n",jt,"Dime tu Coordenada de Renglones(1-4): ",end="")
    xt=int(input())
    print("\n",jt,"Dime tu Coordenada de Columnas(1-4): ",end="")
    yt=int(input())
    print("\n",jt,"Dime tu Segunda Coordenada de Renglones(1-4): ",end="")
    xxt=int(input())
    print("\n",jt,"Dime tu Segunda Coordenada de Columnas(1-4): ",end="")
    yyt=int(input())
    n1=ListAst(aster,m,xt,yt)
    n2=ListAst(aster,m,xxt,yyt)
    ImpMat(aster)
    if m[xt-1][yt-1]==m[xxt-1][yyt-1]:
        print("\n ¡Felicidades",jt,"te tardaste",cont,"turnos para encontrar el par! \n")
        p=4
    return p

def ListAst(e,l,xt,yt):
    e[xt-1][yt-1]=l[xt-1][yt-1]

def Reinic(e):
    for i in range(len(e)):        #N. Renglones
        for j in range(len(e[0])): #N. Columnas
            e[i][j]="*"
    
Inic(r,c,n,m)
Inic(r,c,aste,ast)

m[0][0]= 3
m[0][1]= 2
m[0][2]= 8
m[0][3]= 4

m[1][0]= 6
m[1][1]= 4
m[1][2]= 7
m[1][3]= 1

m[2][0]= 5 
m[2][1]= 7
m[2][2]= 2
m[2][3]= 5

m[3][0]= 1
m[3][1]= 8
m[3][2]= 6
m[3][3]= 3

print("Inicio: \n 1. Instrucciones \n 2. Jugar Memorama \n 3. Terminar Juego \n ¿Qué deseas hacer? Elige el número de tu preferencia: ",end="")
x=int(input())
j1=input("¿Cuál es el nombre del Jugador 1? ")
j2=input("¿Cuál es el nombre del Jugador 2? ")

while x!=3:
    if x>3 or x<=0:
        print("\n Error de Entrada \n Inicio: \n 1. Instrucciones \n 2. Jugar Memorama \n 3. Terminar Juego \n ¿Qué deseas hacer? Elige el número de tu preferencia: ",end="")
        x=int(input())
    if x==1:
        arch=open("Inst.txt","r")
        print(arch.read())
        print("Inicio: \n 1. Instrucciones \n 2. Jugar Memorama \n 3. Terminar Juego \n ¿Qué deseas hacer? Elige el número de tu preferencia: ",end="")
        x=int(input())
    if x==2:
        par=1
        while par==1 or par==2:
            if par==1:
                cont+=1
                par=turnos(ast,x1,y1,xx1,yy1,j1,par,cont)
                Reinic(ast)
                par+=1
            if par==2:
                par=turnos(ast,x1,y1,xx1,yy1,j2,par,cont)
                Reinic(ast)
                par-=1
            if par>=3:
                break
        print("Inicio: \n 1. Instrucciones \n 2. Jugar Memorama \n 3. Terminar Juego \n ¿Qué deseas hacer? Elige el número de tu preferencia: ",end="")
        x=int(input())
                
        #Imprimir Tabla de Asteriscos con Números Asignados
        
print("\n Gracias por jugar")