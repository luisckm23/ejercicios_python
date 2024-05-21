#Ejercicio 1: Contador de Números Positivos y Negativos
#Escribe un programa que permita al usuario ingresar números enteros. El programa debe contar cuántos de los números ingresados son positivos
#y cuántos son negativos. El programa terminará cuando el usuario ingrese 0.

# Solución propuesta
positivos = 0
negativos = 0

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    numero = int(input("Introduce otro número (0 para terminar): "))

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
