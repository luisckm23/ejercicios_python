#Imprimir los números del 1 al 10.

for i in range(1,11,1):
    print(i)

#Calcular la suma de los números del 1 al 5.

suma = 0
for i in range(1,6):
    suma+=i
print(suma)

#Imprimir los elementos de una lista de frutas.
frutas = ["Naranjas", "Toronjas", "Manzanas", "Sandías", "Melones", "Tunas"]
for i in frutas:
    print(i)

#Contar las letras "a" en una cadena de texto.
contador = 0
cadenaDeLetras = "La agua está calientita ahorita"
for letra in cadenaDeLetras:
    if letra == "a":
        contador+=1
print("El número de letras 'a' en la cadena es:", contador)

#Imprimir los números impares del 1 al 10.


