#Definimos la función para evaluar la palabra
def palindromo(palabra):
    #Eliminamos espacios y convertimos a minúsculas
    sin_espacios = palabra.replace(" ", "").lower()
    print(sin_espacios)
    comparacion = str('')
    #Utilizamos un ciclo for para la comprobación
    for index,letra in enumerate(sin_espacios):
        if letra == sin_espacios[-(index+1)]:
            comparacion = comparacion+letra
            if comparacion == sin_espacios:
                print('La palabra es un Palindromo')
        else:
            print('La palabra no es un palindromo')
            break

palabra = str(input('Ingresa la primera palabra: '))
palindromo(palabra)
