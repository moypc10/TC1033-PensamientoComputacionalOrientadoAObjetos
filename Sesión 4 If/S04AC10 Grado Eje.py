#Grados del Plano Cartesiano

G=int(input("Dime un grado de 0° a 360°: "))

if G < 0 or G > 360:
    print("Tu Grado Excede")

elif G > 0 and G < 90:
    print("Tu Grado esta en el Cuadrante 1")

elif G > 90 and G < 180:
    print("Tu Grado esta en el Cuadrante 2")

elif G > 180 and G < 270:
    print("Tu Grado esta en el Cuadrante 3")
    
elif G > 270 and G < 360:
    print("Tu Grado esta en el Cuadrante 4")
    
elif G == 0 or G == 90 or G == 180 or G == 270 or G == 360:
    print("Tu Grado esta en un Eje")
      