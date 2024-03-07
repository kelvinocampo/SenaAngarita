#
# Hecho por Kevin Esneider Ocampo Osorio
#

def percentNum():
    percent=float(input('ingrese el porcentaje : '))
    num=float(input('ingrese el numero : '))
    result=(num*percent)/100
    print (f'{result} es el {percent}% de {num}')
    return result


#calcula el porcentaje necesario para sacar el numero original
def calcPercentNeeded():
    numPercent=float(input('ingrese el porcentaje : '))
    numOrigin=float(input('ingrese el numero : '))
    result=((numPercent/numOrigin)*100)
    
    print (f'{result} es el % necesario de {numOrigin} para dar {numPercent}')
    return result


def aumentoPercent():
    percent=float(input('ingrese el aumento porcentual : '))
    num=float(input('ingrese el numero : '))
    aumento=percentNum(percent,num)
    result=num+aumento
    
    print(f'luego de hacer un aumento del {percent}% a {num} nos da {result}')
    return result


def descuentoPercent():
    percent=int(input('ingrese el descuento porcentual : '))
    num=int(input('ingrese el numero : '))
    descuento=percentNum(percent,num)
    result=num-descuento
    
    print(f'luego de hacer un descuento del {percent}% a {num} nos da {result}')
    return result


# calcPercentNeeded()
# percentNum()
# descuentoPercent()
# aumentoPercent()