def indicaciones():
    print ("Esta es la prueba de una calculadora de 'basica'")
    print ("los unicos signos permitidos para el uso de esta calculadora son: /n")

def operacion (a, b, signo):
    resultado = 0
    if signo == "+": 
        resultado = a + b
    if signo == "-": 
        resultado = a - b
    if signo == "*": 
        resultado = a * b
    if signo == "/": 
        resultado = a / b
    print (resultado)
    return resultado 

def eleccion_operacion ():
    operaciones_validas ={"+", "*", "-", "/", "="}
    signo = input ("ingresa un signo aritmetico de '+', '-', '*', '/' ")
    if signo in operaciones_validas:
        return signo, operaciones_validas
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
    

def segunda_operacion_fun ():
    segunda_operacion = input("esperando")
    try:
        numero = float (segunda_operacion)
        validar_numero = True

    except ValueError:
        validar_numero = False

    if validar_numero == True:
        print ("es un numero")
        return numero 
    else:
        signo = str(segunda_operacion)
        return signo
    

def motor_de_operaciones():
    valor1 = ingreso_de_numeros()
    signo, signo_segunda_suma = eleccion_operacion()
    valor2 = ingreso_de_numeros()
    proceso = operacion(valor1, valor2, signo)
    resultado = proceso
    print (f"este es el valor que volveremos a usar {resultado}")
    segunda_operacion_var = segunda_operacion_fun()
    print (type(segunda_operacion_var))
    if isinstance (segunda_operacion_var, float):
        print ("la segunda fue considerada como un numero")
        motor_de_operaciones()
    if isinstance (segunda_operacion_var, str):
        valor2 = ingreso_de_numeros()
        segunda_operacion = operacion(resultado, valor2, segunda_operacion_var)
        print (segunda_operacion)
    else:
        print ("para poder continuar con las operaciones debe de ser un signo o un numero")







motor_de_operaciones()