#Tablas de Multiplicar Usuario

i= 1

t= int(input("Dime que tabla de multiplicar quieres: "))
n= int(input("Dime hasta que número lo deseas multiplicar: "))

while i <= n:
    print(t,"x",i,"=",t*i)
    i+=1
