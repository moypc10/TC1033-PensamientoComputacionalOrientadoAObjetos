#Indice Masa Corporal

P=float(input("Dime tu peso: "))
A=float(input("Dime tu altura: "))

IMC= P / (A**2)

if 20 > IMC:
    print("Tienes Peso Bajo")

elif IMC >= 20 and IMC < 25:
    print("Tienes Peso Normal")
    
elif IMC >= 25 and IMC < 30:
    print("Tienes Sobre Peso")
    
elif IMC >= 30 and IMC < 40:
    print("Tienes Obesidad")
    
elif IMC >= 40:
    print("Tienes Obesidad Morbida")