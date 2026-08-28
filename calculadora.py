def indicaciones():
    print ("Esta es la prueba de una calculadora de 'basica'")
    print ("los unicos signos permitidos para el uso de esta calculadora son: /n")

#Las siguientes funciones seran las operaciones que tendran disponibles la calculadora

def suma(a, b):
    #Esta funcion nos permite realizar una suma
    return a + b
def resta(a, b):
    #Esta funcion nos permite realizar una resta
    return a - b
def multiplicacion(a, b):
    #Esta funcion nos permite realizar una multiplicacion
    return a * b
def division(a, b):
    #Esta funcion nos permite realizar una division
    if b == 0:
        print ("No se puede dividir entre cero")
    return a / b

def motor_de_operaciones():
    operaciones_validas ={"+", "*", "-", "/"} 
    indicaciones()
    try:
        var1 = int(input("ingresa un numero"))
        signo = input ("ingresa un signo aritmetico valido")
        var2 = int(input("ingresa un segundo numero"))
    except ValueError:
        print("solo se pueden ingresar numeros validos")

    if signo not in operaciones_validas:
        print ("la operacion no esta hablitada")
    if signo == "+":
        print(suma(var1, var2))
    if signo == "-":
        print(resta(var1, var2))
    if signo == "*":
        print(multiplicacion(var1, var2))


motor_de_operaciones()