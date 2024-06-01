# #Found the smallest values

# smallest = 100
# print('Before', smallest)
# for num in [9,41,12,3,74,15]:
#     if num < smallest:
#         smallest = num
#     print(num, smallest)
# print('After', smallest)

# #Search using a Boolean variable

# found = False
# print('Before', found)
# for values in [9,41,12,3,74,15]:
#     if values == 3:
#         found = True
#     elif values != 3:  
#         found = False
#     print(found, values)

# print('After', found)



# # */ #Imprimir Números: Escribe un programa que imprima los números del 1 al 10 en orden ascendente.
# print("Escribe dos nùmeros para contar el rango entre ellos")
# rangoUno = int(input("Escribe el primero numero del rango"))
# rangoDos = int(input("Escribe el segundo nùmero del rango"))

# def imprimeNumeros (rangoUno, rangoDos):
#     for i in range(rangoUno, rangoDos + 1):
#         print(i)
#     diferencia = abs(rangoUno -  rangoDos)
#     print("La diferencia entre", rangoUno, "y", rangoDos, "es:", diferencia)

# imprimeNumeros(rangoUno, rangoDos) 

# # #Suma de Números Pares: Desarrolla un programa que sume todos los números pares del 1 al 100.

# print("Suma de Números Pares: Desarrolla un programa que sume todos los números pares del 1 al numero ingresado por el usuario.")

# numeroUsuario = int(input("Escribe un nùmero: "))
# def numerosPares(numeroUsuario):
#     suma = 0
#     for i in range(1,numeroUsuario + 1):
#        if i % 2 == 0:
#         suma += i 
#     return suma
# resultado = numerosPares(numeroUsuario)
# print("La suma de los números pares desde 1 hasta", numeroUsuario, "es:", resultado)

# # #Tabla de Multiplicar: Crea un programa que solicite al usuario un número y luego imprima la tabla de multiplicar de ese número del 1 al 10.

# print("Tabla de Multiplicar: Crea un programa que solicite al usuario un número y luego imprima la tabla de multiplicar de ese número del 1 al 10.")

# numeroDeTabla = int(input("Ingrese un número para obtener su tabla de multiplicar: "))

# def tablaMulti(numeroDeTabla):
#     print("La tabla de multiplicar de", numeroDeTabla, "es:")
#     for i in range(1, 11):
#         multiplicacion = i * numeroDeTabla
#         print(numeroDeTabla, "x", i, "=", multiplicacion)

# tablaMulti(numeroDeTabla)

# # #Sumar todos los elementos de una lista.

# lista = [1, 2, 3, 4, 5]

# def sumaLista():
#     suma = 0
#     for i in lista:
#         suma += i
#     return suma

# print(sumaLista()) 

# #Imprimir cada elemento de una lista en una línea nueva.

# listaLlena = [1,2,3,4,5]
# listaVacia = []

# def llenarLista ():
#     for i in listaLlena:
#         print(i)
#         listaVacia.append(i)

# llenarLista()
# print(listaVacia)

# #Contar cuántas veces aparece un elemento específico en una lista.

# listaRepetidos = [1,1,3,4,2,2,2,9,9,9,9,9,9]

# def contarRepetidos(elemento_objetivo):
#     cuenta = 0
#     for i in listaRepetidos:
#         if i == elemento_objetivo:
#             cuenta += 1
#     return cuenta

# elemento = 9
# print(f"El elemento {elemento} aparece {contarRepetidos(elemento)} veces en la lista.")

# #Multiplicar todos los elementos de una lista entre sí.

# def multiplicar_elementos_listas(listaUno, listaDos):
#     if len(listaUno) != len(listaDos):
#         print("Las listas deben tener la misma longitud.")
#         return None

#     producto_total = 1
#     for elemento1, elemento2 in zip(listaUno, listaDos):
#         producto_total *= elemento1 * elemento2

#     return producto_total

# listaUno = [1, 2, 3, 4]
# listaDos = [1, 2, 3, 4]
# resultado = multiplicar_elementos_listas(listaUno, listaDos)
# print("El producto de los elementos de las listas es:", resultado)

# #Esta funciòn retorna multiples valores 
# def coordenadasAlCuadrado(x,y):
#     coordenadaX = x * x
#     coordenadaY = y * y
#     return coordenadaX, coordenadaY

# xAlCuadrado, yAlCuadrado = coordenadasAlCuadrado(4,3)
# print(xAlCuadrado)
# print(yAlCuadrado)
# print(coordenadasAlCuadrado(4,3))

#Ejercicio: Filtrar y ordenas palabras

# Función para filtrar y ordenar palabras
def filtrar_y_ordenar_palabras(entrada):
    # Convertir la entrada en una lista de palabras
    palabras = [palabra.strip() for palabra in entrada.split(",")]
    
    # Filtrar palabras con más de 5 caracteres
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) > 5]
    
    # Eliminar duplicados convirtiendo la lista en un conjunto y luego de nuevo a una lista
    palabras_unicas = list(set(palabras_filtradas))
    
    # Ordenar la lista alfabéticamente
    palabras_ordenadas = sorted(palabras_unicas)
    
    return palabras_ordenadas

# Solicitar al usuario que ingrese una lista de palabras separadas por comas
entrada_usuario = input("Introduce una lista de palabras separadas por comas: ")

# Obtener el resultado
resultado = filtrar_y_ordenar_palabras(entrada_usuario)

# Imprimir el resultado
print(resultado)
