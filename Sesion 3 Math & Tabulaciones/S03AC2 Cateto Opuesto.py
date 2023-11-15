#Buscar Cateto Opuesto
import math

Ca=float(input("¿Cuánto mide tu cateto adyacente? "))
Grad=int(input("¿Cúanto es tu ángulo? "))

Rad= math.radians(Grad)
tan = math.tan(Rad)
Co= (tan*Ca)

print("Tu cateto opuesto es:",Co)