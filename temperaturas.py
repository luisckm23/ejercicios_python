temperaturas = [21, 23, 19, 22, 20, 25, 24]
suma = 0
diferencia = []


for temperatura in temperaturas:
    suma += temperatura 
    maximo = max(temperaturas)
    minima = min(temperaturas)

promedio = suma / len(temperaturas)    

for temperatura in temperaturas:
     diferencia.append(temperatura-promedio)

print("La temperatura promedio fue: ", promedio)
print("La temperatura máxima fue: ", maximo)
print("La temperatura minima fue: ", minima)
print("Diferencias:", [round(dif, 1) for dif in diferencia])

