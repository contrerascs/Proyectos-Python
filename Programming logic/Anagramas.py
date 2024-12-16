# Solicitar las palabras del usuario
palabra1 = input('Dame la primer palabra: ')
palabra2 = input('Dame la segunda palabra: ')

# Eliminar espacios y convertir a minúsculas para comparar correctamente
palabra1 = palabra1.replace(" ", "").lower()
palabra2 = palabra2.replace(" ", "").lower()

resultado = ''
if len(palabra1) == len(palabra2):
    for letra in palabra1:
        contador = 0
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
                        break
            if letra != letra2:
                contador += 1
                if contador == len(palabra1):
                    print('Las palabras no son Anagramas')
                    break
else:
    print('Las palabras no son Anagramas')