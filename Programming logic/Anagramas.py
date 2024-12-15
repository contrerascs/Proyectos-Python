palabra1 = input(str(print('Dame la primer palabra')))
palabra2 = input(str(print('Dame la segunda palabra')))

def recursividad(palabra):
    return recursividad(palabra-1)

resultado = ''
if len(palabra1) == len(palabra2):
    for letra in palabra1:
        for letra2 in palabra2:
            if letra == letra2:
                palabra2 = palabra2.replace(letra2,'',1)
                palabra1 = palabra1.replace(letra,'',1)
                if palabra2 == '':
                    if palabra1 == '':
                        print('Las palabras son Anagramas')
                        break
                    else:
                        print('Las palabras no son Anagramas')
else:
    print('Las palabras no son Anagramas')