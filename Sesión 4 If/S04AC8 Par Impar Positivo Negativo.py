#Par Impar Positivo Negativo

x=int(input("Dime un número: "))

Pos = x//2
Par = x%2

if Pos > 0:
    if Par == 0:
        print("Tu número es par positivo")
    else:
        print("Tu número es impar positivo")

elif Pos < 0:
    if Par == 0:
        print("Tu número es par negativo")
    else:
        print("Tu número es impar negativo")
else:
    print("Tu número es par positivo")
