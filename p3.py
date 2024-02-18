#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

x = int(input("ingrese la cantidad de numeros que desea obtener: "))    
lista = [random.randint(0,100)for i in range(x)]
print(lista)
