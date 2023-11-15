#Millas a Kilometros

def millas(x):
    M= x*1.609
    return M

a=int(input("Dime el número de millas que deseas convertir: "))

Mi= millas(a)
print(a,"km son",Mi,"millas")