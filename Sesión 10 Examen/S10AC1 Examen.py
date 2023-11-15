#Taquilla y Dulcería del Cine
b="Boletos"
p="Palomitas"
si="s"
no="n"
n="Nada"

def bol(c,d):
    y=int(input("¿Cuántos boletos deseas comprar? "))
    f=input("¿Tienes Folio de Descuento? \ns=si n=no  ")
    if f==c:
        print("El Total de tus Boletos es:",y*40)
    elif f==d:
        print("El Total de tus Boletos es:",y*80)
    else:
        print("Error de Entrada")

def pal (c,d):
    y=int(input("¿Cuántas Palomitas deseas comprar? "))
    f=input("¿Tienes Folio de Descuento? \ns=si n=no  ")
    if f==c:
        print("El Total de tus Palomitas es:",y*25)
    elif f==d:
        print("El Total de tus Palomitas es:",y*50)
    else:
        print("Error de Entrada")

ot=input("Bienvenido a CineTec, ¿Deseas ordenar algo? \ns=si n=no  ")

while ot==si:
    x=input("\nTenemos Palomitas o Boletos\n¿Qué deseas ordenar? \nEn caso de haber terminado tu orden escribir 'Nada' ")
    if x==b:
        bol(si,no)
    elif x==p:
        pal(si,no)
    elif x==n:
        break

    while x!=b and x!=p:
        x=input("\nError de Entrada, tenemos Palomitas o Boletos\n¿Qué deseas ordenar? \nEn caso de haber terminado tu orden escribir 'Nada' ")
        if x==b:
            bol(si,no)
        elif x==p:
            pal(si,no)

print("Gracias por su visita")