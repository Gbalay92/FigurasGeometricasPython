#Fichero de calculos
import math

def pedirOperandos(operando1, operando2, operando3):
    try:
        x = float(input("introduzca el "+ operando1 + ": "))
        if(operando2):
            y = float(input("introduzca el "+ operando2 + ": "))
            if(operando3):
                z = float(input("introduzca el "+ operando2 + ": "))
                return x,y,z
            else:
                return x, y
        else:
            return x
    except TypeError:
        print("introduzca solo numeros.")
    

def areaCuadrado():
    lado=pedirOperandos("lado", False, False)
    area=lado**(2)
    return "el area del cuadrado es: "+ str(area)

def areaRectangulo():
    operando1, operando2 = pedirOperandos("operando1", "operando2", False)
    area=operando1*operando2
    return "El area del rectangulo es: "+ str(area)

def areaPentagono():
    lado, apotema=pedirOperandos("lado", "apotema", False)
    checkApotema=lado/2*math.sqrt(1+2/math.sqrt(5))
    if(apotema==checkApotema):
        area=5*lado*apotema/2
        return "el area del pentagono es: " + str(area)
    else:
        return "el apotema introducida y el lado no son compatibles"

def areaRombo():
    lado, altura = pedirOperandos("lado", "altura", False)
    area=altura*lado
    return "el area del Rombo es: " + str(area)

def areaTriangulo():
    lado1, lado2, lado3=pedirOperandos("lado1", "lado2", "lado3")
    semiPer=(lado1+lado2+lado3)/2
    area=math.sqrt(semiPer*(semiPer-lado1)*(semiPer-lado2)*(semiPer-lado3))
    return "el area del Triangulo es: " + str(area)

def perimetroCuadrado():
    lado=pedirOperandos("lado", False, False)
    perimetro=lado*4
    return "el perimetro del cuadrado es: " + str(perimetro)

def perimetroRectangulo():
    lado1, lado2= pedirOperandos("lado 1", "lado 2", False)
    perimetro=lado1*2+lado2*2
    return "el perimetro del Rectangulo es: " + str(perimetro)

def perimetroPentagono():
    lado=pedirOperandos("lado", False, False)
    perimetro=lado*5
    return "el perimetro del Pentagono es: " + str(perimetro)

def perimetroTriangulo():
    lado1, lado2, lado3=pedirOperandos("lado 1", "lado 2", "lado 3")
    perimetro=lado1+lado2+lado3
    return "el perimetro del Triangulo es: " + str(perimetro)

def perimetroRombo():
    lado=pedirOperandos("lado", False, False)
    perimetro=lado*4
    return "el perimetro del Rombo es: " + str(perimetro)