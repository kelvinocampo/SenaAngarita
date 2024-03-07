def numMayor():
    num1=float(input('ingrese el primer numero : '))
    num2=float(input('ingrese el segundo numero : '))
    if(num1 == num2):
        print('los dos numeros ingresados son iguales .')
    elif(num1>num2):
        print('el primer numero ingresado es el mayor .')
    else:
        print('el segundo numero ingresado es el mayor .')

def productoIva():
    producto = input('Ingrese el producto: ')
    if producto == 'crema' or producto == 'vino':
        print('El producto paga IVA.')
    elif producto == 'lentejas' or producto == 'arroz':
        print('El producto no paga IVA.')
    else:
        print('El producto ingresado no se encuentra en el supermercado.')

#
# Hecho por kevin Ocampo
#
# productoIva()
# numMayor()