#Tiempo Equivalente en Segundos

def equivalente(x,y,z):
    Ti= (x*3600)+(y*60)+z
    return Ti

H=int(input("Dime la cantidad de horas que deseas convertir: "))
M=int(input("Dime la cantidad de minutos que deseas convertir: "))
S=int(input("Dime una cantidad de segundos: "))

T = equivalente(H,M,S)
print(H,"horas",M,"minutos",S,"segundos son un total de",T,"segundos")
