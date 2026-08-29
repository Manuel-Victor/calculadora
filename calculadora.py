def indicaciones():
    print ("Esta es la prueba de una calculadora de 'basica'")
    print ("los unicos signos permitidos para el uso de esta calculadora son: /n")

#Las siguientes funciones seran las operaciones que tendran disponibles la calculadora
"""
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
def eleccion_signo():
    operaciones_validas ={"+", "*", "-", "/", "="}
""" 
def operacion (a, b, signo):
    if signo == "+": resultado = a + b
    if signo == "-": resultado = a - b
    if signo == "*": resultado = a * b
    if signo == "/": resultado = a / b
    print (resultado)
    return resultado 

def eleccion_operacion ():
    operaciones_validas ={"+", "*", "-", "/", "="}
    signo = input ("ingresa un signo aritmetico de '+', '-', '*', '/' ")
    if signo in operaciones_validas:
        return signo 
    else:
        print ("los unicos signos aritmeticos que puedes usar son '+', '-', '*', '/' ")

def ingreso_de_numeros():
    while True:
        try:
            nro_para_operaciones = float(input("ingresa el numero"))
            print (nro_para_operaciones)
            return nro_para_operaciones
        except:
            ValueError 
            print("Solo puedes ingresar numeros")
    



def motor_de_operaciones():
    valor1 = ingreso_de_numeros()
    signo = eleccion_operacion ()
    valor2 = ingreso_de_numeros()
    proceso = operacion(valor1, valor2, signo)
    resultado = proceso
    print (f"este es el valor que volveremos a usar {resultado}")




motor_de_operaciones()

"""
        try:
            var1 = int(input("ingrese el primer valor"))
            signo = input ("ingresa un signo aritmetico valido")
            if signo in operaciones_validas:
                var2 = int(input("ingresa el segundo numero"))
                if signo == "+":
                    resultado = suma(var1, var2)
                    print (resultado)
                if signo == "-":
                    resultado = resta(var1, var2)
                    print (resultado)
                if signo == "*":
                    resultado = multiplicacion(var1, var2)
                    print (resultado)
                while True: 
                    if segunda_operacion == "esc":
                        print ("el sistema finalizara")
                        break 
                    if signo in operaciones_validas:
                        var2 = int(input("ingresa el segundo numero"))
                        if signo == "+":
                            resultado = suma(var1, var2)
                            print (resultado)
                        if signo == "-":
                            resultado = resta(var1, var2)
                            print (resultado)
                        if signo == "*":
                            resultado = multiplicacion(var1, var2)
                            print (resultado)

            else:     
                print ("la operacion no esta hablitada")
                print ("intentelo nuevamente")

        except ValueError:
            print("solo se pueden ingresar numeros validos")
""" 


#motor_de_operaciones()