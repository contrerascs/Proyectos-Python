def num_primos(num):
    for numero in range(num):
        if numero == 0 :
            pass
        elif numero == 1:
            pass
        elif num%numero == 0:
            print('El numero ingresado no es un numero primo')
            break
        elif numero == (num-1):
            print('El numero ingresado es un numero primo') 
        

num = int(input('Ingresa un numero: '))
num_primos(num)