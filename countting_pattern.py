counts = dict() # creamos un diccionario vacío llamado 'counts'
print('Enter a line of text:') # pedimos una línea de texto al usuario
line = input(' ') # asignamos la línea de texto ingresada a la variable 'line'
words = line.split() # dividimos la línea de texto en palabras usando el método split() y asignamos la lista resultante a la variable 'words'
print('words', words) # imprimimos la lista de palabras
print('Counting') # imprimimos la cadena 'Counting'
for word in words: # recorremos cada palabra en la lista 'words'
     counts[word] = counts.get(word, 0) + 1 # para cada palabra que en el diccionario 'counts', obtenemos su conteo actual en el diccionario 'counts' (o 0 si no está presente) y le sumamos 1

print('counts', counts) # imprimimos el diccionario 'counts' que contiene cada palabra y su frecuencia en la línea de texto



