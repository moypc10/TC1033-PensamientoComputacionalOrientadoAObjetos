#Litros de Pintura

import math

m2 = int(input("¿Cuántos metros cuadrados quieres pintar? "))
Ef = int(input("Un litro de pintura ¿Cuántos metros cuadrados cubre? "))

Div = m2/Ef
lit = math.ceil(Div)

print("Se usara un total de",lit,"litros de pintura para cubrir toda la superficie")