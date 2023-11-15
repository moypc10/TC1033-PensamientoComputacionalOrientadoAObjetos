#Total de Números positivos

n=int(input("Dime los números positivos deseas sumar: "))
 
i=0
NT= 0

while i<n:
    m=int(input("Dime tu número: "))
    if m>0:
        i +=1
        NT+=1
        
    if m<=0:
        NT+=1
    
print("De los",NT,"números, fueron",i,"positivos")