def triangulo_valido():
    angulo1=float(input('Ingrese el primer angulo interno del triangulo : '))
    angulo2=float(input('Ingrese el segundo angulo interno del triangulo : '))
    angulo3=float(input('Ingrese el tercer angulo interno del triangulo : '))
    if angulo1+angulo2+angulo3==180:
        print('Es valido como triangulo .')
    else:
        print('no es valido como triangulo')

def parImpar():
    num=float(input('ingrese el numero : '))
    if num%2==0:
        print(f'{num} es par .')
    else:
        print(f'{num} es impar .')

def divPor5():
    num=float(input('ingrese el numero : '))
    if num%5==0:
        print(f'{num} es divisible por 5 . ')
#
# Hecho por kevin Ocampo
#
# triangulo_valido()
# parimpar
# divPor5()