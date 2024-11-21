import pandas as pd
import numpy as np

#Crear lista de numeros de telefonos en un archivo TXT/CSV (10 digitos)
numeros = np.random.randint(1000000000, 9999999999, size=100, dtype=np.int64)
#Exportamos estos numeros a un archivo txt
numeros.tofile(r'Automate-TXT/numero-telefonos-2.txt', sep='\n')
#Exportamos estos numeros a un archivo csv
numeros.tofile(r'Automate-TXT/numero-telefonos-2.csv', sep='\n')