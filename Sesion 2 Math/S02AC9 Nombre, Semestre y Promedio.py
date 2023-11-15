#Promedio, Semestre y Nombre

Nom = input("¿Cuál es tu nombre completo? ")
Sem = int(input("¿En qué semestre vas? "))

C1 = float(input("¿Cuál es la calificación de tu primera materia? "))
C2 = float(input("¿Cuál es la calificación de tu segunda materia? "))
C3 = float(input("¿Cuál es la calificación de tu tercera materia? "))
C4 = float(input("¿Cuál es la calificación de tu cuarta materia? "))

P= (C1 + C2 + C3 + C4) / 4

print("Nombre:",Nom,"\nSemestre:",Sem,"\nPromedio:",P)
    