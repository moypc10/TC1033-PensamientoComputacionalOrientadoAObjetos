#Costo Mensual Telefonía

Mens= int(input("Buenos días en Moycel le pedimos total honestidad \n¿Cuántos mensajes envío en el mes? "))
Meg= int(input("¿Cuántos megas uso en el mes? "))
Min= int(input("¿Cuántos minutos en llamada hizo en el mes? "))

T= (Mens + Meg + Min) * 0.8
print("El costo de su telefonía en este mes es de: $",T)
