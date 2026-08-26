var1 = int(input("ingresa un numero"))
signo = input ("ingresa el signo de la operacion que quieras realizar")
var2 = int(input("ingresa un segundo numero"))
operaciones_validas ={"+", "*", "-"}

if  signo not in operaciones_validas:
    print ("la operacion no esta hablitada")
if signo == "+":
    suma = var1 + var2
    print (suma)
if signo == "-":
    resta = var1 - var2
    print (resta)
if signo == "*":
    multiplicacion = var1 * var2  
    print (multiplicacion)

 
