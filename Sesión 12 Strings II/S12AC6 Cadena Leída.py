#Números Escritos

x=int(input("Dime cuantos números deseas evaluar:"))

for i in range(0,x):
    y=input("Determina el número que veces que desesas multiplicar: \nEj: uno, dos, tres, cuatro, etc... ")
    z=int(input("Determina que número vas a multiplicar: "))
    if y=="uno":
        print("Tu número es",z*1)
    if y=="dos":
        print("Tu número es",z*2)
    if y=="tres":
        print("Tu número es",z*3)
    if y=="cuatro":
        print("Tu número es",z*4)
    if y=="cinco":
        print("Tu número es",z*5)
    if y=="seis":
        print("Tu número es",z*6)
    if y=="siete":
        print("Tu número es",z*7)
    if y=="ocho":
        print("Tu número es",z*8)
    if y=="nueve":
        print("Tu número es",z*9)
    if y=="diez":
        print("Tu número es",z*10)
