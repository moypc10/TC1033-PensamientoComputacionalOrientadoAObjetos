#Años Bisiesto

A= int(input("Dime un año: "))

Cu = A%4
Ci = A%100
Cua = A%400

if Cu == 0:
    if Ci == 0 and Cua != 0:
        print("Tu año no es bisiesto")
    else:
        print("Tu año es bisiesto")

else:
    print("Tu año no es bisiesto")
        
              