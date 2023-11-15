#Promedio

Materias= 0
Total = 0

Materias = int(input("¿Cuantas materias tienes? "))
TM = Materias

while Materias > 0:
      S = float(input("¿Cual fue tu calificación? "))
      Total += S
      Materias -= 1
      
if Materias == 0:
     Promedio = Total / TM
     
print("Tu promedio es: ", Promedio) 
      
      