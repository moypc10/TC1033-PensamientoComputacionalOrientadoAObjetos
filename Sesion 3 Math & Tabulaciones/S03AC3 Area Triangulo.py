#Area Triángulo

import math

A=float(input("¿Cuánto mide tu Lado A? "))
B=float(input("¿Cuánto mide tu Lado B? "))
Grad=int(input("¿Cúanto es tu ángulo? "))

Rad=math.radians(Grad)
A= 0.5*(A*B)*math.sin(Rad)

print("El Área de tu triángulo es: ",A)