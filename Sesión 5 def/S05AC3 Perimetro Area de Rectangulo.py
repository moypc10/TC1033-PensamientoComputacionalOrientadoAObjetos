#Area Perimetro de Rectangulo

def Perimetro(x,y):
    P=(x*2)+(y*2)
    return P

def Area(c,d):
    A= (c*d)
    return A

a=int(input("¿Cuál es el ancho de tu rectángulo? "))
b=int(input("¿Cuál es el largo de tu rectángulo? "))

Pe= Perimetro(a,b)
Ar= Area(a,b)

print("El perímetro de tu Rectángulo es",Pe,"y su Área es",Ar)