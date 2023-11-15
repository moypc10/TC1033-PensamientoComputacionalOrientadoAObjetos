#Programa que saca Area y Perimetro del Circulo

import math

A=float(input("¿Cuál es el radio de tu círculo? "))

x= math.pi*(A*A)
y= (2*math.pi)*A

print("Tu Área es: ", x,"y tu Perímetro es:", y)