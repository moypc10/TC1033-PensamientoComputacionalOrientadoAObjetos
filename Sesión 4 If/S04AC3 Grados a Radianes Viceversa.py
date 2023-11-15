#Grados a Radianes o VIceversa

import math

P=int(input("Elige la opción que desees usar: \n1. Grados a Radianes 2. Radianes a Grados  "))

if P == 1:
    G= int (input("Escribe los grados que deseas convertir: "))
    R = math.radians(G)
    print(G,"grados son",R,"radianes")

elif P == 2:
    G= int (input("Escribe los radianes que deseas convertir: "))
    Grad = math.degrees(G)
    print(G,"radianes son",Grad,"grados")
    
          
      
