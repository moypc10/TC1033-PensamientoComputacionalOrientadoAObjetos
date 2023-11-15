#Espacios Blancos

p=input("Dime un texto: ")
long=len(p)
cont=0

for i in range (0,long):
    esp=p[i]
    if esp== " ":
        cont+=1
        
print("Espacios Blancos: ", cont)