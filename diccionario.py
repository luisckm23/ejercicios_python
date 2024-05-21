miDiccionario={"Alemania":"Berlín",
              "Francia":"Paris",
              "UK":"Londres",
              "España":"Madrid"}

miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

miDiccionario["Italia"]="Roma"
print(miDiccionario)

del miDiccionario["España"]
print(miDiccionario)
