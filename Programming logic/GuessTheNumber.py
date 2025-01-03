import random 
def guess(num,secreto):
    if num > secreto:
        print('El numero en el que estoy pensando es menor')
        return False
    elif num < secreto:
        print('El numero en el que estoy pensando es mayor')
        return False
    elif num == secreto:
        print('CORRECTO!!! ADIVINASTE EL NUMERO')
        return True

num = int(input('Estoy pensando en un numero del 1 al 100, intenta adivinarlo '))
secreto = random.randint(1,100)

contador = guess(num,secreto)
while contador == False:
    num2 = int(input('Intenta otra vez '))
    contador = guess(num2,secreto)