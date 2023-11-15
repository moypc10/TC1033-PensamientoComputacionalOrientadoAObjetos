#Listas

x=["Moises","Hiram","Pineda","Campos"]
'''
print("Longitud de la Lista: ",len(x))
print(x[2])
x[1]="Mamado"
print(x)

del x[3]
print(x)

for i in x:
    print (i)
'''

for i in range(0,4):
    if i==2:
        x[i]="PINEDA"
    print(x[i])

if "Campos" in x:
    print("Si se apellida Campos")
else:
    print("No se apellida Campos")

x.append("Jiménez")
print(x)
    