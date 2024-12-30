def pascal(n):
    triangle = []
    for i in range(n):
        # Inicializar la nueva fila
        row = [1] * (i + 1)
         # Completar los valores intermedios de la fila
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        # Agregar la fila al triángulo
        triangle.append(row)

    return triangle

num = int(input('Ingresa el tamaño de la piramide'))
print(pascal(num))