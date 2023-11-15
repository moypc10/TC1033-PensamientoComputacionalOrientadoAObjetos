#Distancia Plano Cartesiano
import math

x1 = int(input("Dime tu x1: "))
y1 = int(input("Dime tu y1: "))
x2 = int(input("Dime tu x2: "))
y2 = int(input("Dime tu y2: "))

D = ((x2-x1)**2)+((y2-y1)**2)
Dis = math.sqrt(D)

print("Tu distancia es:",Dis)