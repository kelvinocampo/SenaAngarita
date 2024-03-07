def asc_desc():
    for i in range(101):
        print(i)
    for i in range(100,-1,-1):
        print(i)

def tabla_3():
    for i in range(51):
        print(f'3 x {i} = {3*i}')

def promedio():
    n=int(input('ingrese la cantidad de estudiantes a evaluar'))
    for i in range(1,n+1):
        nota1=int(input('ingrese la primera nota : '))
        nota2=int(input('ingrese la segunda nota : '))
        nota3=int(input('ingrese la tercera nota : '))
        promedio=(nota1+nota2+nota3)/3
        print(f'el estudiante {i} tiene un promedio de {promedio}')

def factorial():
    n=int(input('ingrese el numero a calcular: '))
    result=1
    for i in range(n,0,-1):
        result*=i
    print(result)

#
#Hecho por Kevin Ocampo
#
# tabla_3()
# asc_desc()
# promedio()
# factorial()