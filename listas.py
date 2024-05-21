#Sintaxis nombreLista = [elemento1, elemento2, elemento3...]
#                 índice  0           1           2

miLista = ["María", "Pepe", "Martha", "Antonio","Luis","Juan","Oscar","Jimena","Julian","Lety"]
mLista = [1,2,3,4,5,6,7]
print(miLista[:])
print(miLista[2])
print(miLista[-1])
print(mLista[1:6])

miLista.append("Sandra")
print(miLista[:])
miLista.insert(2,"Ana")
print(miLista[:])
miLista.extend(["Gaby","Roberto", "Carlos"])
print(miLista[:])
print(miLista.index("Gaby"))
miLista.remove("Ana")
print(miLista[:])