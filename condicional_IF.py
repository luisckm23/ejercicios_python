print("Programa de evaluación de notas ")

nota_alumno=(float(input("Introduce la nota del alumno: ")))

def evaluacion(nota):
    valoracion="aprobado"
    if nota <= 5:
        valoracion="Suspenso"
    return valoracion

print(evaluacion(nota_alumno))

#1. Número positivo o negativo
pasaElNumero=float(input("Escribe un número para saber si es positivo, negativo o cero: "))
def numeroPositivo(valor):
    if valor == 0:
        return "Es Cero"
    elif valor >= 0:
        return "Es Positivo"
    else:
        return "Es negativo"

print(numeroPositivo(pasaElNumero))

#2.Número mayor

tuNumero = float(input("Escribe un nùmero para decir cual es mayor: "))
tuNumeroDos = float(input("Escribe otro nùmero para decir cual es mayor: "))

def mayorQue(num1, num2):
    if num1 > num2:
        return "Tu primer nùmero es mayor"
    elif num2 > num1:
        return "Tu segundo nùmero es mayor"
    else:
        return "Los números son iguales"

print(mayorQue(tuNumero,tuNumeroDos))

#3. Par o impar
elNumero = int(input("Ingresa un número entero para saber si es par o no: "))
def imparNoImpar(num3):
    if num3 % 2 == 1:
        return "El número es impar"
    else: 
        return "El número es par"

print(imparNoImpar(elNumero))

#Día de la semana

dia = int(input("Escribe un nímero entre el 1-7, para saber qué día es: "))
def diaSemana(day):
    if day == 1:
        return "Es lunes"
    elif day == 2:
        return "Es martes"
    elif day == 3:
        return "Es miercoles"
    elif day == 4:
        return "Es jueves"
    elif day == 5:
        return "Es viernes"
    elif day == 6:
        return "Es sabado"
    elif day == 7:
        return "Es domingo"
    else:
        return "Número de día inválido"

print(diaSemana(dia))


#Mayor que 18
edad_usuario = int(input("Introduce tu edad: "))
def mayorDeEdad(edad):
    if edad >= 18 and edad <=99:
        return "Puedes pasar, eres mayor de edad"
    else:
        return "No puedes pasar, eres menor de edad o has ingresado una edad incorrecta"

print(mayorDeEdad(edad_usuario))