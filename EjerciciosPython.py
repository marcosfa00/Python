#Ejercicios practica Python, declaraciond e variables etc
#Autor: Marcos Fernández Avendaño
import math


#Definicion de funciones
def potencia():
    print("Se calcula la potencia de dos núneros")
    num1 = input("Ingresa un número entero: ") #por defecto guardará un int, asiq deberemos castearlo
    num2 = input("Ingresa otro número entero: ")
    #para calcular la potencia podemos usar dos métodos
    result =math.pow(int(num1),int(num2))
    print(result)
    result=0

def printNumbers():
    #se imprimiarn en pantalla todos los números entre 10 y 20
    for x in range(10,21):
        print(x)

def printNumbers2(num):
    print(num)
#potencia()
printNumbers()

#array vacio
array = []

for x in range(1,5):
    array.append( input("Ingresa un número: "))

print(array)