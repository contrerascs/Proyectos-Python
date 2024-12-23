def num_primos(num):
    for numero in range(num):
        if numero == 0 :
            pass
        elif numero == 1:
            pass
        elif num == 2:
            print(f'El numero {num} es un numero primo')
        elif num%numero == 0:
            print(f'El numero {num} no es un numero primo')
            break
        elif numero == (num-1):
            print(f'El numero {num} es un numero primo') 
        
Lista = []
longitud = int(input('Ingresa el tamaño de la lista: '))
for i in range(longitud):
    num = int(input('Ingresa un numero: '))
    Lista.append(num)

for elemento in Lista:
    num_primos(elemento)