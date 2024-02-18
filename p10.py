#Escribir una función que calcule el factorial de un número dado.


numero = int(input("ingrese el numero: "))
factorial = 1
i = 1
while (i <= numero):
   factorial = factorial * i
   i = i + 1
print("el factorial del numero ingresado es: ",factorial)    


