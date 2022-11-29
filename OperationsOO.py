import math
from Figura import *

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
    
def crearCuadrado():
    lado=pedirOperandos("lado", False, False)
    cuadrado=Cuadrado(lado)
    return cuadrado
    
def crearRectangulo():
    lado1, lado2= pedirOperandos("lado 1", "lado 2", False)
    rectangulo=Rectangulo(lado1, lado2)
    return rectangulo
    
def crearTriangulo():
    lado1, lado2, lado3=pedirOperandos("lado 1", "lado 2", "lado 3")
    triangulo=Triangulo(lado1, lado2, lado3)
    return triangulo
    
def crearPentagono():
    lado, apotema= pedirOperandos("lado", "apotema", False)
    pentagono = Pentagono(lado, apotema)
    return pentagono

def crearRombo():
    lado, altura= pedirOperandos("lado", "altura", False)
    rombo = Rombo(lado, altura)
    return rombo

