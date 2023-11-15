#Area Perimetro de Esfera

import math

def Volumen(x):
    P=(4/3)*math.pi*(x**3)
    return P

def Area(c):
    A= 4*(c**2)*math.pi
    return A

a=int(input("¿Cuál es el radio de tu esfera? "))

Pe= Perimetro(a)
Ar= Area(a)

print("El perímetro de tu Rectángulo es",Pe,"y su Área es",Ar)