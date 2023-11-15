#Cuantos Pares e Impares Funcion

par=0
impar=0
e=0
re=0

def numpar(a,e,b,c,d):
    for i in range (0,a):
        e=int(input("Dime un número: "))
        d= e%2
        if d==0:
            b+=1
        else:
            c+=1
    return {"Pares:":b,"Impares":c}

x=int(input("Dime cuántos números deseas evaluar: "))

ParI = numpar (x,e,par,impar,re)

print(ParI)