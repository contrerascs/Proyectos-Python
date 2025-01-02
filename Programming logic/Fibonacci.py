#Definimos una función recursiva para crear la secuencia
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return (fibonacci(num-1)+fibonacci(num-2))
        

# Solicitamos al usuario el tamaño de la secuencia
fib = int(input('Ingresa el tamaño de la secuencia de Fibonacci: '))
secuencia = []

for i in range(fib+1):
    secuencia.append(fibonacci(i))

print(secuencia)