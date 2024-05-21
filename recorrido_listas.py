#Suma de elementos en una lista
#Escribe una función llamada suma_lista que tome una lista de números como argumento y devuelva la suma de todos los elementos en la lista.

def suma_lista(numeros): #pasamos por parametro numeros que será la lista
    suma = 0 #inicializamos una variable en 0 donde se guardarán los numeros de la lista
    for i in numeros: # el indice "i" recorre el rango de la longitud de la lista
        suma += i #la variable suma va guardandose los resultados: 
                  #cuando el indice esta en 0 toma valor de 1
                  #i= 0 suma= 1
                  #cuando el indice esta en 1, toma el valor de 2 y se suma con 1, que es 3
                  #i= 1 suma= 3
                  #cuando el indice esta en 2, toma el valor de 3 y se suma con 3, que es 6
                  #i= 2 suma= 6
                  #cuando el indice esta en 3, toma el valor de 4 y se suma con 6, que es 10
                  #i= 3 suma= 10

    return suma

lista_suma = [1,2,3,4]
resultado = suma_lista(lista_suma)
print(resultado)

#Buscar el elemento máximo:
#Escribe una función llamada maximo_lista que tome una lista de números como argumento y devuelva el elemento más grande en la lista.

def maximo_lista(lista_numeros): #Creamos la funcion para pasarle el parametro lista_numeros
    maximo = lista_numeros[0] #igualamos la variable con el primer valor de la lista
    for i in lista_numeros: #recorremos el indice en la lista que nos pasan por parametro
        if i > maximo: #si el indice es mayor a maximo, que en primera instancia dijimos es 1
            maximo = i #entonces maximo cambia su valor por el valor mayor que tiene i
    return maximo 

listaNumeros = [1,2,3] #declaramos la lista con los valores
resu = maximo_lista(listaNumeros) #creamos una variable para igualarla a la llamada de la funcion con el parametro que le pasamos
print(resu) 

#Eliminar duplicados:
#Escribe una función llamada eliminar_duplicados que tome una lista y elimine los elementos duplicados, manteniendo solo la primera ocurrencia de cada elemento en la lista.

def eliminar_duplicados(elimina_dup): #definimos la funcion con el parametro que nos pasaran posteriormente
    lista_unicos = [] #creamos una lista vacia que es donde se guardan los valores unicos
    for i in elimina_dup: #recorremos el indice en la lista que es el parametro que nos van a pasar 
        if i not in lista_unicos: #si el indice no está en la lista de unicos
            lista_unicos.append(i) #agregamos el indice a la lista de unicos
    return lista_unicos

lista_original = [1, 2, 3, 4, 3, 2, 1, 5] #creamos la lista que le pasamos a la funcion
lista_sin_duplicados = eliminar_duplicados(lista_original) #igualamos una variable con la funcion y el parametro esperado 
print(f'Esta es la lista original: ',lista_original) 
print(f'La lista sin elementos duplicados:',lista_sin_duplicados)

#Contar ocurrencias de un elemento:
#Escribe una función llamada contar_ocurrencias que tome una lista y un elemento como argumentos, y devuelva el número de veces que ese elemento aparece en la lista.

elemento = int(input("Verifica si un numero esta en la lista y cuantas veces aparece: "))
def contar_concurrencias(listarepetidos, elemento):
    contador = 0
    for i in listarepetidos:
        if i == elemento:
            contador += 1
    return contador

lista_repetidos = [1, 2, 3, 4, 3, 2, 1, 5]
contarRepetidos = contar_concurrencias(lista_repetidos, elemento)
print(print(f"El elemento {elemento} aparece {contarRepetidos} veces en la lista."))

#Invertir una lista:
#Escribe una función llamada invertir_lista que tome una lista como argumento y devuelva una nueva lista que sea la inversa de la lista dada.

