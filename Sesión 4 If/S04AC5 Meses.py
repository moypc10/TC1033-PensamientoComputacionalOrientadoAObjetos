#Número de días de los meses

M=int(input("Elige un mes del 1 al 12: "))

if M == 2:
    print("Tu mes tiene 28 días")

elif M==4 or M==6 or M==9 or M==11:
    print("Tu mes tiene 30 días")
    
elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
    print("Tu mes tiene 31 días")
    
elif M == 0 or M > 12:
    print("Ese mes no existe")