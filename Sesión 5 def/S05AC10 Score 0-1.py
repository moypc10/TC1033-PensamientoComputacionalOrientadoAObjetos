#Calificacion

def calcula_grado(a):
    if a>0.9 and a <=1:
        print("Tu calificación es A")
    elif a > 0.8 and a <= 0.9:
        print("Tu calificación es B")
    elif a > 0.7 and a <= 0.8:
        print("Tu calificación es C")
    elif a > 0.6 and a <= 0.7:
        print("Tu calificación es D")
    elif a <= 0.6:
        print("Tu calificación es F")
    else:
        print("Score Incorrecto")
        
C= float(input("Dime tu score 0-1: "))

R= calcula_grado(C)