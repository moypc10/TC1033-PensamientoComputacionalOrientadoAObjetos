#Poblacion

import math

Pob = int(input("¿Cuál es tu Población Inicial? "))
Años = int(input("¿Cuántos años quieres que crezca tu Población? "))
TdC = float(input("¿Cuál es tu Tasa de Crecimiento? "))

Crec= Pob*(math.e**(TdC*Años))
PobFut = math.trunc(Crec)

print(PobFut)