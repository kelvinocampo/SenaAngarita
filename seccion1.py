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

#
# Hecho por Kevin Esneider Ocampo Osorio
#
# operator()
# edadAfter()
# prestamo()