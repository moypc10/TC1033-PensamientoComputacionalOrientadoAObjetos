#Número más cercano del tercero

P=int(input("Escribe tu primer número: "))
S=int(input("Escribe tu segundo número: "))
T=int(input("Escribe tu tercer número: "))

R= T - S
R1 = abs(R)

Re= T - P
R2 = abs (Re)

if R1 < R2:
    print("El segundo esta más cercano del tercero")
    
elif R1 > R2:
    print ("El primero esta más cercano del tercero")
    
else:
    print("EL primero y el segundo son igual de cercanos")