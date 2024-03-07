def edadAfter():
    edad = int(input('ingrese su edad : '));
    num = int(input('ingrese en cuantos años desea saber su edad : '));
    suma = edad+num;
    print(f'usted en {num} años tendra {suma} años de edad');

def operator():
    num1=float(input('ingrese el primer numero a operar : '))
    num2=float(input('ingrese el segundo numero a operar : '))
    producto=num1*num2
    cociente=num1/num2
    suma=num1+num2
    resta=num1-num2
    modulo=num1%num2
    print(f'los numero ingresados son {num1} y {num2} el modulo es: {modulo} , el cociente es : {cociente} , la suma es {suma} , la resta es : {resta} , la multiplicacion es {producto} .')

def prestamo():
    interes=0.027
    prestamo=float(input('ingrese el prestamo que desea solicitar : '))
    meses=int(input('ingrese la cantidad de meses de plazo para pagar : '))
    pago_mes=(prestamo/meses)
    aumento=interes*pago_mes
    total_mes=round(pago_mes+aumento,2)
    print(f'el valor de las cuotas mensuales es {total_mes} con un interes fijo de 2.7% mensual')

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

def iva():
    producto=float(input('ingrese el precio del producto : '))
    iva=0.19;
    aumento=producto*iva
    precio=aumento+producto
    print(f'El producto con precio {producto} mas el iva del 19% da como resultado final {precio}')

def descuento():
    producto=float(input('ingrese el precio del producto : '))
    descuento=0.1
    decremento=producto*descuento
    precio=producto-decremento
    print(f'el precio final del producto con precio de {producto} menos el descuento del 10% da {precio}')

def percent():
    num=float(input('ingrese el numero : '))
    percent=float(input('ingrese el porcentaje : '))
    result=(num*percent)/100
    print (f'{result} es el {percent}% de {num}')

#
# Hecho por Kevin Esneider Ocampo Osorio
#

#los ejercicios se encuentran en orden de enumeracion
# areaTriangle()
# circle()
# cubo()
# iva()
# descuento()
# percent()