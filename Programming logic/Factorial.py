def factorial(num):
    if num == 0:
        return 1
    else:
        return (num*factorial(num-1))

numero = int(input('Ingresa un numero y te regresare su factorial '))
print(factorial(numero))