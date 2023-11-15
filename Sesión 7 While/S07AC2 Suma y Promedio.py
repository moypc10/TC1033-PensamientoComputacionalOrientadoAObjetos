#Promedio y Suma

i=1
suma= 0

n=int(input("Dime la cantidad de número que deseas sumar: "))

while i<=n:
    print("Introduce el dato [",i,"]: ",end="")
    m=int(input())
    suma=suma+m
    i+=1
  
promedio= suma / n  
print("La suma es:", suma)
print("Tu promedio es:",promedio)
    