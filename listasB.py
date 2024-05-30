#Este par de programas muestran la diferencia entre usar Métodos de Python contra no usarlos

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

avg = total / count
print('Average', avg)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/ len(numlist)
print('Average', average)
