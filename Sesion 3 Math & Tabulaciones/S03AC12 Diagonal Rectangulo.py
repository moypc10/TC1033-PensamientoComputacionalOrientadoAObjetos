#Diagonal Rectangulo
import math

A = int(input("Dime el ancho de tu rectángulo: "))
L = int(input("Dime el largo de tu rectángulo: "))

Diag= math.hypot(A,L)
print("La medida diagonal de tu rectángulo es:",Diag)