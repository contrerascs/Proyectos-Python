def recursividad(num):
    if num == 0:
        return 0
    else:
        return num + recursividad(num -1)
    
print(recursividad(7))