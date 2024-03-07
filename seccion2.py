def areaTriangle():
    base=float(input('ingrese la base de tringulo : '))
    altura=float(input('ingrese la altura de tringulo : '))
    area=(base*altura)/2
    print(f'el area del triangulo con base {base} y altura {altura} es igual a {area}')

def circle():
    radio =float(input('indique el radio del circulo : '))
    pi=3.1416
    area=pi*(radio**2)
    diametro=radio*2
    perimetro=diametro*pi
    print(f'el circulo con radio {radio} posee un area de {area} y un perimetro {perimetro}')

def cubo():
    lado=float(input('ingrese la medida de un lado del cubo : '))
    volumen=lado**3
    print(f'el volumen de cubo con lado {lado} es {volumen}')

#
# Hecho por Kevin Esneider Ocampo Osorio
#

# areaTriangle()
# circle()
# cubo()