
def primo_prime(num):
    def primo():
        for i in range(2,num):
            if num%i==0:
                return False
    esprimo=primo()
    if esprimo is False:
        print(num ,' no es primo')
    else:
        print(num ,' es primo')

num=int(input('ingrese el numero :'))
if num>=1 and num<=15:
    primo_prime(num)
