def burbuja(lista):
    for e,i in enumerate(lista):
        if (e+1) == len(lista):
            break
        elif lista[e] >= lista[e+1]:
            lista[e] = lista[e+1]
            lista[e+1] = i
            print(lista)
        
    print(lista)

Lista = [9,8,7,6,5,4,3,2,1]
burbuja(Lista)