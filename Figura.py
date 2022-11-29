import math
#clase padre, con parametros y funciones basicas que todos los hijos deben tener
class Figura():
    def __init__(self, n_lados):
        self.n_lados = n_lados
    
    def perimetro (self):
        pass
        
    def area(self):
        pass

#clase cuadrado

class Cuadrilatero(Figura):
    def __init__(self, lado, altura):
        super().__init__(4)
        self.lado =lado
        self.altura = altura
    
    def perimetro (self):
        perimetro= self.lado+self.altura+self.altura+self.lado
        return perimetro
        
    def area(self):
        area= self.lado*self.altura
        return area
class Cuadrado (Cuadrilatero):
    def __init__ (self, lado):
        super().__init__(lado, lado)
        self.lado = lado

#clase rectangulo
class Rectangulo(Cuadrilatero):
    def __init__(self, lado1, lado2):
        super().__init__(lado1, lado2)
        self.lado1=lado1
        self.lado2=lado2
        

#clase rombo
class Rombo(Cuadrilatero):
    def __init__(self, lado, altura):
        super().__init__(lado, altura)
        self.lado=lado
        self.altura=altura        
#cuadrado=Cuadrado(7)
#print(cuadrado.area(), cuadrado.perimetro())
#rectangulo=Rectangulo(5,4)
#print(rectangulo.area(), rectangulo.perimetro())

#clase triangulo
class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(3)
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        
        
    def area (self):
        semiPer=(self.lado1+self.lado2+self.lado3)/2
        area=math.sqrt(semiPer*(semiPer-self.lado1)*(semiPer-self.lado2)*(semiPer-self.lado3))
        return area
        
    def perimetro (self):
        perimetro = self.lado1+self.lado2+self.lado3
        return perimetro
#triangulo=Triangulo(3,4,5)
#print(triangulo.perimetro())
#clase pentagono
class Pentagono(Figura):
    def __init__(self, lado, apotema):
        super().__init__(5)
        self.lado =lado
        self.apotema =apotema
        
        
    def perimetro(self):
        perimetro = self.lado*self.n_lados
        return perimetro

    def area (self):
        checkApotema=self.lado/2*math.sqrt(1+2/math.sqrt(5))
        if(self.apotema==checkApotema):
            area=5*self.lado*self.apotema/2
            return (area)
        else:
            return "el apotema introducida y el lado no son compatibles"

