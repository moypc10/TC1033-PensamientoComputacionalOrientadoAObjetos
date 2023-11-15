#Grados a Radianes

import math

G= int(input("Escribe la cantidad de grados que deseas convertir: "))

R= (G*math.pi)/180
Rad= math.radians(G)

print (G,"grados son",R,"grados")
print ("Según Python son: ",Rad)