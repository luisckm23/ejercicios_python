lista = []
for i in range(1,16):
    if i % 3 ==0 and i % 5 == 0:
        lista.append("fizzbuzz")
    elif i % 3 == 0:
        lista.append("fizz")
    elif i % 5 == 0:
        lista.append("buzz")
    else:
        lista.append(i)
print(lista)