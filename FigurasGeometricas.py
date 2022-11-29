from optparse import Values
from OperationsOO import *
import argparse
#Escribe menu principal
def escribirMenu():
    print("FIGURAS GEOMETRICAS\n1. Triangulo\n2. Cuadrado\n3. Rectangulo\n4. Pentagono\n5. Rombo\n0. Salir\nElija una opcion: ")
    
#Escribe submenu
def areaOPerimetro():
    print("¿Que desea calcular?\n1. area\n2. perimetro: ")

def main():
    while(True):
        escribirMenu()
        try:
            opcion=int(input())
            match(opcion):
                case 1:
                    #triangulo
                    triangulo=crearTriangulo()
                    areaOPerimetro()
                    opcion2=int(input())
                    if(opcion2==1):
                        print(triangulo.area())
                    elif(opcion2==2):
                        print(triangulo.perimetro())
                    else:
                        print("introduzca una opcion correcta")
                case 2:
                    #cuadrado
                    cuadrado=crearCuadrado()
                    areaOPerimetro()
                    opcion2=int(input())
                    if(opcion2==1):
                        print(cuadrado.area())
                    elif(opcion2==2):
                        print(cuadrado.perimetro())
                    else:
                        print("introduzca una opcion correcta")
                case 3:
                    #rectangulo
                    rectangulo=crearRectangulo()
                    areaOPerimetro()
                    opcion2=int(input())
                    if(opcion2==1):
                        print(rectangulo.area())
                    elif(opcion2==2):
                        print(rectangulo.perimetro())
                    else:
                        print("introduzca una opcion correcta")
                case 4:
                    #pentagono
                    pentagono=crearPentagono()
                    areaOPerimetro()
                    opcion2=int(input())
                    if(opcion2==1):
                        print(pentagono.area())
                    elif(opcion2==2):
                        print(pentagono.perimetro())
                    else:
                        print("introduzca una opcion correcta")
                case 5:
                    #rombo
                    rombo=crearRombo()
                    areaOPerimetro()
                    opcion2=int(input())
                    if(opcion2==1):
                        print(rombo.area())
                    elif(opcion2==2):
                        print(rombo.perimetro())
                    else:
                        print("introduzca una opcion correcta")
                case 0:
                    exit()
                case other:
                    print("introduzca una opcion correcta")
        except ValueError:
            print("introduzca solo numeros")

#añadimos argumentos al arg parse
if __name__=="__main__":
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lado', nargs='+', type=float, help='lado tipo: float, este argumento acepta mas de un parametro dependiendo de la figura')
    #-l es para introducir el lado, el parametro nargs le dice que tiene que tener 1 o mas argumentos
    parser.add_argument('-a', '--altura', type=float, help='altura o apotema(solo pentagono) de la figura tipo: float', required=False)
    parser.add_argument('-f', '--figura',
                    type=str,
                    required=False,
                    help='opciones: cuadrado, rectangulo, rombo, pentagono, triangulo\rfigura a construir con l y a. tipo: str')
    #el parametro -f es para figura, a partir de este comparando el string introducido se creara la figura y dara los calculos de area y perimetro
    args=parser.parse_args()
    #args sera la variable en la que se almacenan los float o strings introducidos
    #para referenciar a parametro concreto usaremos args.parametro donde parametro es el nombre que se indica en add_argument: --altura por ejemplo seria args.altura
    if not any(vars(args).values()):
        #ejecuta programa sin argumentos
        main()
    elif args.figura=='cuadrado':
        #crea cuadrado y calcula parametros
        cuadrado=Cuadrado(args.lado[0])
        print('perimetro: ',str(cuadrado.perimetro()),'\narea: ', str(cuadrado.area()))
    elif args.figura=='rectangulo':
        #crea rectangulo y calcula parametros
        if len(args.lado)==1:
            rectangulo=Rectangulo(args.lado[0],args.altura)
            print('perimetro: ',str(rectangulo.perimetro()),'\narea: ', str(rectangulo.area()))
        if len(args.lado)>1:
            rectangulo=Rectangulo(args.lado[0],args.lado[1])
            print('perimetro: ',str(rectangulo.perimetro()),'\narea: ', str(rectangulo.area()))
    elif args.figura=='rombo':
        #crea rombo y calcula parametros
        rombo=Rombo(args.lado[0],args.altura)
        print('perimetro: ',str(rombo.perimetro()),'\narea: ', str(rombo.area()))
    elif args.figura=='pentagono':
        #crea pentagono y calcula parametros
        pentagono=Pentagono(args.lado[0],args.altura)
        print('perimetro: ',str(pentagono.perimetro()),'\narea: ', str(pentagono.area()))
    elif args.figura=='triangulo':
        #crea triangulo y calcula parametros
        triangulo=Triangulo(args.lado[0],args.lado[1],args.lado[2])
        print('perimetro: ',str(triangulo.perimetro()),'\narea: ', str(triangulo.area()))
    else:
        print('introduzca parametros validos. Use el comando --help si desea desplegar la ayuda')





