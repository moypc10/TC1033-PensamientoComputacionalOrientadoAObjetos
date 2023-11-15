#Strings Prueba
'''
cadena= ("Moi es cool")
print(cadena)

ncadena=cadena[0:2]+"y"+cadena[3:]
print(ncadena)
'''
#Strings Prueba II
'''
cad=("Moisés Hiram Pineda Campos")

va="M" not in  cad
print(cad)
'''
#Strings Methods
'''
cade=("saludos BanDiTa")
v=cade.capitalize()
var=v.center(50,'*')
vari=v.count("a")
print("\n",cade,",v,",\n,",var,"\n",vari)
'''
#Format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))